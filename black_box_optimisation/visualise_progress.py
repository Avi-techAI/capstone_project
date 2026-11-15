"""
Black Box Capstone Project - progress visualisation
Cohort IMP-PCMLAI-26-06 | Avi Thakur

Regenerates every figure from two sources:
  initial_data/function_N/*.npy   (course-provided starting data)
  submissions.json                (our weekly inputs and outputs)

Usage:
    python visualise_progress.py

Each week: add the new output to submissions.json, re-run this script.
All figures are written to figures/.
"""

import json
import os
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec
from scipy.optimize import minimize
from scipy.stats import norm, qmc, spearmanr
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel as C
from sklearn.gaussian_process.kernels import Matern, WhiteKernel

warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "initial_data")
FIGS = os.path.join(HERE, "figures")
os.makedirs(FIGS, exist_ok=True)

# House style
NAVY, TEAL, AMBER, RED, GREY = "#1B2A4A", "#2A9D8F", "#E9C46A", "#E05A47", "#8C93A8"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "#CBD2E0",
    "axes.labelcolor": NAVY,
    "axes.titlecolor": NAVY,
    "axes.titleweight": "bold",
    "text.color": NAVY,
    "xtick.color": GREY,
    "ytick.color": GREY,
    "axes.grid": True,
    "grid.color": "#EDF0F5",
    "grid.linewidth": 0.9,
    "axes.axisbelow": True,
    "figure.dpi": 130,
})


# ---------------------------------------------------------------- data loading

def load_all():
    with open(os.path.join(HERE, "submissions.json")) as fh:
        sub = json.load(fh)
    out = {}
    for i in range(1, 9):
        key = f"F{i}"
        X0 = np.load(f"{DATA}/function_{i}/initial_inputs.npy")
        Y0 = np.load(f"{DATA}/function_{i}/initial_outputs.npy")
        wk = sub["functions"][key]["weeks"]
        wx, wy, wn = [], [], []
        for w in sorted(wk, key=int):
            if wk[w]["output"] is not None:
                wx.append(wk[w]["input"])
                wy.append(wk[w]["output"])
                wn.append(int(w))
        pending = {int(w): wk[w]["input"] for w in wk if wk[w]["output"] is None}
        out[key] = dict(dim=sub["functions"][key]["dim"], X0=X0, Y0=Y0,
                        wx=np.array(wx).reshape(-1, X0.shape[1]) if wx else np.empty((0, X0.shape[1])),
                        wy=np.array(wy), weeks=wn, pending=pending)
    return sub, out


# ---------------------------------------------------------------- GP machinery

def rank_gauss(y):
    """Monotone rank -> normal score. Preserves argmax, removes scale pathology."""
    n = len(y)
    r = np.argsort(np.argsort(y))
    return norm.ppf((r + 0.5) / n)


def standardise(y):
    """Plain z-score. Keeps magnitude information that rank_gauss discards."""
    return (y - y.mean()) / y.std()


# Output transform chosen per function by cross-validation, not assumed.
# Selection metric: Spearman(true y, leave-one-out prediction). That metric is
# comparable across transforms because every transform here is monotone, so it
# preserves ordering. R2 is NOT comparable across transforms - a transform that
# compresses variance inflates it.
#
# Measured Spearman (raw vs rank):
#   F1 -0.118 / +0.555   F2 +0.645 / +0.645   F3 +0.535 / +0.753
#   F4 +0.975 / +0.902   F5 +0.566 / +0.475   F6 +0.738 / +0.864
#   F7 +0.491 / +0.773   F8 +0.983 / +0.973
#
# Rank wins where the output scale is pathological or heavily skewed (F1 spans
# 1e-124 to 1e-16). Raw wins where magnitude carries real signal, most
# importantly F5, whose range 0.11 to 1088 means a rank transform throws away
# the fact that its best point is an order of magnitude above the rest.
TRANSFORM = {"F1": "rank", "F2": "raw", "F3": "rank", "F4": "raw",
             "F5": "raw", "F6": "rank", "F7": "rank", "F8": "raw"}


