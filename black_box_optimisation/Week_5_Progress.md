# Black Box Capstone: Week 5 Progress

**Cohort:** IMP-PCMLAI-26-06 | **Student:** Avi Thakur
**Course:** Imperial College London Professional Certificate in ML and AI
**Status of this file:** Week 5 inputs are proposed only. They have not been submitted yet. Fill in the outputs table after the portal replies.

---

## 1. What was submitted so far

| Function | Dim | Week 1 input | Week 2 input | Week 3 input | Week 4 input |
|---|---|---|---|---|---|
| F1 | 2 | `0.731024-0.733000` | `0.747350-0.757252` | `0.715000-0.709000` | `0.697000-0.682000` |
| F2 | 2 | `0.702637-0.926564` | `0.718372-0.000000` | `0.698000-0.990000` | `0.705000-0.560000` |
| F3 | 3 | `0.492581-0.611593-0.340176` | `0.614976-0.699593-0.383667` | `0.660000-0.730000-0.400000` | `0.560000-0.660000-0.372000` |
| F4 | 4 | `0.577766-0.428772-0.425826-0.249007` | `0.440364-0.425179-0.378308-0.397055` | `0.410500-0.417300-0.352000-0.434500` | `0.406800-0.414700-0.344200-0.438700` |
| F5 | 4 | `0.224189-0.846480-0.879484-0.878516` | `0.203449-0.958957-0.999999-0.960107` | `0.150000-0.999999-0.999999-0.999999` | `0.080000-0.999999-0.999999-0.999999` |
| F6 | 5 | `0.728186-0.154693-0.732552-0.693997-0.056401` | `0.447694-0.000000-0.909797-0.999999-0.000000` | `0.650000-0.230000-0.650000-0.770000-0.030000` | `0.585000-0.315000-0.565000-0.830000-0.000000` |
| F7 | 6 | `0.057896-0.491672-0.247422-0.218118-0.420428-0.730970` | `0.000000-0.117995-0.800238-0.320528-0.316723-0.893535` | `0.000000-0.060000-0.860000-0.360000-0.280000-0.950000` | `0.000000-0.200000-0.720000-0.310000-0.330000-0.810000` |
| F8 | 8 | `0.056447-0.065956-0.022929-0.038786-0.403935-0.801055-0.488307-0.893085` | `0.105641-0.000000-0.134347-0.000000-0.999999-0.471787-0.151664-0.399205` | `0.125000-0.060000-0.160000-0.000000-0.999999-0.490000-0.200000-0.470000` | `0.126000-0.080000-0.166000-0.000000-0.999999-0.503000-0.228000-0.532000` |

## 2. Outputs received

| Function | Week 1 | Week 2 | Week 3 | Week 4 | Best so far | Week 4 result |
|---|---|---|---|---|---|---|
| F1 | 7.71e-16 | 1.62e-23 | 3.84e-10 | 5.66e-06 | 5.66e-06 (W4) | Better, about 15,000 times higher |
| F2 | 0.6965 | 0.5388 | 0.5961 | 0.5261 | 0.6965 (W1) | Worse, but F2 is noisy |
| F3 | -0.0334 | -0.0166 | -0.0376 | -0.0206 | -0.0166 (W2) | Worse, but closer than Week 3 |
| F4 | -4.0256 | 0.2626 | 0.5540 | 0.3837 | 0.5540 (W3) | Worse by 0.17 |
| F5 | 1088.86 | 3452.92 | 4443.11 | 4440.81 | 4443.11 (W3) | Same as best (0.05% lower) |
| F6 | -0.6992 | -1.0053 | -0.4242 | -0.4142 | -0.4142 (W4) | Better, small gain |
| F7 | 1.3650 | 1.5281 | 1.0610 | 2.0818 | 2.0818 (W4) | Better, up about 36% |
| F8 | 9.5985 | 9.9254 | 9.9437 | 9.9453 | 9.9453 (W4) | Better, very small gain |

Four of eight functions set a new best in Week 4 (F1, F6, F7, F8). F5 matched its best. F2, F3 and F4 did not improve.

## 3. What the data shows for each function

**F1.** The log curve from last week worked well. It predicted about 1e-6 at the Week 4 point and the real value was 5.7e-6. All four points on the line (Week 2, Week 1, Week 3, Week 4) now sit almost exactly on one curve in log scale. That curve has its top about one more step along the same line, near 0.674-0.648, where it predicts about 4e-4.

**F2.** The Week 4 test answered last week's question. With x1 at 0.705, x2 = 0.56 gave 0.526. Across x2 = 0, 0.12, 0.56, 0.93 and 0.99, all outputs near x1 = 0.70 sit between 0.53 and 0.70. One repeated point alone gave 0.61 and 0.70, so a large part of this spread may be noise, and there is no clear pattern in x2. So x2 hardly matters along this ridge. Four weeks of points near x1 = 0.70 now mostly tell me about the noise, not about the peak. The area with x1 above 0.9 has never been tested.

