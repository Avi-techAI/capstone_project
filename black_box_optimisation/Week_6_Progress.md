# Black Box Capstone: Week 6 Progress

**Cohort:** IMP-PCMLAI-26-06 | **Student:** Avi Thakur
**Course:** Imperial College London Professional Certificate in ML and AI
**Status:** I have chosen my Week 6 inputs but I have not submitted them yet. I will record the outputs in section 8 when the portal replies.

---

## 1. My inputs and outputs so far

I put each week's input next to the output it gave.

| Function | Dim | Week 1 input | Week 1 output | Week 2 input | Week 2 output | Week 3 input | Week 3 output | Week 4 input | Week 4 output | Week 5 input | Week 5 output |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | 2 | `0.731024-0.733000` | 7.71e-16 | `0.747350-0.757252` | 1.62e-23 | `0.715000-0.709000` | 3.84e-10 | `0.697000-0.682000` | 5.66e-06 | `0.680000-0.657000` | -1.55e-03 |
| F2 | 2 | `0.702637-0.926564` | 0.6965 | `0.718372-0.000000` | 0.5388 | `0.698000-0.990000` | 0.5961 | `0.705000-0.560000` | 0.5261 | `0.985000-0.985000` | -0.0028 |
| F3 | 3 | `0.492581-0.611593-0.340176` | -0.0334 | `0.614976-0.699593-0.383667` | -0.0166 | `0.660000-0.730000-0.400000` | -0.0376 | `0.560000-0.660000-0.372000` | -0.0206 | `0.850000-0.700000-0.384000` | -0.0165 |
| F4 | 4 | `0.577766-0.428772-0.425826-0.249007` | -4.0256 | `0.440364-0.425179-0.378308-0.397055` | 0.2626 | `0.410500-0.417300-0.352000-0.434500` | 0.5540 | `0.406800-0.414700-0.344200-0.438700` | 0.3837 | `0.414200-0.419900-0.359800-0.430300` | 0.6473 |
| F5 | 4 | `0.224189-0.846480-0.879484-0.878516` | 1088.86 | `0.203449-0.958957-0.999999-0.960107` | 3452.92 | `0.150000-0.999999-0.999999-0.999999` | 4443.11 | `0.080000-0.999999-0.999999-0.999999` | 4440.81 | `0.300000-0.999999-0.999999-0.999999` | 4473.75 |
| F6 | 5 | `0.728186-0.154693-0.732552-0.693997-0.056401` | -0.6992 | `0.447694-0.000000-0.909797-0.999999-0.000000` | -1.0053 | `0.650000-0.230000-0.650000-0.770000-0.030000` | -0.4242 | `0.585000-0.315000-0.565000-0.830000-0.000000` | -0.4142 | `0.622000-0.282000-0.609000-0.817000-0.000000` | -0.4396 |
| F7 | 6 | `0.057896-0.491672-0.247422-0.218118-0.420428-0.730970` | 1.3650 | `0.000000-0.117995-0.800238-0.320528-0.316723-0.893535` | 1.5281 | `0.000000-0.060000-0.860000-0.360000-0.280000-0.950000` | 1.0610 | `0.000000-0.200000-0.720000-0.310000-0.330000-0.810000` | 2.0818 | `0.000000-0.220000-0.700000-0.275000-0.355000-0.800000` | 2.1092 |
| F8 | 8 | `0.056447-0.065956-0.022929-0.038786-0.403935-0.801055-0.488307-0.893085` | 9.5985 | `0.105641-0.000000-0.134347-0.000000-0.999999-0.471787-0.151664-0.399205` | 9.9254 | `0.125000-0.060000-0.160000-0.000000-0.999999-0.490000-0.200000-0.470000` | 9.9437 | `0.126000-0.080000-0.166000-0.000000-0.999999-0.503000-0.228000-0.532000` | 9.9453 | `0.015000-0.181000-0.113000-0.219000-0.998000-0.790000-0.251000-0.207000` | 9.8546 |

## 2. My best result so far