def transform(key, y):
    """Apply the cross-validated transform for this function."""
    return rank_gauss(y) if TRANSFORM.get(key, "rank") == "rank" else standardise(y)


def make_gp(d):
    """ARD Matern GP.

    length_scale_bounds=(0.05, 3.0) is deliberate. Inputs live in [0,1], so a
    length-scale of 100 is meaningless - it lets the optimiser declare a
    dimension entirely irrelevant, which it did for F2 x2, F3 x2 and F8 x6/x8
    on only 11-41 points. A floor of 0.05 stops the opposite failure, where the
    kernel collapses to white noise and the GP learns nothing.
    Validated by leave-one-out: these bounds beat (1e-2, 1e2) on 6 of 8
    functions (F7 0.43 -> 0.64, F6 0.67 -> 0.73) and lose by <=0.013 elsewhere.
    """
    k = (C(1.0, (1e-3, 1e3))
         * Matern(length_scale=np.ones(d), nu=2.5, length_scale_bounds=(0.05, 3.0))
         + WhiteKernel(1e-4, (1e-8, 1e-1)))
    return GaussianProcessRegressor(kernel=k, normalize_y=False,
                                    n_restarts_optimizer=15, random_state=0)


def expected_improvement(X, gp, z_best, xi):
    mu, s = gp.predict(X, return_std=True)
    s = np.maximum(s, 1e-12)
    imp = mu - z_best - xi
    z = imp / s
    return imp * norm.cdf(z) + s * norm.pdf(z)


def loo(X, z, d):
    """Leave-one-out: does the GP beat simply predicting the mean?"""
    p = np.empty(len(X))
    for i in range(len(X)):
        m = np.ones(len(X), bool)
        m[i] = False
        g = make_gp(d)
        g.fit(X[m], z[m])
        p[i] = g.predict(X[i:i + 1])[0]
    r2 = 1 - np.sum((z - p) ** 2) / np.sum((z - z.mean()) ** 2)
    return r2, spearmanr(z, p).correlation, p


def combined(rec):
    X = np.vstack([rec["X0"], rec["wx"]]) if len(rec["wx"]) else rec["X0"]
    Y = np.concatenate([rec["Y0"], rec["wy"]]) if len(rec["wy"]) else rec["Y0"]
    return X, Y


# ---------------------------------------------------------- 1. convergence

