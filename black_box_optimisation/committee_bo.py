"""Committee-of-surrogates Bayesian optimisation.
Modules drawn on: M9/M10 ensembles, M12 BO + acquisition functions,
M14 SVR, M15/M16 neural nets, M18 hyperparameter tuning + regularisation."""
import sys, json, warnings, numpy as np
warnings.filterwarnings('ignore'); sys.path.insert(0,'.')
from visualise_progress import rank_gauss, standardise, TRANSFORM
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel as C, Matern, RBF, RationalQuadratic, WhiteKernel
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from scipy.stats import norm, qmc
sub=json.load(open('submissions.json'))
NOISE={'F1':1e-8,'F2':0.043,'F3':0.0015,'F4':1e-5,'F5':0.0015,'F6':0.0151,'F7':1e-6,'F8':1e-8}
BEST=json.load(open('/tmp/best_models.json'))

def load(k):
    i=k[1]; X=np.load(f'initial_data/function_{i}/initial_inputs.npy'); Y=np.load(f'initial_data/function_{i}/initial_outputs.npy')
    for w in sorted(sub['functions'][k]['weeks'],key=int):
        d=sub['functions'][k]['weeks'][w]
        if d['output'] is not None:
            X=np.vstack([X,np.array(d['input']).reshape(1,-1)]); Y=np.append(Y,d['output'])
    return X,Y

def build(n,d,nz):
    g=lambda ker: GaussianProcessRegressor(kernel=ker,normalize_y=False,n_restarts_optimizer=3,random_state=0)
    wk=WhiteKernel(max(nz**2,1e-10),(1e-10,1.))
    return {
 'GP-Matern':g(C(1.,(1e-3,1e3))*Matern(np.ones(d),nu=2.5,length_scale_bounds=(.05,3.))+wk),
 'GP-RBF':g(C(1.,(1e-3,1e3))*RBF(np.ones(d),length_scale_bounds=(.05,3.))+wk),
 'GP-RatQuad':g(C(1.,(1e-3,1e3))*RationalQuadratic(length_scale_bounds=(.05,3.))+wk),
 'RandomForest':RandomForestRegressor(n_estimators=200,random_state=0,n_jobs=-1),
 'ExtraTrees':ExtraTreesRegressor(n_estimators=200,random_state=0,n_jobs=-1),
 'GradBoost':GradientBoostingRegressor(n_estimators=150,max_depth=3,learning_rate=.08,random_state=0),
 'SVR-RBF':make_pipeline(SVR(C=10.,gamma='scale',epsilon=.05)),
 'KNN-5':KNeighborsRegressor(n_neighbors=4,weights='distance'),
 'MLP-net':MLPRegressor(hidden_layer_sizes=(64,64),max_iter=1500,random_state=0,learning_rate_init=.01),
 'Poly2-Ridge':make_pipeline(PolynomialFeatures(2),RidgeCV(alphas=np.logspace(-4,3,30))),
}[n]

def predict(name,mdl,X,z,Q,d,nz,B=24):
    """Return mean and uncertainty. GPs natively; tree ensembles from the
    spread across estimators; everything else by bootstrap resampling."""
    if name.startswith('GP-'):
        mdl.fit(X,z); mu,sd=mdl.predict(Q,return_std=True); return mu,np.maximum(sd,1e-9)
    if name in ('RandomForest','ExtraTrees'):
        mdl.fit(X,z)
        P=np.stack([t.predict(Q) for t in mdl.estimators_])
        return P.mean(0),np.maximum(P.std(0),1e-9)
    P=[]
    rng=np.random.default_rng(0)
    for b in range(B):
        idx=rng.choice(len(X),len(X),replace=True)
        if len(np.unique(z[idx]))<2: continue
        m=build(name,d,nz); m.fit(X[idx],z[idx]); P.append(m.predict(Q))
    P=np.stack(P)
    return P.mean(0),np.maximum(P.std(0),1e-9)

def acq(kind,mu,sd,zb,xi=.01):
    if kind=='EI':
        imp=mu-zb-xi; t=imp/sd; return imp*norm.cdf(t)+sd*norm.pdf(t)
    if kind=='UCB':  return mu+2.0*sd
    if kind=='PI':   return norm.cdf((mu-zb-xi)/sd)
    if kind=='TS':
        rng=np.random.default_rng(1); return mu+sd*rng.standard_normal(len(mu))
    raise ValueError

out={}
for k in [f'F{i}' for i in range(1,9)]:
    X,Y=load(k); d=X.shape[1]
    z=rank_gauss(Y) if TRANSFORM[k]=='rank' else standardise(Y)
    nz=NOISE[k]/Y.std() if TRANSFORM[k]=='raw' else .05
    zb=z.max()
    Q=qmc.Sobol(d,scramble=True,seed=3).random(8192)*0.999999
    Q=np.vstack([Q,np.clip(X[np.argmax(Y)]+0.03*np.random.default_rng(2).standard_normal((2048,d)),0,0.999999)])
    tbl={}
    for name in BEST[k]:
        mu,sd=predict(name,build(name,d,nz),X,z,Q,d,nz)
        for a in ('EI','UCB','PI','TS'):
            v=acq(a,mu,sd,zb)
            tbl[f'{name}|{a}']=v
    # consensus: average normalised rank across every model x acquisition pair
    R=np.zeros(len(Q))
    for v in tbl.values():
        r=np.argsort(np.argsort(v))/ (len(v)-1)
        R+=r
    R/=len(tbl)
    j=int(np.argmax(R))
    out[k]={'consensus':Q[j].tolist(),'score':float(R[j]),
            'per_method':{m:Q[int(np.argmax(v))].tolist() for m,v in tbl.items()}}
    print(f"{k} ({d}D) models={BEST[k]}")
    print(f"   consensus: {'-'.join(f'{t:.6f}' for t in Q[j])}  (agreement {R[j]:.3f})")
json.dump(out,open('/tmp/ensemble.json','w'),indent=1)
print('\nwritten')
