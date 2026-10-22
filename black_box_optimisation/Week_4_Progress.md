# Black Box Capstone: Week 4 Progress

**Cohort:** IMP-PCMLAI-26-06 | **Student:** Avi Thakur
**Course:** Imperial College London Professional Certificate in ML and AI
**Status of this file:** Week 4 inputs are proposed only. They have not been submitted yet. Fill in the outputs table after the portal replies.

---

## 1. What was submitted so far

| Function | Dim | Week 1 input | Week 2 input | Week 3 input |
|---|---|---|---|---|
| F1 | 2 | `0.731024-0.733000` | `0.747350-0.757252` | `0.715000-0.709000` |
| F2 | 2 | `0.702637-0.926564` | `0.718372-0.000000` | `0.698000-0.990000` |
| F3 | 3 | `0.492581-0.611593-0.340176` | `0.614976-0.699593-0.383667` | `0.660000-0.730000-0.400000` |
| F4 | 4 | `0.577766-0.428772-0.425826-0.249007` | `0.440364-0.425179-0.378308-0.397055` | `0.410500-0.417300-0.352000-0.434500` |
| F5 | 4 | `0.224189-0.846480-0.879484-0.878516` | `0.203449-0.958957-0.999999-0.960107` | `0.150000-0.999999-0.999999-0.999999` |
| F6 | 5 | `0.728186-0.154693-0.732552-0.693997-0.056401` | `0.447694-0.000000-0.909797-0.999999-0.000000` | `0.650000-0.230000-0.650000-0.770000-0.030000` |
| F7 | 6 | `0.057896-0.491672-0.247422-0.218118-0.420428-0.730970` | `0.000000-0.117995-0.800238-0.320528-0.316723-0.893535` | `0.000000-0.060000-0.860000-0.360000-0.280000-0.950000` |
| F8 | 8 | `0.056447-0.065956-0.022929-0.038786-0.403935-0.801055-0.488307-0.893085` | `0.105641-0.000000-0.134347-0.000000-0.999999-0.471787-0.151664-0.399205` | `0.125000-0.060000-0.160000-0.000000-0.999999-0.490000-0.200000-0.470000` |

## 2. Outputs received

| Function | Week 1 output | Week 2 output | Week 3 output | Best so far | Week 3 result |
|---|---|---|---|---|---|
| F1 | 7.71e-16 | 1.62e-23 | 3.84e-10 | 3.84e-10 (W3) | Better, about a million times higher |
| F2 | 0.6965 | 0.5388 | 0.5961 | 0.6965 (W1) | Worse, but inside the noise |
| F3 | -0.0334 | -0.0166 | -0.0376 | -0.0166 (W2) | Worse |
| F4 | -4.0256 | 0.2626 | 0.5540 | 0.5540 (W3) | Better, about double |
| F5 | 1088.86 | 3452.92 | 4443.11 | 4443.11 (W3) | Better, up about 29% |
| F6 | -0.6992 | -1.0053 | -0.4242 | -0.4242 (W3) | Better, new best |
| F7 | 1.3650 | 1.5281 | 1.0610 | 1.5281 (W2) | Worse |
| F8 | 9.5985 | 9.9254 | 9.9437 | 9.9437 (W3) | Slightly better |

Five of eight functions set a new best in Week 3 (F1, F4, F5, F6, F8). Three did not (F2, F3, F7). The best value for those three is still safe from an earlier week.

## 3. What the data shows for each function

**F1.** The Week 3 probe worked. Going back the other way from the Week 2 move raised the output from 7.7e-16 to 3.8e-10. The three points on that line (Week 2, Week 1, Week 3) fit a simple curve in log scale, and the curve says the output keeps rising for about two more steps in the same direction. The one negative value in the data (-3.6e-03 at 0.650-0.682) sits close to the end of that line, so I should not go too far.

**F2.** I found something important here. The initial data and my Week 1 submission are the exact same point (0.702637-0.926564), but they gave different outputs: 0.6112 and 0.6965. So F2 is noisy, by about 0.05 or more. This means the Week 3 result of 0.5961 is not clearly worse than the best. The model now says x1 near 0.70 matters a lot and x2 hardly matters at all (length scale for x2 hit the upper limit of 3.0).