def fig_convergence(d, total_weeks=13):
    """Best-so-far per week.

    Two traps avoided. (1) matplotlib's offset notation ("1e-6+1.36496")
    magnifies a change of 0.0000018 into a dramatic climb - switched off.
    (2) With one week of data the y-axis auto-scales to a sliver, so a
    negligible move fills the panel; the axis is padded relative to the
    value's own magnitude and a "no material change" flag is printed when
    the total gain is under 0.1% of |baseline|.
    """
    fig, axes = plt.subplots(2, 4, figsize=(17, 7.8))
    fig.suptitle("Optimisation progress: best output found so far",
                 fontsize=15, fontweight="bold", y=0.985)
    for ax, (k, rec) in zip(axes.ravel(), d.items()):
        base = float(np.max(rec["Y0"]))
        weeks = [0] + rec["weeks"]
        running, cur = [base], base
        for y in rec["wy"]:
            cur = max(cur, float(y))
            running.append(cur)

        ax.axhline(base, color=GREY, ls=":", lw=1.2, zorder=1)
        # shade the submissions still unused
        ax.axvspan(max(weeks) + 0.5, total_weeks + 0.5, color="#F4F6FA", zorder=0)
        ax.plot(weeks, running, "-o", color=TEAL, lw=2.2, ms=7,
                mfc="white", mew=2, zorder=3)

        gain = running[-1] - base
        material = abs(gain) > 1e-3 * max(abs(base), 1e-300)
        for j in range(1, len(running)):
            if running[j] > running[j - 1] and material:
                ax.plot(weeks[j], running[j], "o", color=AMBER, ms=11, zorder=2)

        ax.set_title(f"{k}  ({rec['dim']}D)", fontsize=11.5, pad=9)
        ax.set_xlabel("week  (0 = initial data)", fontsize=9)
        ax.set_ylabel("best output", fontsize=9)
        ax.set_xlim(-0.5, total_weeks + 0.5)
        ax.set_xticks(range(0, total_weeks + 1, 2))
        # plain ticks normally, but scientific where the scale demands it
        # (F1 lives at 1e-16; "plain" would print a column of zeros)
        mag = max(abs(min(running)), abs(max(running)))
        if mag and (mag < 1e-3 or mag > 1e5):
            ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0),
                                useOffset=False)
            ax.yaxis.get_offset_text().set_fontsize(8)
        else:
            ax.ticklabel_format(axis="y", style="plain", useOffset=False)

        # pad y relative to magnitude so a trivial change cannot fill the panel
        lo, hi = min(running), max(running)
        span = max(hi - lo, 0.04 * max(abs(hi), 1e-300), 1e-300)
        ax.set_ylim(lo - 0.55 * span, hi + 0.55 * span)

        note = f"best {running[-1]:.5g}"
        if not material:
            note += "\n(no material gain yet)"
        ax.text(0.97, 0.06, note, transform=ax.transAxes, ha="right", va="bottom",
                fontsize=8.5, fontweight="bold", color=NAVY,
                bbox=dict(fc="white", ec="#CBD2E0", boxstyle="round,pad=0.35",
                          alpha=0.95))
    fig.tight_layout(rect=[0, 0.02, 1, 0.945])
    fig.savefig(f"{FIGS}/01_convergence.png", bbox_inches="tight")
    plt.close(fig)


# -------------------------------------- 2. GP surface + EI for 2D functions

