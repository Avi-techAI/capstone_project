# Black Box Capstone: Week 7 Progress

**Cohort:** IMP-PCMLAI-26-06 | **Student:** Avi Thakur
**Course:** Imperial College London Professional Certificate in ML and AI
**Status:** I have chosen my Week 7 inputs but I have not submitted them yet. I will record the outputs in section 8 when the portal replies.

---

## 1. My inputs and outputs so far

I put each week's input next to the output it gave.

| Function | Dim | Week 1 input | Week 1 output | Week 2 input | Week 2 output | Week 3 input | Week 3 output | Week 4 input | Week 4 output | Week 5 input | Week 5 output | Week 6 input | Week 6 output |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | 2 | `0.731024-0.733000` | 7.71e-16 | `0.747350-0.757252` | 1.62e-23 | `0.715000-0.709000` | 3.84e-10 | `0.697000-0.682000` | 5.66e-06 | `0.680000-0.657000` | -1.55e-03 | `0.421000-0.464000` | -7.21e-03 |
| F2 | 2 | `0.702637-0.926564` | 0.6965 | `0.718372-0.000000` | 0.5388 | `0.698000-0.990000` | 0.5961 | `0.705000-0.560000` | 0.5261 | `0.985000-0.985000` | -0.0028 | `0.702637-0.926564` | 0.6517 |
| F3 | 3 | `0.492581-0.611593-0.340176` | -0.0334 | `0.614976-0.699593-0.383667` | -0.0166 | `0.660000-0.730000-0.400000` | -0.0376 | `0.560000-0.660000-0.372000` | -0.0206 | `0.850000-0.700000-0.384000` | -0.0165 | `0.850000-0.700000-0.376000` | -0.0313 |
| F4 | 4 | `0.577766-0.428772-0.425826-0.249007` | -4.0256 | `0.440364-0.425179-0.378308-0.397055` | 0.2626 | `0.410500-0.417300-0.352000-0.434500` | 0.5540 | `0.406800-0.414700-0.344200-0.438700` | 0.3837 | `0.414200-0.419900-0.359800-0.430300` | 0.6473 | `0.416800-0.421700-0.365300-0.427400` | 0.6716 |
| F5 | 4 | `0.224189-0.846480-0.879484-0.878516` | 1088.86 | `0.203449-0.958957-0.999999-0.960107` | 3452.92 | `0.150000-0.999999-0.999999-0.999999` | 4443.11 | `0.080000-0.999999-0.999999-0.999999` | 4440.81 | `0.300000-0.999999-0.999999-0.999999` | 4473.75 | `0.500000-0.999999-0.999999-0.999999` | 4678.30 |
| F6 | 5 | `0.728186-0.154693-0.732552-0.693997-0.056401` | -0.6992 | `0.447694-0.000000-0.909797-0.999999-0.000000` | -1.0053 | `0.650000-0.230000-0.650000-0.770000-0.030000` | -0.4242 | `0.585000-0.315000-0.565000-0.830000-0.000000` | -0.4142 | `0.622000-0.282000-0.609000-0.817000-0.000000` | -0.4396 | `0.549000-0.272000-0.517000-0.785000-0.047000` | -0.4388 |
| F7 | 6 | `0.057896-0.491672-0.247422-0.218118-0.420428-0.730970` | 1.3650 | `0.000000-0.117995-0.800238-0.320528-0.316723-0.893535` | 1.5281 | `0.000000-0.060000-0.860000-0.360000-0.280000-0.950000` | 1.0610 | `0.000000-0.200000-0.720000-0.310000-0.330000-0.810000` | 2.0818 | `0.000000-0.220000-0.700000-0.275000-0.355000-0.800000` | 2.1092 | `0.000000-0.200000-0.680000-0.248000-0.355000-0.802000` | 2.1315 |
| F8 | 8 | `0.056447-0.065956-0.022929-0.038786-0.403935-0.801055-0.488307-0.893085` | 9.5985 | `0.105641-0.000000-0.134347-0.000000-0.999999-0.471787-0.151664-0.399205` | 9.9254 | `0.125000-0.060000-0.160000-0.000000-0.999999-0.490000-0.200000-0.470000` | 9.9437 | `0.126000-0.080000-0.166000-0.000000-0.999999-0.503000-0.228000-0.532000` | 9.9453 | `0.015000-0.181000-0.113000-0.219000-0.998000-0.790000-0.251000-0.207000` | 9.8546 | `0.138700-0.056400-0.170700-0.000000-0.968400-0.499500-0.223600-0.501300` | 9.9445 |

