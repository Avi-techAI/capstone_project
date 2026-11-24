# Black Box Capstone: Week 8 Progress

**Cohort:** IMP-PCMLAI-26-06 | **Student:** Avi Thakur
**Course:** Imperial College London Professional Certificate in ML and AI
**Status:** I have chosen my Week 8 inputs but I have not submitted them yet. I will record the outputs in section 8 when the portal replies.

---

## 1. My Week 7 results

| Function | Dim | Week 7 input | Week 7 output | Best before | New best? |
|---|---|---|---|---|---|
| F1 | 2 | `0.693500-0.676700` | 1.70e-05 | 5.66e-06 (W4) | Yes |
| F2 | 2 | `0.240000-0.926564` | -0.0086 | 0.6965 (W1) | No |
| F3 | 3 | `0.850000-0.715000-0.386250` | -0.0221 | -0.0165 (W5) | No |
| F4 | 4 | `0.413800-0.421900-0.368100-0.430100` | 0.6310 | 0.6716 (W6) | No |
| F5 | 4 | `0.750000-0.999999-0.999999-0.999999` | 5652.15 | 4678.30 (W6) | Yes, up 20.8% |
| F6 | 5 | `0.590000-0.290000-0.651000-0.734000-0.000000` | -0.4233 | -0.4142 (W4) | No |
| F7 | 6 | `0.000000-0.170000-0.640000-0.200000-0.355000-0.806000` | 2.1010 | 2.1315 (W6) | No |
| F8 | 8 | `0.139900-0.076100-0.167900-0.009900-0.999999-0.504000-0.217800-0.520900` | 9.94614 | 9.94532 (W4) | Yes, by 0.0008 |

## 2. My best result so far

| Function | Best so far | Week found | Starting data |
|---|---|---|---|
| F1 | 1.70e-05 | 7 | 7.71e-16 |
| F2 | 0.6965 | 1 | 0.6112 |
| F3 | -0.0165 | 5 | -0.0348 |
| F4 | 0.6716 | 6 | -4.0255 |
| F5 | 5652.15 | 7 | 1088.86 |
| F6 | -0.4142 | 4 | -0.7143 |
| F7 | 2.1315 | 6 | 1.3650 |
| F8 | 9.94614 | 7 | 9.5985 |

Three of eight improved. F5 went up 20.8% and F1 tripled. F8 moved by 0.0008, which counts as a new best but does not mean much.

## 3. What I learned about each function

**F1.** The short step worked. The output went from 5.66e-06 to 1.70e-05, and my sign changing curve had predicted 1.4e-05, so it was close. I then sorted every F1 point by x1 plus x2. All five of the biggest positive outputs sit above 1.370 and all three of the biggest negative ones sit below 1.337. So there is one line where the sign flips, at about 1.3698. Last week I thought the sign might flip back and forth in bands, and that was wrong. The output also drops very fast once you pass that line, by about 139 times for every 0.01.

**F2.** The explore point at x1 of 0.24 gave -0.0086. So there is no hidden peak in the gap between 0.14 and 0.34, and that gap is now closed. F2 is still about 0.65 near x1 of 0.70, with noise of 0.043.

**F3.** I raised x2 to 0.715 and x3 to 0.38625 and got -0.0221, worse than -0.0165. But I changed two inputs at once, so I cannot say which one caused it. That was a mistake in how I set the test up.

**F4.** The step across the line gave 0.6310, below the 0.6716 best, so that direction was wrong. My five best F4 points are now within 0.024 of each other on every input.

**F5.** Raising x1 from 0.50 to 0.75 gave 5652.15. My curve had predicted 5150, so the real gain was even bigger. With the other three inputs on the upper edge the numbers are 4441 at x1 of 0.08, 4443 at 0.15, 4474 at 0.30, 4678 at 0.50 and 5652 at 0.75. Each step gives more than the one before.

**F6.** The medium step gave -0.4233. My five best F6 values are now between -0.4142 and -0.4396. That spread is 0.025, less than two times the noise of 0.015, so this area is flat and small steps inside it will not show me anything.

**F7.** The step gave 2.1010, below the best. Looking at my four best weeks one input at a time, x3 gives 2.082 at 0.72, 2.109 at 0.70, 2.132 at 0.68 and 2.101 at 0.64, so the top is near 0.68. For x4 the top is near 0.248 and for x2 near 0.20. Those three values are all the Week 6 point, so one input at a time says Week 6 is already the top.

**F8.** 9.94614 is a new best but only by 0.0008. The weekly gains are about 0.001 now.

## 4. How I chose the Week 8 inputs

I changed two things this week.