def fig_surface_2d(d, key):
    rec = d[key]
    X, Y = combined(rec)
    z = transform(key, Y)
    gp = make_gp(2)
    gp.fit(X, z)
    z_best, xi = z.max(), 0.01 * z.std()

    g = np.linspace(0, 0.999999, 170)
    A, B = np.meshgrid(g, g)
    P = np.c_[A.ravel(), B.ravel()]
    mu, sd = gp.predict(P, return_std=True)
    ei = expected_improvement(P, gp, z_best, xi)
    MU, SD, EI = mu.reshape(A.shape), sd.reshape(A.shape), ei.reshape(A.shape)

    nxt = rec["pending"].get(max(rec["pending"]) if rec["pending"] else None)
    fig = plt.figure(figsize=(16.5, 5.0))
    gs = gridspec.GridSpec(1, 3, wspace=0.26)
    panels = [("GP predicted mean", MU, "viridis"),
              ("GP uncertainty (sd)", SD, "magma"),
              ("Expected Improvement", EI, "cividis")]
    for n, (title, Z, cm) in enumerate(panels):
        ax = fig.add_subplot(gs[n])
        im = ax.contourf(A, B, Z, levels=45, cmap=cm)
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
        ax.scatter(rec["X0"][:, 0], rec["X0"][:, 1], s=46, c="white",
                   edgecolors="black", lw=1.1, label="initial data", zorder=4)
        if len(rec["wx"]):
            ax.scatter(rec["wx"][:, 0], rec["wx"][:, 1], s=95, marker="s",
                       c=AMBER, edgecolors="black", lw=1.2,
                       label="submitted", zorder=5)
        xb = X[np.argmax(Y)]
        ax.scatter(*xb, s=240, marker="*", c=RED, edgecolors="black",
                   lw=1.2, label="best so far", zorder=6)
        if nxt is not None:
            ax.scatter(*nxt, s=170, marker="X", c=TEAL, edgecolors="black",
                       lw=1.4, label="next pick", zorder=7)
        ax.set_title(title, fontsize=11.5)
        ax.set_xlabel("$x_1$")
        ax.set_ylabel("$x_2$")
        ax.grid(False)
        if n == 0:
            ax.legend(loc="lower left", fontsize=8, framealpha=0.92)
    fig.suptitle(f"{key} ({rec['dim']}D) - what the model believes, and why it picked the next point",
                 fontsize=13.5, fontweight="bold", y=1.04)
    fig.savefig(f"{FIGS}/02_surface_{key}.png", bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------- 3. model skill (LOO validation)

def fig_model_skill(d):
    fig, axes = plt.subplots(2, 4, figsize=(17, 7.6))
    fig.suptitle("Model validation: can the GP predict points it has never seen?",
                 fontsize=15, fontweight="bold", y=0.98)
    table = {}
    for ax, (k, rec) in zip(axes.ravel(), d.items()):
        X, Y = combined(rec)
        z = transform(k, Y)
        r2, rho, p = loo(X, z, rec["dim"])
        table[k] = (r2, rho)
        ok = r2 > 0.4
        col = TEAL if ok else RED
        lim = [min(z.min(), p.min()) - 0.3, max(z.max(), p.max()) + 0.3]
        ax.plot(lim, lim, ls="--", color=GREY, lw=1.2, zorder=1)
        ax.scatter(z, p, s=42, c=col, edgecolors="black", lw=0.8,
                   alpha=0.85, zorder=3)
        ax.set_xlim(lim)
        ax.set_ylim(lim)
        ax.set_title(f"{k}  ({rec['dim']}D)", fontsize=11.5)
        ax.set_xlabel("actual (rank score)", fontsize=9)
        ax.set_ylabel("predicted", fontsize=9)
        verdict = "trust EI" if ok else "weak - be careful"
        ax.text(0.04, 0.96, f"$R^2$ = {r2:.2f}\n$\\rho$ = {rho:.2f}\n{verdict}",
                transform=ax.transAxes, va="top", fontsize=9, fontweight="bold",
                color=col,
                bbox=dict(fc="white", ec=col, lw=1.2, boxstyle="round,pad=0.4",
                          alpha=0.95))
    fig.tight_layout(rect=[0, 0.02, 1, 0.95])
    fig.savefig(f"{FIGS}/03_model_skill.png", bbox_inches="tight")
    plt.close(fig)
    return table


# -------------------------------- 4. per-dimension sensitivity (any dim)

def fig_sensitivity(d):
    fig, axes = plt.subplots(2, 4, figsize=(17, 7.6))
    fig.suptitle("Which inputs matter? GP response along each dimension, through the best point",
                 fontsize=15, fontweight="bold", y=0.98)
    for ax, (k, rec) in zip(axes.ravel(), d.items()):
        X, Y = combined(rec)
        z = transform(k, Y)
        dim = rec["dim"]
        gp = make_gp(dim)
        gp.fit(X, z)
        xb = X[np.argmax(Y)].copy()
        g = np.linspace(0, 0.999999, 120)
        cmap = plt.get_cmap("viridis")
        for j in range(dim):
            P = np.tile(xb, (120, 1))
            P[:, j] = g
            mu, sd = gp.predict(P, return_std=True)
            c = cmap(j / max(1, dim - 1) * 0.85)
            ax.plot(g, mu, lw=2.0, color=c, label=f"$x_{{{j+1}}}$")
            ax.fill_between(g, mu - sd, mu + sd, color=c, alpha=0.10)
        ax.axhline(z.max(), color=RED, ls=":", lw=1.3)
        ax.set_title(f"{k}  ({dim}D)", fontsize=11.5)
        ax.set_xlabel("value of that input", fontsize=9)
        ax.set_ylabel("predicted score", fontsize=9)
        ax.legend(fontsize=7.5, ncol=2 if dim > 4 else 1, loc="best",
                  framealpha=0.9)
    fig.tight_layout(rect=[0, 0.02, 1, 0.95])
    fig.savefig(f"{FIGS}/04_sensitivity.png", bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------ 5. one-page status board

def fig_dashboard(d, skill, total_weeks):
    fig = plt.figure(figsize=(15, 6.4))
    fig.suptitle("Black Box Capstone - status board", fontsize=16,
                 fontweight="bold", y=0.99)
    gs = gridspec.GridSpec(1, 2, width_ratios=[1.25, 1], wspace=0.22)

    # left: submissions used vs remaining
    ax = fig.add_subplot(gs[0])
    keys = list(d)
    used = [len(d[k]["wy"]) for k in keys]
    pend = [len(d[k]["pending"]) for k in keys]
    left = [total_weeks - u - p for u, p in zip(used, pend)]
    y = np.arange(len(keys))
    ax.barh(y, used, color=TEAL, label="output received")
    ax.barh(y, pend, left=used, color=AMBER, label="submitted, awaiting output")
    ax.barh(y, left, left=np.array(used) + np.array(pend), color="#E8EBF2",
            label="remaining")
    ax.set_yticks(y)
    ax.set_yticklabels([f"{k} ({d[k]['dim']}D)" for k in keys])
    ax.invert_yaxis()
    ax.set_xlabel(f"weekly submissions (of {total_weeks})")
    ax.set_xlim(0, total_weeks)
    ax.set_title("Budget used", fontsize=12)
    ax.legend(fontsize=8.5, loc="lower right")
    ax.grid(axis="y", visible=False)

    # right: model skill
    ax2 = fig.add_subplot(gs[1])
    r2s = [skill[k][0] for k in keys]
    cols = [TEAL if v > 0.4 else (AMBER if v > 0.2 else RED) for v in r2s]
    ax2.barh(y, r2s, color=cols, edgecolor="black", lw=0.7)
    ax2.axvline(0.4, color=NAVY, ls="--", lw=1.3)
    ax2.text(0.41, -0.65, "trust threshold", fontsize=8.5, color=NAVY)
    ax2.axvline(0, color=GREY, lw=1)
    ax2.set_yticks(y)
    ax2.set_yticklabels(keys)
    ax2.invert_yaxis()
    ax2.set_xlabel("leave-one-out $R^2$")
    ax2.set_title("Model skill per function", fontsize=12)
    ax2.grid(axis="y", visible=False)
    # labels always sit to the right of zero so they never collide with ticks
    for yy, v in zip(y, r2s):
        ax2.text(max(v, 0.0) + 0.025, yy, f"{v:.2f}", va="center", ha="left",
                 fontsize=8.5, fontweight="bold")
    ax2.set_xlim(min(min(r2s) - 0.08, -0.12), 1.12)
    fig.tight_layout(rect=[0, 0.02, 1, 0.94])
    fig.savefig(f"{FIGS}/05_dashboard.png", bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------------------------- main

if __name__ == "__main__":
    sub, d = load_all()
    print("Generating figures ...")
    fig_convergence(d, sub["total_weeks"])
    print("  01_convergence.png")
    for k in ("F1", "F2"):
        fig_surface_2d(d, k)
        print(f"  02_surface_{k}.png")
    skill = fig_model_skill(d)
    print("  03_model_skill.png")
    fig_sensitivity(d)
    print("  04_sensitivity.png")
    fig_dashboard(d, skill, sub["total_weeks"])
    print("  05_dashboard.png")
    print(f"\nDone. {len(os.listdir(FIGS))} files in figures/")
    print("\nLeave-one-out skill:")
    for k, (r2, rho) in skill.items():
        print(f"  {k}: R2 {r2:+.3f}   Spearman {rho:+.3f}")