## 2. My best result so far

| Function | Best so far | Week 6 result |
|---|---|---|
| F1 | 5.66e-06 (W4) | Worse, negative (explore point) |
| F2 | 0.6965 (W1) | Third reading of the best point |
| F3 | -0.0165 (W5) | Worse |
| F4 | 0.6716 (W6) | Better, up about 3.7% |
| F5 | 4678.30 (W6) | Better, up about 4.6% |
| F6 | -0.4142 (W4) | Worse, but inside the noise |
| F7 | 2.1315 (W6) | Better, up about 1.1% |
| F8 | 9.9453 (W4) | Very slightly worse |

Three of eight functions set a new best in Week 6 (F4, F5, F7). F1 and F2 were planned tests, not attempts at a new best. F3, F6 and F8 did not improve.

## 3. What I learned about each function

**F1.** My explore point at 0.421-0.464 gave -7.21e-03. This is the largest negative value so far, about twice the size of the -3.6e-3 in the starting data. So the middle of the square is not empty, and it does not hold a strong positive source. It is a negative area. I now have negative values at three places: 0.650-0.682, 0.680-0.657 and 0.421-0.464. The weak positive source near 0.697-0.682 sits on the edge of this negative area. The explore point did not find a better source, but it ruled out the largest gap in the square, and that was the aim.

**F2.** The best point now has three readings: 0.6112, 0.6965 and 0.6517. Their average is 0.653 and their standard deviation is about 0.043. So the real value at my best point is about 0.65, and the 0.6965 in Week 1 was a lucky high reading. From now on I only call an F2 result better if it beats 0.653 by more than about 0.09, which is two standard deviations. The model still gives x1 a very short length scale (0.065) and x2 the upper limit (3.0), so in practice F2 depends on x1 only.

**F3.** Moving x3 down from 0.384 to 0.376 gave -0.0313, much worse than -0.0165. The raw model predicted -0.0156, so the model was wrong. This drop is real and not noise. Two points with x3 near 0.384 and x2 near 0.70, but with x1 at 0.615 and at 0.85, gave -0.0166 and -0.0165, so results at that spot repeat very closely. The Week 4 point is the key clue. It had x3 = 0.372, lower than this week, but x2 = 0.66, and it gave a much better -0.0206. One explanation fits these points: the best x3 rises when x2 rises. That is a sloped ridge. The two points (0.66, 0.372) and (0.70, 0.384) give a slope of 0.3, but that rests on only two points. So I tested the idea on all 21 F3 points. I turned x3 into "x3 minus slope times x2" and checked how well the model then predicts in leave one out testing. A slope of 0.15 gave the best result (Spearman 0.82 against 0.79 with no slope, and 0.78 with a slope of 0.3). So the data supports a gentle ridge with a slope of about 0.15. My Gaussian Process gives each input its own length scale, so it cannot follow a sloped ridge, and this helps explain why its F3 advice failed.

**F4.** The point at the top of the curve gave 0.6716, a new best. The curve predicted 0.667, so the curve through the real results worked again. A new curve through all four points on the line (Week 4, 3, 5 and 6) fits each of them within 0.0011. Its top lies at 1.79 steps from the Week 3 point and predicts 0.6714, which is no better than the Week 6 point at 1.70 steps. So this line is used up.

**F5.** x1 = 0.50 gave 4678.30, up 4.6%. The raw model predicted only 4541 plus or minus 25, so the real gain was far larger than the model expected. With x2, x3 and x4 on the upper edge, the output rises faster and faster as x1 grows: 4440.81 at 0.08, 4443.11 at 0.15, 4473.75 at 0.30 and 4678.30 at 0.50. A simple curve through these four points predicts about 5150 at x1 = 0.75. The GP gives x1 the upper limit of its length scale (3.0), so it smooths this rise away and predicts only 4698 at 0.75.