**F3.** Week 4 was better than Week 3 but still below the Week 2 best. So the best area is very close to the Week 2 point, and moving x2 down to 0.66 or x3 away from 0.384 makes things slightly worse. The model still says x1 has almost no effect (length scale at the upper limit of 3.0), while x3 is the most sensitive input (length scale 0.09).

**F4.** This was a surprise. The Week 4 point was only 0.01 away from the Week 3 point, and the model predicted a small gain, but the output fell from 0.554 to 0.384. F4 has almost no noise (the repeated Week 1 point gave -4.02554 and -4.02556, a difference of only 0.00001), so this drop is real. The top of F4 is very narrow, and a small move that mainly lowered x3 went past it. The GP smooths over this and now predicts about 0.47 even at the Week 3 point, so its trust near the top is lower than its overall score suggests.

**F5.** Lowering x1 from 0.15 to 0.08 gave almost the same value (4440.8 against 4443.1). The raw output model now gives x1 a length scale at the upper limit, so x1 barely matters here. Looking back, the big gains from Week 1 to Week 3 came from moving x2, x3 and x4 to the upper edge, not from lowering x1. F5 looks close to its peak at that corner.

**F6.** A small gain (-0.4242 to -0.4142), much less than the model predicted (-0.32). Week 3 and Week 4 now give almost the same value. This suggests the top lies between those two points, not further along the line. The raw output model agrees with this. The rank model mostly wants to continue the line, so the two models disagree this week.

**F7.** A big gain, from 1.528 to 2.082. Stepping back from the Week 3 overshoot and moving the way the candidates agreed worked well. The raw and rank models now give local best points only about 0.07 apart, and both suggest a small step: x4 down a little, x5 up a little, x6 near 0.80.

**F8.** Another very small gain (9.944 to 9.945). The local exploit point now predicts no gain at all (9.945 plus or minus 0.015). The safe gains near this point are used up.

## 4. Method used for Week 5

Same Gaussian Process setup as Week 4 (ARD Matern 2.5 kernel, length scales bounded to 0.05 to 3.0, white noise term, Expected Improvement). Each model was refitted on the initial data plus all four weeks of results, with repeated points kept as separate rows. The output transform (raw or rank) was chosen again for each function by leave one out Spearman. I produced four candidates for each function: the EI point, a pure exploit point, an EI point inside a box of plus or minus 0.1 around the best input, and an exploit point inside that box. For F6 and F7 I also compared the raw and rank models, to see whether the two transforms give the same advice. For F1 I refitted the curve on the log output along the line through all four F1 points.

This week I also asked a new question for each function: is a fifth point near the best still the most useful thing to learn? For three functions (F2, F3, F5) the answer was no, so I used a controlled test of one input, or a jump to an unexplored area. For F8 I took the exploration step that I set aside last week.

| Function | Transform | LOO R2 | LOO Spearman | Model trust |
|---|---|---|---|---|
| F1 | rank | -0.14 | 0.36 | Very low (the log curve is used instead) |
| F2 | raw | 0.45 | 0.72 | Low to moderate |
| F3 | rank | 0.64 | 0.79 | Moderate |
| F4 | raw | 0.98 | 0.99 | High overall, low near the top |
| F5 | raw* | 0.95 | 0.64 | Moderate |
| F6 | rank | 0.61 | 0.84 | Moderate |
| F7 | rank | 0.49 | 0.68 | Moderate |
| F8 | raw | 0.98 | 0.99 | High |

The model skill chart in `figures/` comes from `visualise_progress.py`, which uses a slightly different rank transform, so its scores can differ from this table by a few hundredths.

*For F5 the rank model wins on Spearman by a small margin (0.67 against 0.64), but the raw model has far better R2 (0.95 against 0.43) and matches the real results, so I used the raw model.

## 5. Week 5 proposed inputs

| Function | Dim | Input to submit | Style | Confidence |
|---|---|---|---|---|
| F1 | 2 | `0.680000-0.657000` | Exploit along trend | Moderate |
| F2 | 2 | `0.985000-0.985000` | Explore | Low |
| F3 | 3 | `0.850000-0.700000-0.384000` | Explore one input (x1) | Moderate |
| F4 | 4 | `0.414200-0.419900-0.359800-0.430300` | Exploit, small mirror step | Low to moderate |
| F5 | 4 | `0.300000-0.999999-0.999999-0.999999` | Explore one input (x1) | Moderate |
| F6 | 5 | `0.622000-0.282000-0.609000-0.817000-0.000000` | Exploit, step back between two best | Moderate |
| F7 | 6 | `0.000000-0.220000-0.700000-0.275000-0.355000-0.800000` | Exploit | Moderate to high |
| F8 | 8 | `0.015000-0.181000-0.113000-0.219000-0.998000-0.790000-0.251000-0.207000` | Explore (EI) | Moderate |