**I tried other kinds of model.** So far I have only used a Gaussian Process. The Module 12 video on surrogate models also mentions regression trees, neural networks and splines, so I tested ten kinds of model on each function: three Gaussian Process kernels (Matern, RBF, Rational Quadratic), Random Forest, Extra Trees, Gradient Boosting, Support Vector Regression, nearest neighbours, a neural network, and polynomial regression with ridge.

The Gaussian Process with a Matern kernel, which I have used for seven weeks, was not the best model on any of the eight.

| Function | GP Matern | Best model | Its score |
|---|---|---|---|
| F1 | 0.47 | Extra Trees | 0.54 |
| F2 | 0.73 | Extra Trees | 0.82 |
| F3 | 0.80 | GP RBF | 0.81 |
| F4 | 0.97 | GP Rational Quadratic | 0.98 |
| F5 | 0.76 | Extra Trees | 0.83 |
| F6 | 0.88 | Support Vector Regression | 0.95 |
| F7 | 0.76 | Support Vector Regression | 0.88 |
| F8 | 0.99 | Polynomial with ridge | 1.00 |

**Then I found my model testing was wrong.** Leave one out testing takes out one point, fits on all the others and predicts the one it took out. But my points arrive week by week, so "all the others" includes later weeks. The model gets to see the future when it predicts the past. Every score I have quoted since Week 1 is too high because of this.

So I ran it the way the real task works. For each week I trained only on the starting data and the weeks before it, then predicted that week.

| Model | Honest test | Leave one out |
|---|---|---|
| Random Forest | 0.22 | 0.71 |
| Extra Trees | 0.16 | 0.80 |
| Nearest neighbours | 0.11 | 0.72 |
| GP Rational Quadratic | -0.03 | 0.74 |
| Gradient Boosting | -0.03 | 0.73 |
| Support Vector Regression | -0.06 | 0.75 |
| GP Matern | -0.16 | 0.82 |
| GP RBF | -0.22 | 0.82 |
| Polynomial with ridge | -0.39 | 0.60 |

Every model dropped, and most came out worse than guessing. Polynomial with ridge scored 1.00 on F8 in the first table and is bottom of this one. That is the model I had used to pick my F8 point.

Per function it is more mixed, which is more useful.

| Function | GP Matern | Random Forest | Extra Trees | Usable? |
|---|---|---|---|---|
| F1 | 0.60 | 0.54 | 0.77 | Yes |
| F2 | 0.83 | 0.94 | 1.00 | Yes, the best of the eight |
| F3 | -0.43 | -0.54 | -0.60 | No |
| F4 | -0.66 | 0.89 | 0.14 | Random Forest only |
| F5 | -0.83 | -0.77 | -0.71 | No |
| F6 | -0.43 | -0.77 | -0.37 | No |
| F7 | 0.03 | 0.89 | 0.60 | Random Forest only |
| F8 | -0.37 | 0.60 | 0.43 | Random Forest only |

On F3, F5 and F6 every model ranks the weeks backwards. F5 is the worst at -0.71 to -0.83.

**What I did about it.** I stopped using one method for all eight. Where a model passes the honest test I use it. Where none passes I run a test that changes one input at a time, or I pick a point far from everything if there is nothing to refine. Where the raw numbers show a trend I follow the trend.

**Two things I threw out.** Tree models cannot predict above the highest value they were trained on. On F5, where the output keeps climbing, a tree can never tell me to go further, and Extra Trees was the top scoring model for F5 on my first test. The second thing is my agreement score. When several models all head for the same empty area it reads 1.000, which looks like they agree but only means they share the same blind spot. My rebuilt F7 point scored 1.000 while suggesting x3 of 0.729, which I have already measured as worse than 0.68.

## 5. My Week 8 inputs

| Function | Dim | My input | How I chose it | Confidence |
|---|---|---|---|---|
| F1 | 2 | `0.694334-0.677534` | Curve fitted to the raw numbers | Low to moderate |
| F2 | 2 | `0.681927-0.903578` | Models, which work best here | Low |
| F3 | 3 | `0.850000-0.700000-0.392000` | One input test | Moderate |
| F4 | 4 | `0.419463-0.366077-0.362835-0.424274` | Random Forest, predicted value only | Moderate |
| F5 | 4 | `0.999999-0.999999-0.999999-0.999999` | Trend in the raw numbers | High |
| F6 | 5 | `0.018002-0.003128-0.015123-0.024853-0.043382` | Point furthest from everything tried | Low |
| F7 | 6 | `0.000000-0.200000-0.680000-0.248000-0.500000-0.802000` | One input test | Moderate |
| F8 | 8 | `0.120505-0.004041-0.160075-0.000000-0.999999-0.533357-0.199373-0.515334` | Random Forest, predicted value only | Moderate |