**F3.** Going further along the Week 2 trend made things worse (-0.0376). So the peak is between the Week 1 and Week 2 points, or just around the Week 2 point. The model says x3 is the most sensitive input (length scale 0.09) and x1 barely matters. The Week 1 point also has a repeat in the initial data (-0.0334 and -0.0348), so F3 has a small amount of noise too, but much less than the Week 3 drop.

**F4.** Another clear gain. The model is still very reliable (leave one out Spearman 0.98) and the exploit point is only 0.01 away from the Week 3 point. That tells me we are now very close to the top of this function.

**F5.** Lowering x1 to 0.15 with the other three inputs on the upper edge raised the output to 4443. The trend from Week 1 to Week 3 is steady: x1 down and x2, x3, x4 up gives a higher value each time.

**F6.** Going back near the Week 1 best and taking a half step worked well. The output went from -0.6992 to -0.4242. All three model candidates now agree on the same area, which continues the same direction (x1 and x3 down, x2 and x4 up, x5 to zero).

**F7.** Pushing further along the Week 2 trend failed (1.061 against 1.528). So the Week 2 step was already a bit too far for some inputs. All three model candidates now want x2 a bit higher and x3 and x6 a bit lower than the Week 2 best, which is a step back the other way.

**F8.** Small gain again, 9.925 to 9.944. The model is still very good (Spearman 0.99) and the exploit point predicts almost the same value as the current best. Gains here are getting very small.

## 4. Method used for Week 4

Same Gaussian Process setup as Week 3 (ARD Matern 2.5 kernel, length scales bounded to 0.05 to 3.0, white noise term, Expected Improvement). Each model was refitted on the initial data plus all three weeks of results. I kept repeated points as separate rows this time, because the repeats showed that F2 and F3 are noisy. The output transform (raw or rank) was chosen again for each function by leave one out Spearman. Three candidates were produced for each function: the EI point, a pure exploit point, and an EI point restricted to a box of plus or minus 0.1 around the best input.

For F1 I also fitted a simple curve to the log of the output along the line through the Week 1, 2 and 3 points, because the outputs change by many orders of magnitude and the GP cannot see that well.

The final Week 4 inputs below are **judgement blends** of those candidates and the trends so far. They are not the raw model output.

| Function | Transform | LOO R2 | LOO Spearman | Model trust |
|---|---|---|---|---|
| F1 | rank | -0.21 | 0.29 | Very low |
| F2 | raw | 0.48 | 0.70 | Low to moderate |
| F3 | rank | 0.63 | 0.80 | Moderate |
| F4 | raw | 0.98 | 0.98 | High |
| F5 | rank | 0.40 | 0.65 | Low to moderate |
| F6 | raw | 0.40 | 0.80 | Moderate |
| F7 | rank | 0.57 | 0.76 | Moderate |
| F8 | raw | 0.98 | 0.99 | High |

F6 moved up from low to moderate trust because its Spearman rose from 0.61 to 0.80. F1 dropped because the new point is far above all the others, which the model cannot predict.

## 5. Week 4 proposed inputs

| Function | Dim | Input to submit | Style | Confidence |
|---|---|---|---|---|
| F1 | 2 | `0.697000-0.682000` | Exploit along trend | Low to moderate |
| F2 | 2 | `0.705000-0.560000` | Explore along ridge | Low |
| F3 | 3 | `0.560000-0.660000-0.372000` | Step back towards best | Moderate |
| F4 | 4 | `0.406800-0.414700-0.344200-0.438700` | Exploit | High |
| F5 | 4 | `0.080000-0.999999-0.999999-0.999999` | Exploit along trend, edge | Moderate |
| F6 | 5 | `0.585000-0.315000-0.565000-0.830000-0.000000` | Exploit along trend | Moderate |
| F7 | 6 | `0.000000-0.200000-0.720000-0.310000-0.330000-0.810000` | Step back towards best | Moderate |
| F8 | 8 | `0.126000-0.080000-0.166000-0.000000-0.999999-0.503000-0.228000-0.532000` | Exploit | High |