**F6.** The new point gave -0.4388. The raw model predicted -0.323, so it was too hopeful for the second week in a row. My four best F6 values are now -0.4142, -0.4242, -0.4388 and -0.4396. They all lie within 0.026 of each other, less than two times the noise of 0.015. So small steps around these points cannot show a gain I can trust. F6 is stuck on a flat top, and it needs a larger step.

**F7.** The small step gave 2.1315, a new best, above the raw model prediction of 2.114. Lowering x4 helped three weeks in a row (0.31, 0.275, 0.248). Both models still point to a lower x4 and a slightly lower x2.

**F8.** The local step gave 9.9445, only 0.0008 below the best. The model predicted 9.945, so it is accurate again. F8 is at or very near its top, and the differences are now about 0.001.

## 4. How I chose the Week 7 inputs

I used the same Gaussian Process setup as Weeks 4 to 6 (ARD Matern 2.5 kernel, length scales bounded to 0.05 to 3.0, white noise term, Expected Improvement). I refitted each model on the initial data plus all six weeks of results. I chose the output transform (raw or rank) again for each function by leave one out Spearman. I produced four candidates for each function: the EI point, a pure exploit point, an EI point inside a box of plus or minus 0.1 around the best input, and an exploit point inside that box. For F3, F6 and F7 I compared the raw and rank models. For F4 I refitted the curve along the line and then used the GP to find the best direction across the line. For F5 I fitted a simple curve through the four points on the corner. For F1 I kept the curve that can change sign.

**A second model type.** After a first draft of these inputs I tested a different strategy: a rougher kernel, Matern 1.5 in place of Matern 2.5. A Matern 2.5 model assumes a smooth surface. A Matern 1.5 model allows sharper bends, which suits narrow tops such as F4. I compared both kernels on every function in leave one out testing, with both raw and rank outputs. Matern 1.5 scored equal or better on Spearman for all eight functions, and the gain is large for F4 (0.99 against 0.93), F6 (0.89 against 0.82 on raw outputs) and F5 (0.89 against 0.85). For F8 both kernels score 0.99. Matern 1.5 also fits the F4 top: at the best point it predicts 0.6716, the real value, while Matern 2.5 predicts only 0.565. So for each function I now use the kernel and transform with the best leave one out Spearman, and I checked every Week 7 point under both kernels. Together with the ridge test in section 3, this changed three points (F3, F6 and F8) and gave stronger support to three others (F4, F5 and F7).

This week I also checked each function for a repeated mistake. Three times now a model was too hopeful near the top (F3 and F6 this week, F1 in Week 5). Where a model has failed in this way, I gave more weight to the trend in the real results, or I chose a test that can show whether the model is wrong.

**Noise check.** Each Week 1 input was the best point of the starting data, so every function has one point measured twice, and F2 now has a third reading. The gap between readings shows how noisy each function is: F2 about 0.043 (standard deviation of three readings), F6 0.015, F3 0.0014, F5 0.0014 (on outputs above 1000, so very small), F4 0.00001, F7 0.000002, F8 0.0000001, and F1 almost 0.

| Function | Spearman, Matern 2.5 | Spearman, Matern 1.5 | Model used | Model trust |
|---|---|---|---|---|
| F1 | 0.41 (raw) | 0.46 (raw) | raw, Matern 1.5 | Very low |
| F2 | 0.72 (rank) | 0.72 (raw and rank) | raw, Matern 1.5 | Low to moderate |
| F3 | 0.79 (rank) | 0.79 (rank) | rank, both kernels | Moderate, but it cannot see the ridge |
| F4 | 0.93 (raw) | 0.99 (raw) | raw, Matern 1.5 | High |
| F5 | 0.85 (raw) | 0.89 (raw) | raw, Matern 1.5 | High |
| F6 | 0.85 (rank) | 0.89 (raw) | raw, Matern 1.5 | Moderate |
| F7 | 0.78 (rank) | 0.80 (rank) | rank, Matern 1.5 | Moderate |
| F8 | 0.99 (raw) | 0.99 (raw) | raw, Matern 2.5 | High |