I checked that all eight differ from points I have already sent, so none of them repeats an answer I have.

### Why I chose each input

**F1 (low to moderate).** The models wanted x1 plus x2 of 1.3868. My own numbers say no, because the output falls as x1 plus x2 grows past 1.3702: 1.70e-05, then 5.66e-06, then 3.84e-10. So I fitted a small curve to the two positive points closest to the sign line. It puts the top at 1.37187, which is what I chose. It sits between two points I know are positive, so it cannot come back negative. I should say the curve has three settings fitted to two points and it does not match my Week 5 number, so the 2.5 times gain is the most I could get, not what I expect.

**F2 (low).** This is the one function where the models do well on the honest test, 0.83 to 1.00, so I used them. I only used the ones that can predict above their training values, because a tree cannot suggest an improvement. The point sits at x1 of 0.682, inside the good area. I still do not expect much from F2 because the noise of 0.043 is about the size of the gains I am chasing.

**F3 (moderate).** Models score -0.43 to -0.60 here so I left them out. Last week I moved x2 and x3 together and learned nothing. This time I hold x1 at 0.85 and x2 at 0.700, which are their best values, and move x3 on its own from 0.384 to 0.392. I already know 0.376 is worse, so this checks the other side.

**F4 (moderate).** Random Forest is the only model that passes here, 0.89 against -0.66 for the Gaussian Process. I used its predicted value and not its uncertainty, because the predicted value is the part that works. Its uncertainty version wanted x3 of 0.21, which is far outside anything that has ever worked, so it was just heading for an empty area. My five best points are within 0.024 of each other, so this is a small step outside a cluster that has stopped moving.

**F5 (high).** Every model scores -0.71 to -0.83 here so I ignored them and followed the numbers. With the other three on the upper edge the output climbs faster each step: 4441, 4443, 4474, 4678, 5652. So I take x1 to the upper edge too.

**F6 (low).** Models score -0.37 to -0.77, and the area is flat as well, five weeks between -0.4142 and -0.4396. So I have no model and no trend. I picked the point furthest from everything I have tried, 0.919 away from the nearest one. I expect a bad number. A bad number still tells me that area is empty.

**F7 (moderate).** I threw out both model suggestions. One wanted x3 of 0.729, which I have measured as worse than 0.68, and x5 of 0.55 when every good run is near 0.355. Changing one input at a time says x2, x3, x4 and x6 are already at their best, and those are the Week 6 point, so there is nothing left to refine there. x5 has barely moved near the top, only 0.038 across my five best runs. So I hold everything at Week 6 and move x5 on its own from 0.355 to 0.500.

**F8 (moderate).** Random Forest is the one that passes here, 0.60. Polynomial with ridge scored 1.00 on the first test and is bottom on the honest one, so I stopped using it. Predicted value only again. The point keeps x5 at 0.999999, which all four of my best F8 runs have.

## 6. What I am not sure about

The F1 curve fits two points with three settings and does not match Week 5, so it can fit those points and still be wrong in between. The honest test only has six weeks per function, so the scores in section 4 are shaky themselves, and 0.60 against 0.43 is not much of a gap on that little data. The functions where the test fails are also the ones where my weekly outputs differ least, so some of those low scores may be about the test being hard rather than the model being bad. F6 is a guess. The F5 step goes past anything I have measured, so the output could fall, and if it does the top is between 0.75 and the edge.

## 7. My next steps

1. I will submit these and record the outputs in section 8.
2. I will add the Week 8 outputs to `submissions.json` and run the honest test again with seven weeks instead of six.
3. For F1, if the output beats 1.70e-05 I will refit the curve and take another short step. If it falls, the top is nearer the sign line than my curve says.
4. For F3 I will learn something either way, because only x3 moved.
5. For F5, if it rises again then F5 is done at the corner and I will put the remaining weeks elsewhere. If it falls, the top is between 0.75 and the edge.
6. For F6, if the far point is bad I will stop spending weeks on F6 and leave it near -0.41.
7. For F7, if x5 helps I will keep moving it. If not, Week 6 was the top.
8. I will check each Week 8 prediction against the real output and keep a record of which models got it right, so the honest test gets better each week.

## 8. Week 8 outputs

| Function | Output received | Better than best so far? | New best |
|---|---|---|---|
| F1 | | | |
| F2 | | | |
| F3 | | | |
| F4 | | | |
| F5 | | | |
| F6 | | | |
| F7 | | | |
| F8 | | | |