| Function | Best so far | Week 5 result |
|---|---|---|
| F1 | 5.66e-06 (W4) | Worse, negative |
| F2 | 0.6965 (W1) | Much worse (explore) |
| F3 | -0.0165 (W5) | Better, very small gain |
| F4 | 0.6473 (W5) | Better, up about 17% |
| F5 | 4473.75 (W5) | Better, up about 0.7% |
| F6 | -0.4142 (W4) | Worse |
| F7 | 2.1092 (W5) | Better, small gain |
| F8 | 9.9453 (W4) | Worse (explore) |

Four of eight functions set a new best in Week 5 (F3, F4, F5, F7). The four that did not improve were F1 and F6, plus the two exploration points (F2 and F8).

## 3. What I learned about each function

**F1.** The log curve predicted about 3e-4 at the Week 5 point, but the real output was -1.55e-3. So the curve does not hold past the Week 4 point. This is the second negative value close to this area. The first was -3.6e-3 at 0.650-0.682 in the starting data. Both negative values are much larger in size than any positive value so far. So there is something close to 0.65 to 0.68 that pushes the output below zero. The positive values grow along the line only up to the Week 4 point, and the best point lies on the edge of that negative area. My Week 5 mistake was to fit a curve that can only be positive, so it could never predict the change to a negative value. This week I fitted a curve that can change sign, of the shape (z minus t) times a bell curve, where t is the position along the line. It fits all five points on the line closely. It puts the change from positive to negative at about 0.689-0.670, and the highest positive value just before that, at about 0.692-0.674, where it predicts about 1.7e-5.

**F2.** The corner at 0.985-0.985 gave -0.0028, which is a very poor value. This rules out that corner and confirms that the good area is the narrow ridge near x1 = 0.70. The outputs near x1 = 0.70 range from 0.53 to 0.70 across many x2 values, and the model still gives x2 almost no effect (length scale at the upper limit of 3.0).

**F3.** The one input test worked. Moving x1 from 0.615 to 0.85 gave -0.0165, almost the same as the Week 2 value of -0.0166. The difference is smaller than the noise seen on a repeated point (about 0.0015). So x1 does not matter, and F3 is in practice a 2D problem in x2 and x3. x3 is still the most sensitive input (length scale 0.09).

**F4.** The mirror step worked well. The output rose to 0.6473, a new best. So the drop in Week 4 did not mean the top was at the Week 3 point. It meant Week 4 moved the wrong way. The Week 4, Week 3 and Week 5 points lie on one straight line, and their outputs rise along it (0.384, 0.554, 0.647). A simple curve through these three points has its top about 0.7 of a step past the Week 5 point, where it predicts about 0.667.

**F5.** The one input test also worked. With x2, x3 and x4 on the upper edge, x1 = 0.30 gave 4473.75, higher than x1 = 0.08 (4440.81) and x1 = 0.15 (4443.11). So a higher x1 helps a little. The raw model now gives x1 a length scale of 2.34, so it sees a gentle rise in x1, and it predicts the rise continues up to at least x1 = 0.6.

**F6.** The point between Week 3 and Week 4 gave -0.4396, worse than both. At first this suggests the top is not between them. But the noise check in section 4 shows that F6 is noisy: the same point gave -0.714 and -0.699, a gap of 0.015. The Week 3, Week 4 and Week 5 values (-0.424, -0.414, -0.440) differ by less than two times that gap, so all three points are close to equal, and none of them is clearly the best. This week the raw and rank models agree with each other, and both point in a new direction from the Week 4 best: x1, x2, x3 and x4 down, and x5 a little above 0.

**F7.** A small new best (2.109), very close to the raw model prediction of 2.10. The gains are now small, which suggests F7 is close to its top. Both models agree that x4 should go a little lower and x6 should stay near 0.80.

**F8.** The exploration point gave 9.8546. The model predicted 9.854 for it, so the F8 model is very accurate even far from the best. This tells me there is no better area in that direction. The model's highest prediction anywhere is still close to the current best, so F8 is near its top.

## 4. How I chose the Week 6 inputs

I used the same Gaussian Process setup as Weeks 4 and 5 (ARD Matern 2.5 kernel, length scales bounded to 0.05 to 3.0, white noise term, Expected Improvement). I refitted each model on the initial data plus all five weeks of results. I chose the output transform (raw or rank) again for each function by leave one out Spearman. I produced four candidates for each function: the EI point, a pure exploit point, an EI point inside a box of plus or minus 0.1 around the best input, and an exploit point inside that box. For F3, F6 and F7 I compared the raw and rank models, to see whether they give the same advice. For F4 I fitted a simple curve through the three points on one line. For F1 I fitted a curve along the line that can change sign.