Four functions exploit (F1, F4, F6, F7) and four explore (F2, F3, F5, F8).

### Reasoning for each function

**F1 (moderate, exploit).** The log curve through the four F1 points predicts about 3e-4 at 0.680-0.657, which is about one more step along the same line and would be more than 50 times the current best. I stop a little short of the curve's top (0.674-0.648), because the negative point at 0.650-0.682 is now only about 0.04 away and I still do not know what causes it. If the output rises again, the source is close and I will search around it. If it falls, the top is most likely between the Week 4 point and this one.

**F2 (low, explore).** Since x2 hardly matters near x1 = 0.70, and the noise is about the same size as the differences there, another point on this ridge would add little. The GP EI and the upper confidence bound both choose the unexplored corner near 0.985-0.985. The model predicts about 0.39 plus or minus 0.24, so the result could be anywhere from poor to a new best. F2 has local optima, so testing a new area now is better than finding out in Week 12. The Week 1 best stays safe whatever this point returns.

**F3 (moderate, explore one input).** I keep x2 and x3 at the Week 2 best (0.70 and 0.384) and only move x1 from 0.615 to 0.85. The model says x1 has almost no effect, so this is a low cost test of that claim. If the output is close to -0.017, x1 truly does not matter and F3 becomes a 2D problem in x2 and x3. If it is clearly better or worse, I learn the direction for x1. The raw model predicts about -0.016 here, so a small gain is possible too.

**F4 (low to moderate, exploit).** The Week 4 move from the Week 3 point lowered the output by 0.17. I now take the same small step the other way from the Week 3 point (mainly x3 up and x4 down). With three points on one line I can fit a simple curve and find where the narrow top lies along that line. The GP local exploit point also moves x3 up, so this direction agrees with the model. The GP predicts only 0.47 here, but it predicts the same at the Week 3 point, which really gave 0.554, so I expect a value close to 0.55 with a fair chance of a small gain.

**F5 (moderate, explore one input).** I keep x2, x3 and x4 at the upper edge and raise x1 to 0.30. Both recent results (x1 = 0.08 and 0.15) gave the same output, and the model gives x1 almost no weight, so this tests how far that flat area goes. The model predicts 4433 plus or minus 10, so the cost is small. If the output stays near 4440, x1 does not matter and F5 is close to finished. If it rises, x1 has a second good area to search.

**F6 (moderate, exploit).** Week 3 and Week 4 gave almost the same value, so I step back to a point between them. This is the raw model's best point, and it was the same for boxes of 0.05, 0.1 and 0.2, which makes it a stable answer. It predicts -0.389 plus or minus 0.02, a small gain. Both models agree that x4 should stay near 0.81. For x5 the raw model keeps 0 and the rank model wants about 0.05 to 0.11, so I keep 0, which is close to what the last two real results used (0.03 and 0).

**F7 (moderate to high, exploit).** Both the raw and rank models put their local best within about 0.05 of this point, and it is close to the Week 4 best. The raw model predicts 2.10 plus or minus 0.05. I keep x1 at 0 and make small changes: x2 0.22, x3 0.70, x4 0.275, x5 0.355, x6 0.80. I did not continue the full Week 3 to Week 4 line. That line would take x6 down to about 0.76, and the raw model predicts a lower value there (1.93), while both models keep x6 near 0.80.

**F8 (moderate, explore).** Last week I said I would explore F8 once the safe gains ran out, and they now have. The F8 model is the strongest of the eight (Spearman 0.99), so its EI point is worth trusting. It sits about 0.51 away from the best, moves x6 up to 0.79 and x8 down to 0.21, and predicts 9.85 plus or minus 0.17. That range includes values above the current best. The best of 9.945 stays safe whatever this point returns.

## 6. Honest limits

F2 and F3 are noisy, so one output can look better or worse than it really is. The F1 choice rests on a curve through four points on one line, so it says nothing about how the output changes across the line. The F4 model cannot see the narrow top, so its predictions near the best are too low and too smooth. For F6 the raw and rank models disagree, and I chose the raw model because the last two real results support it. The four exploration points (F2, F3, F5, F8) may all return lower values than the current best. That is expected, because their purpose is to learn about the function, and the best value for each is already safe.

## 7. Next steps

1. Submit these inputs through the portal and fill in the outputs table below.
2. Add the Week 5 outputs to `submissions.json` and refit all eight models.
3. For F1, if the output rises again, test a point across the line as well as along it, to find the true centre of the source.
4. For F2, if the corner is good, search around it. If it is poor, go back to x1 near 0.70 and average two nearby points to reduce the effect of noise.
5. For F3 and F5, use the one input test to decide whether to drop x1 from the search.
6. For F4, fit a curve through the Week 3, Week 4 and Week 5 points to place the narrow top.
7. For F8, if the EI point does well, search around it. If not, go back to small exploit steps.

## 8. Week 5 outputs (fill in after the portal replies)

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
