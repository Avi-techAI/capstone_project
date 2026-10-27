# Black Box Capstone: Week 3 Progress

**Cohort:** IMP-PCMLAI-26-06 | **Student:** Avi Thakur
**Course:** Imperial College London Professional Certificate in ML and AI
**Status of this file:** Week 3 inputs are proposed only. They were submitted and the outputs are in section 8.

---

## 1. What was submitted so far

| Function | Dim | Week 1 input | Week 2 input |
|---|---|---|---|
| F1 | 2 | `0.731024-0.733000` | `0.747350-0.757252` |
| F2 | 2 | `0.702637-0.926564` | `0.718372-0.000000` |
| F3 | 3 | `0.492581-0.611593-0.340176` | `0.614976-0.699593-0.383667` |
| F4 | 4 | `0.577766-0.428772-0.425826-0.249007` | `0.440364-0.425179-0.378308-0.397055` |
| F5 | 4 | `0.224189-0.846480-0.879484-0.878516` | `0.203449-0.958957-0.999999-0.960107` |
| F6 | 5 | `0.728186-0.154693-0.732552-0.693997-0.056401` | `0.447694-0.000000-0.909797-0.999999-0.000000` |
| F7 | 6 | `0.057896-0.491672-0.247422-0.218118-0.420428-0.730970` | `0.000000-0.117995-0.800238-0.320528-0.316723-0.893535` |
| F8 | 8 | `0.056447-0.065956-0.022929-0.038786-0.403935-0.801055-0.488307-0.893085` | `0.105641-0.000000-0.134347-0.000000-0.999999-0.471787-0.151664-0.399205` |

## 2. Outputs received

| Function | Week 1 output | Week 2 output | Best so far | Week 2 result |
|---|---|---|---|---|
| F1 | 7.71e-16 | 1.62e-23 | 7.71e-16 (W1) | Worse, still effectively zero |
| F2 | 0.6965 | 0.5388 | 0.6965 (W1) | Worse |
| F3 | -0.0334 | -0.0166 | -0.0166 (W2) | Better |
| F4 | -4.0256 | 0.2626 | 0.2626 (W2) | Much better, now positive |
| F5 | 1088.86 | 3452.92 | 3452.92 (W2) | Better, about 3.2 times higher |
| F6 | -0.6992 | -1.0053 | -0.6992 (W1) | Worse |
| F7 | 1.3650 | 1.5281 | 1.5281 (W2) | Better |
| F8 | 9.5985 | 9.9254 | 9.9254 (W2) | Better |

Five of eight functions improved in Week 2 (F3, F4, F5, F7, F8). Three did not (F1, F2, F6). The best value so far for those three is still the Week 1 result, so nothing was lost.

## 3. What the data shows for each function

**F1.** Almost every output in the data is close to zero, from 1e-124 up to 1e-16. The only large value is negative (-3.6e-03 at 0.650114-0.681526). The function looks like a very narrow peak that decays by many orders of magnitude over a short distance. From Week 1 to Week 2 we moved by (+0.016, +0.024) and the output fell from 7.7e-16 to 1.6e-23. That says we moved the wrong way, so the signal is to go the other way.

**F2.** Two separate regions give high values. Both have x1 near 0.67 to 0.72. One has x2 near 0.93 (0.6965) and the other has x2 near 0.0 to 0.12 (0.5388 and 0.5390). Points with x1 far from 0.7 score much lower. So x1 near 0.70 matters a lot, and x2 seems to work best at the edges.

**F3.** All outputs are negative, so the maximum is probably near zero. Week 2 moved in the direction (+0.12, +0.09, +0.04) and improved from -0.0334 to -0.0166. That is a consistent upward trend.

**F4.** The surface is smooth and the model is very reliable (leave one out Spearman 0.99). Moving every coordinate toward about 0.4 lifted the output from -4.03 to +0.26.

**F5.** The output is very large and very peaked (range 0.11 to 3453). Week 2 raised x2, x3 and x4 towards the upper edge and lowered x1 slightly, and the output tripled. The best point now sits on the upper boundary for x3.

**F6.** Week 2 moved far from the Week 1 point (distance about 0.6) and the output got worse. Pushing several inputs to the 0 or 1 edge at once did not help.

**F7.** Small improvement from 1.365 to 1.528. Week 2 moved x1 to 0 and x3, x6 upward. The trend is modest, so small steps look safer than big ones.

**F8.** Good model (Spearman 0.98). Week 2 improved the output from 9.60 to 9.93 by moving x5 to the upper edge and x2 and x4 to zero.

## 4. Method used for Week 3

Same Gaussian Process setup as Week 2 (ARD Matern 2.5 kernel, length scales bounded to 0.05 to 3.0, white noise term, Expected Improvement). Each model was refitted on the initial data plus both weeks of results. The output transform (raw or rank) was chosen again for each function by leave one out Spearman. Three candidate points were produced for each function: the EI point, a pure exploit point, and an EI point restricted to a box of plus or minus 0.1 around the best input.

The final Week 3 inputs below are **judgement blends** of those candidates and the Week 1 to Week 2 trend. They are not the raw model output. With only 12 to 42 points per function, the model can be wrong, so I kept steps small where the model skill is low.