**Noise check.** Each Week 1 input was the best point of the starting data, so every function has one point measured twice. The gap between the two readings shows how noisy each function is: F2 0.085, F6 0.015, F3 0.0014, F5 0.0014 (on outputs above 1000, so very small), F4 0.00001, F7 0.000002, F8 0.0000001, and F1 almost 0. So only F2, F6 and F3 have noise that matters, and for those three a small change in output can be noise. For the other five, every change in output is real.

| Function | Transform | LOO R2 | LOO Spearman | Model trust |
|---|---|---|---|---|
| F1 | raw | 0.25 | 0.39 | Very low |
| F2 | raw | 0.35 | 0.67 | Low to moderate |
| F3 | rank | 0.63 | 0.82 | Moderate |
| F4 | raw | 0.99 | 0.98 | High overall, low near the top |
| F5 | raw* | 0.96 | 0.69 | Moderate |
| F6 | rank | 0.65 | 0.83 | Moderate |
| F7 | rank | 0.56 | 0.75 | Moderate |
| F8 | raw | 0.98 | 0.99 | High |

The model skill chart in `figures/` comes from `visualise_progress.py`, which uses a slightly different rank transform and fixed transform choices, so its scores can differ from this table. The gap is small for the strong models (F4, F5, F8) and can reach about 0.2 for the weak ones such as F1.

*For F5 the rank model wins on Spearman by a very small margin (0.70 against 0.69), but the raw model has far better R2 (0.96 against 0.52) and matches the real results, so I used the raw model, as in Week 5. For F6 the raw and rank models give the same scores this week.

## 5. My Week 6 inputs

| Function | Dim | My input | Style | Confidence |
|---|---|---|---|---|
| F1 | 2 | `0.421000-0.464000` | Explore, largest empty area | Low |
| F2 | 2 | `0.702637-0.926564` | Repeat best point (noise test) | Moderate |
| F3 | 3 | `0.850000-0.700000-0.376000` | Explore one input (x3) | Moderate |
| F4 | 4 | `0.416800-0.421700-0.365300-0.427400` | Exploit along the line | Moderate to high |
| F5 | 4 | `0.500000-0.999999-0.999999-0.999999` | Exploit along trend (x1) | Moderate |
| F6 | 5 | `0.549000-0.272000-0.517000-0.785000-0.047000` | Exploit, both models agree | Moderate |
| F7 | 6 | `0.000000-0.200000-0.680000-0.248000-0.355000-0.802000` | Exploit | Moderate to high |
| F8 | 8 | `0.138700-0.056400-0.170700-0.000000-0.968400-0.499500-0.223600-0.501300` | Exploit | High |

Five functions exploit (F4, F5, F6, F7, F8). One explores a new area (F1). Two test something specific (F2, F3).

### Why I chose each input

**F1 (low, explore).** F1 stands for finding a radiation source, and the course says there are strong and weak sources. After five weeks the best value is still only 5.66e-06, so the source near 0.69-0.68 looks like a weak one, and a few more small steps there can only add a very small amount. Every value far from that area is almost exactly zero, which means the output falls to zero within a short distance of a source. So a strong source could sit in any large gap between the points tried so far, and the data would not show it. This week I use F1 to search for a second source. I do not pick a random point, because a random point can land close to points already tried and teach very little. Instead I take the point inside the square that is farthest from every F1 point tried so far, at 0.421-0.464. Its nearest tried points are all about 0.32 away. A corner such as 0-1 is a little further from the data (0.40), but most of the area around a corner lies outside the square, so a point in the middle covers more new ground. The weak source is not lost: the curve that can change sign still gives a clear next step there (about 0.6935-0.6767, predicted about 1.4e-5), which I can use in a later week.