For F2 the raw and rank scores tie, so I used the raw model, which has the better R2 (0.44 against 0.38). For F8 the two kernels tie at 0.99, so I kept Matern 2.5, which has the better R2 (0.98 against 0.97).

The model skill chart in `figures/` comes from `visualise_progress.py`, which uses a slightly different rank transform and fixed transform choices, so its scores can differ from this table. The gap is small for the strong models (F4, F5, F8) and larger for the weak ones such as F1.

## 5. My Week 7 inputs

| Function | Dim | My input | Style | Confidence |
|---|---|---|---|---|
| F1 | 2 | `0.693500-0.676700` | Exploit, short step along the line | Low to moderate |
| F2 | 2 | `0.240000-0.926564` | Explore one input (x1) | Low |
| F3 | 3 | `0.850000-0.715000-0.386250` | Test the sloped ridge | Low to moderate |
| F4 | 4 | `0.413800-0.421900-0.368100-0.430100` | Test a second direction | Moderate |
| F5 | 4 | `0.750000-0.999999-0.999999-0.999999` | Exploit along trend (x1) | Moderate to high |
| F6 | 5 | `0.590000-0.290000-0.651000-0.734000-0.000000` | Exploit, medium step with the best model | Moderate |
| F7 | 6 | `0.000000-0.170000-0.640000-0.200000-0.355000-0.806000` | Exploit, both models agree | High |
| F8 | 8 | `0.139900-0.076100-0.167900-0.009900-0.999999-0.504000-0.217800-0.520900` | Exploit, all models agree | High |

Five functions exploit (F1, F5, F6, F7, F8). One explores (F2). Two test an idea about the shape of the function (F3, F4).

### Why I chose each input

**F1 (low to moderate, exploit).** The Week 6 explore point showed that the middle of the square is a negative area, so I go back to the weak source and take the short step I saved last week. It is a step of about 0.006 from the Week 4 best along the same line, to 0.6935-0.6767. The curve that can change sign predicts about 1.4e-5 here, about 2.5 times the current best. It stays short of the point where the curve turns negative (about 0.689-0.670). The GP cannot see changes of size 1e-5 on F1, so I do not use its prediction here.

**F2 (low, explore one input).** At the best point the real value is about 0.65, and one more reading near it cannot show a gain larger than the noise. So the best use of this week is to look for a second peak. F2 depends on x1 only, so I list the x1 values tried so far, rounded to two places: 0.14, 0.34, 0.44, 0.46, 0.58, 0.67, 0.70, 0.72, 0.85, 0.88 and 0.99. The largest gap lies between 0.14 and 0.34. It is 0.20 wide, about three times the x1 length scale of 0.065, so a narrow peak could sit in it and the data would not show it. I take its middle, x1 = 0.24, and keep x2 at the best point (0.926564), so only one input changes. Both models expect a low value here (raw 0.13 plus or minus 0.24), but with very wide doubt.

**F3 (low to moderate, test the sloped ridge).** With the slope of 0.15 that the data supports, the best x3 for x2 = 0.715 is about 0.384 + 0.15 x 0.015 = 0.38625. So I raise x2 a little, from 0.70 to 0.715, and x3 along with it, to 0.38625. I keep x1 at 0.85 because x1 does not matter. The models disagree here. The raw Matern 1.5 model predicts -0.0158 plus or minus 0.003, a small gain, while the rank models predict a small loss. A result better than -0.0165 would show that the ridge is real and which way along it the output rises. The step is small (0.015 from the best point), so a loss would also be small. My first draft used the two point slope of 0.3 (x3 = 0.3885), which the wider test did not support.

**F4 (moderate, test a second direction).** The line is used up, so I step across it. I took the GP slope at the best point and removed the part along the line. What remains points mainly to x1 down and x3 and x4 up. I move 0.005 in that direction, about half the length of one step on the line, to keep the risk small. On the line, a step of this size away from the top costs about 0.01, so even if this direction gives no gain the loss is small. The GP predicts 0.586 here against 0.565 at the best point, a rise of about 0.02, but the Matern 2.5 GP is about 0.1 too low near the top. The Matern 1.5 model, which fits the top, predicts 0.719 plus or minus 0.03 here, a gain of about 7%, and gives a 94% chance of beating the best. So both kernels agree on the direction, and the better one expects a clear gain.