| Function | Transform | LOO R2 | LOO Spearman | Model trust |
|---|---|---|---|---|
| F1 | rank | 0.05 | 0.71 | Low |
| F2 | rank | 0.28 | 0.69 | Low to moderate |
| F3 | rank | 0.57 | 0.82 | Moderate |
| F4 | raw | 0.98 | 0.99 | High |
| F5 | rank | 0.40 | 0.63 | Low to moderate |
| F6 | raw | 0.21 | 0.61 | Low to moderate |
| F7 | rank | 0.71 | 0.80 | Moderate |
| F8 | raw | 0.98 | 0.98 | High |

## 5. Week 3 proposed inputs

| Function | Dim | Input to submit | Style |
|---|---|---|---|
| F1 | 2 | `0.715000-0.709000` | Explore |
| F2 | 2 | `0.698000-0.990000` | Exploit |
| F3 | 3 | `0.660000-0.730000-0.400000` | Exploit along trend |
| F4 | 4 | `0.410500-0.417300-0.352000-0.434500` | Exploit |
| F5 | 4 | `0.150000-0.999999-0.999999-0.999999` | Exploit along trend, edge |
| F6 | 5 | `0.650000-0.230000-0.650000-0.770000-0.030000` | Recover, near Week 1 best |
| F7 | 6 | `0.000000-0.060000-0.860000-0.360000-0.280000-0.950000` | Exploit along trend |
| F8 | 8 | `0.125000-0.060000-0.160000-0.000000-0.999999-0.490000-0.200000-0.470000` | Exploit |

### Reasoning for each function

**F1 (low confidence).** The Week 1 to Week 2 step made the output fall by seven orders of magnitude. I continue the same line in the opposite direction by the same length, which lands at 0.715-0.709. This is between the Week 1 point and the negative point at 0.650-0.682. Because the best value is almost zero, a miss costs nothing and the information gain is high. The model has almost no skill here, so treat this as a probe.

**F2 (low to moderate).** The EI point and the exploit point agree on x1 near 0.695 to 0.701. They both want x2 at the upper edge, so I use 0.990 to stay slightly inside the boundary. This tests whether the high x2 end of the x1 ridge can beat 0.6965. The low x2 region (0.539) is left for a later week.

**F3 (moderate).** Week 2 improved along one direction. I continue about half of that step. The EI point is far away (distance 0.51), which is exploration I do not need yet, because the trend is still improving.

**F4 (high).** EI and exploit agree to within 0.02. The model predicts a small gain (about 0.02 in standardised units) with low uncertainty, so I expect a small improvement over 0.2626, not a jump. The point is a blend of the two.

**F5 (low to moderate).** This function has the largest upside. Week 2 shows that high x2, x3, x4 and lower x1 is the right direction, and both the exploit and the local EI point say x1 should fall further (to about 0.05 to 0.10). I take a smaller step to x1 = 0.15. The risk is that the peak is narrow, so a wrong step can drop the output by a large factor. The best point still has the other three inputs on the upper edge, so I keep them there.

**F6 (low to moderate).** Week 2 was a bad move. I go back near the Week 1 best and take about half of the step the local model suggests (x1 and x3 down a little, x4 up a little, x2 up a little). I keep x5 close to zero but not on the edge.

**F7 (moderate).** I keep x1 at 0 and move x2 lower, and x3, x4 and x6 higher, about a quarter to a half of the Week 1 to Week 2 step. The exploit point sits almost on the current best, so this is a small, careful push.

**F8 (high).** The exploit point is about 0.17 from the best and predicts a gain with small uncertainty. I use a slightly shorter step. EI wanted a far corner with two coordinates on the upper edge, which I did not follow this week.

## 6. Honest limits

Two weeks of results is very little data. The models for F1, F2, F5 and F6 have low skill, and the Week 2 results for F2 and F6 show the model can point the wrong way. The final inputs are blends chosen by judgement, so I cannot give a predicted gain for them. I expect small gains on F4 and F8, a possible gain on F3, F5 and F7, and no guaranteed gain on F1, F2 and F6.

## 7. Next steps

1. Submit these inputs through the portal and fill in the outputs table below.
2. Add the Week 3 results to `submissions.json` and refit all eight models.
3. Check whether the step along the trend still helps for F3, F5 and F7. If a function drops, step back towards its best point.
4. For F1, if the output is still near zero, test a different region.
5. For F2, test the low x2 ridge once the high x2 side is understood.
6. Keep one file per week (Week_4_Progress.md next) with the same sections.

## 8. Week 3 outputs

| Function | Output received | Better than best so far? | New best |
|---|---|---|---|
| F1 | 3.843061e-10 | Yes | 3.84e-10 (W3) |
| F2 | 0.596109 | No | 0.6965 (W1) |
| F3 | -0.037613 | No | -0.0166 (W2) |
| F4 | 0.554005 | Yes | 0.5540 (W3) |
| F5 | 4443.107049 | Yes | 4443.11 (W3) |
| F6 | -0.424196 | Yes | -0.4242 (W3) |
| F7 | 1.061025 | No | 1.5281 (W2) |
| F8 | 9.943660 | Yes | 9.9437 (W3) |