**F2 (moderate, repeat the best point).** I send the Week 1 best point again, 0.702637-0.926564. This point already has two readings, 0.611 and 0.697. A third reading gives a better idea of the real value at the best point and of the size of the noise. That helps me judge every future F2 result, because right now I cannot tell a real gain from a lucky reading. The Week 5 corner test showed that the area far from x1 = 0.70 is poor, so the best use of this week is to learn more about the ridge itself. The model predicts about 0.61 plus or minus 0.06.

**F3 (moderate, explore one input).** Since x1 does not matter, I keep x1 at 0.85 and x2 at 0.70, and move only x3 from 0.384 down to 0.376. Both the raw and the rank models give this point their best score among the small changes I compared. The raw model predicts about -0.0156, a small gain. The Week 3 point with x3 = 0.40 was much worse, so the top in x3 looks to be at or below 0.384. This test tells me which side of 0.384 is better.

**F4 (moderate to high, exploit along the line).** The curve through the Week 4, Week 3 and Week 5 points has its top at about 1.7 steps from the Week 3 point, where it predicts 0.667. This point is 1.7 steps along that same line, so it moves the same way as the Week 5 step (x1, x2 and x3 up, x4 down) but a little further. The GP predicts only 0.52 here, but last week it predicted 0.47 for a point that really gave 0.647, so near the top I trust the curve through the real results more than the GP.

**F5 (moderate, exploit along trend).** Raising x1 from 0.15 to 0.30 gave a new best, so I raise it again by the same amount, to 0.50, and keep x2, x3 and x4 on the upper edge. The raw model predicts 4541 plus or minus 25, a gain of about 1.5%. I do not go higher than 0.50 in one step, because the model is less sure further out (plus or minus 49 at x1 = 0.6).

**F6 (moderate, exploit).** Last week the two models disagreed and the raw model's choice did not give a gain. This week the raw and rank models agree: their best points inside a box of 0.05 lie only about 0.03 apart. I use the midpoint of those two points. Compared with the Week 4 best, it moves x1 down to 0.549, x2 down to 0.272, x3 down to 0.517 and x4 down to 0.785, and lifts x5 a little to 0.047. The raw model predicts -0.323 plus or minus 0.06. That gain of about 0.09 is about six times the F6 noise, so if it happens, it is a real new best.

**F7 (moderate to high, exploit).** I make a small step from the Week 5 best. The main change is x4 down from 0.275 to 0.248, which both models agree on. x2 goes from 0.22 to 0.20, between what the two models suggest (0.18 and 0.25). I keep x1 at 0, x5 at 0.355 and x6 near 0.80. x3 hardly matters in the rank model (length scale at the upper limit), so its small change to 0.68 is not important. The raw model predicts 2.114 plus or minus 0.011, a small gain over 2.109.

**F8 (high, exploit).** Last week's exploration showed that the model is very accurate, and its highest prediction anywhere is close to the current best. So I go back to a small step from the best point. This is the model's best point inside a box of 0.1, about 0.05 from the best, and it predicts 9.945 plus or minus 0.014. I expect a value very close to the current best. F8 now looks close to finished.

## 6. What I am not sure about

F2 and F3 are noisy, so one output can look better or worse than it really is. The F1 point is a search for a second source, so the most likely result is a value close to zero. The F6 noise means one F6 result cannot show a small gain or loss for certain. The F4 choice rests on a curve through only three points on one line, so it says nothing about other directions. For F5 the model predicts beyond the data it has seen, so the gain may be smaller. The F6 point is in a new direction, so it may not work even though both models agree.

## 7. My next steps

1. I will submit these inputs through the portal and record the outputs in section 8.
2. I will add the Week 6 outputs to `submissions.json` and refit all eight models.
3. For F1, if the output is clearly above zero, a second source lies near 0.421-0.464, so I will search around it next. If it is close to zero, there is no strong source in that gap, so I will go back to the weak source and take the short step of about 0.006 that the curve suggests.
4. For F2, I will use the three readings at the best point to estimate the noise, and I will only call a result better if it beats the average by more than the noise.
5. For F3, I will use the x3 result to decide whether the next step in x3 goes up or down.
6. For F4, if the output rises again, I will fit a new curve and test a second direction.
7. For F5, if the output rises again, I will keep raising x1. If it falls, the best x1 lies between 0.30 and 0.50.

## 8. Week 6 outputs

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