**F5 (moderate to high, exploit along trend).** The rise in x1 grows faster each step, so I take a larger step, from 0.50 to 0.75, and keep x2, x3 and x4 on the upper edge. The curve through the four corner points predicts about 5150. The Matern 1.5 model predicts 4866 plus or minus 130, and the Matern 2.5 model 4698 plus or minus 99. All three are above the current best. I stop at 0.75 rather than 1.0 so that, if the output falls, I know the top lies between 0.50 and 0.75.

**F6 (moderate, exploit with a medium step).** Small steps cannot show a gain on F6, because my four best values lie within the noise, so I need a larger step. My first draft was an explore point that moved x4 down to 0.62. When I checked it under Matern 2.5, Matern 1.5 and a smooth RBF kernel, every model expected that point to fall below the best. So I replaced it with the Matern 1.5 model's best point inside a box of 0.1. It moves x4 down from 0.83 to 0.734 and x3 up from 0.565 to 0.651, sets x2 to 0.29 and x5 to 0, and keeps x1 near 0.59. It is about 0.13 from the best point, so it is still a real step and not a small change. The Matern 1.5 model predicts -0.379 plus or minus 0.063, a gain of about 0.035, which is more than two times the noise, and gives a 71% chance of beating the best. The raw Matern 2.5 model also predicts a small gain (-0.411).

**F7 (high, exploit).** I continue the trend that worked three weeks in a row. Both kernels agree on this point. x4 goes down from 0.248 to 0.20, and x2 from 0.20 to 0.17, which lies between the two model choices (0.154 and 0.189). x3 hardly matters in either model (length scale 3.0 in the raw model and 2.58 in the rank model), so its change to 0.64 is not important. I keep x1 at 0 and x5 at 0.355, and set x6 to 0.806. The raw model predicts 2.161 plus or minus 0.005, a gain of about 0.03, and the raw Matern 1.5 model predicts 2.159.

**F8 (high, exploit).** F8 is near its top, and the Week 5 explore point already showed that the model is accurate far from the best, so a second explore point would only repeat that lesson. My first draft was the Matern 2.5 model's best point inside a box of 0.1, but the Matern 1.5 model predicts a small loss there (9.938). So I searched inside a box of 0.05 for the point where the lowest of three model predictions (Matern 2.5, Matern 1.5 and a smooth RBF kernel) is highest. That point is only 0.023 from the best, and all three models predict 9.9453 or 9.9454 there. I expect a value within about 0.001 of the best. F8 is close to finished, and the real gains left are about 0.001.

## 6. What I am not sure about

The F3 ridge slope of 0.15 comes from a small gain in one test score, so the ridge may not be real. The F4 direction comes from the GP slope at one point, so it may be wrong even though both kernels agree. The F5 curve predicts beyond the data, so the real value at 0.75 may be lower, or the top may lie between 0.50 and 0.75. The F2 point is an explore point, so a poor result is likely and still useful. The F6 gain is only about two times the noise, so one reading may not show it clearly. The F1 curve has four settings fitted to five points, so it can fit well and still be wrong between them.

## 7. My next steps

1. I will submit these inputs through the portal and record the outputs in section 8.
2. I will add the Week 7 outputs to `submissions.json` and refit all eight models.
3. For F1, if the output is positive and higher, I will refit the curve. If it is negative, the top of the weak source lies between the Week 4 point and this one.
4. For F2, if the output is above 0.653 by more than 0.09, I will search around x1 = 0.24. If not, I will go back to x1 near 0.70.
5. For F3, if the output beats -0.0165, I will take a second step along the ridge. If not, I will go back to the best point and test x2 alone.
6. For F4, if the output rises, I will take a second step in the same direction. If it falls, I will try the opposite direction.
7. For F5, if the output rises again, I will try x1 = 0.999999. If it falls, the top lies between 0.50 and 0.75.
8. For F6, if the output beats -0.4142 by more than the noise, I will take a second step in the same direction. If not, I will treat F6 as finished near -0.41.
9. For every function, I will compare the Matern 1.5 and Matern 2.5 predictions with the real Week 7 outputs, to check that the switch of kernel was right.

## 8. Week 7 outputs

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