### Reasoning for each function

**F1 (low to moderate).** I fitted a curve to the log output along the line from Week 2 through Week 1 to Week 3. It peaks about 3.4 steps past the Week 1 point, near 0.677-0.652. I stop shorter, at about 2.1 steps, which lands at 0.697-0.682. The curve predicts something near 1e-6 there, which would be another big jump. I do not go all the way, because the negative point at 0.650-0.682 is only about 0.05 away and I do not know where the sign changes.

**F2 (low).** Because F2 is noisy, sending the same point again would only tell me about the noise. The model says only x1 matters, and the best x1 looks like 0.70 to 0.705. So I keep x1 at 0.705 and test x2 in the middle, at 0.56, where there is no data yet at this x1. If the output is close to 0.6 or higher, then x2 really does not matter and I can focus only on x1. If it drops a lot, then the two edges of x2 are the good regions. The model predicts about 0.61 plus or minus 0.05, so this may not beat 0.6965, but it should tell me a lot.

**F3 (moderate).** Week 3 went too far. The exploit point and the local EI point both sit between the Week 1 and Week 2 points, with x3 slightly lower than the best. I take about half the step from the Week 2 best towards the exploit point. The model rates this close to the best, so I expect a value near -0.017, with a fair chance of a small gain.

**F4 (high).** I use the exploit point. It is only 0.01 from the Week 3 point and the model predicts 0.561 plus or minus 0.024, so a small gain over 0.554. The EI point is almost the same. I think we are near the top of F4 now, and later weeks only need small checks.

**F5 (moderate).** Each week that x1 went down with the other three on the edge, the output went up (1089, 3453, 4443). I continue this and move x1 from 0.15 to 0.08, and keep x2, x3 and x4 at the upper edge. The local EI point also wants x1 near 0.05. The model with rank outputs suggests lowering x3 a little, but every real result so far says the edge is better, so I trust the data here. The risk is that the gain slows down or reverses close to x1 = 0.

**F6 (moderate).** All three candidates agree within about 0.03. I use a point just short of the exploit point, which continues the same direction that worked in Week 3. x5 goes to 0 because every candidate puts it there. The model predicts -0.32 plus or minus 0.09, which would be a new best.

**F7 (moderate).** I go back to the Week 2 best and move the way all three candidates agree: x2 up to 0.20, x3 down to 0.72, x6 down to 0.81, and x4 and x5 almost unchanged. x1 stays at 0. This is close to the local EI point, which is about 0.14 from the best, so it is a careful step.

**F8 (high).** The exploit point is about 0.07 from the best and predicts 9.947 plus or minus 0.013, so only a tiny gain. I use it anyway, because it is safe. The EI point is a far corner (two inputs on the edge, distance 0.58), which I keep in mind as a possible exploration week later, once the safer gains run out.

## 6. Honest limits

F2 and F3 are noisy, so a single output can look better or worse than it really is. The F1 model has almost no skill, and my F1 choice rests on a curve through only three points on one line. The F5 model with rank outputs disagrees with the real trend, so my F5 choice follows the data and not the model. The predicted values above come from the models, not from the final blends, except where I said the point is the exploit point. I expect small gains on F4 and F8, a likely gain on F6, a possible gain on F1, F3, F5 and F7, and F2 is mainly a test.

## 7. Next steps

1. Submit these inputs through the portal and fill in the outputs table below.
2. Add the Week 3 and Week 4 results to `submissions.json` (it still has null outputs for Week 2) and refit all eight models.
3. For F1, if the output rises again, take one more short step along the same line. If it turns negative, step back towards 0.715-0.709.
4. For F2, use the result to decide if x2 matters at all.
5. For F4 and F8, think about one exploration week, since the safe gains are now very small.
6. Keep one file per week (Week_5_Progress.md next) with the same sections.

## 8. Week 4 outputs (fill in after the portal replies)

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
