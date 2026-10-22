# Black Box Capstone: Week 2 Progress

**Cohort:** IMP-PCMLAI-26-06 | **Student:** Avi Thakur
**Course:** Imperial College London Professional Certificate in ML and AI
**Status of this file:** Week 2 inputs were submitted and the outputs are in section 8.

---

## 1. What was submitted so far

| Function | Dim | Week 1 input |
|---|---|---|
| F1 | 2 | `0.731024-0.733000` |
| F2 | 2 | `0.702637-0.926564` |
| F3 | 3 | `0.492581-0.611593-0.340176` |
| F4 | 4 | `0.577766-0.428772-0.425826-0.249007` |
| F5 | 4 | `0.224189-0.846480-0.879484-0.878516` |
| F6 | 5 | `0.728186-0.154693-0.732552-0.693997-0.056401` |
| F7 | 6 | `0.057896-0.491672-0.247422-0.218118-0.420428-0.730970` |
| F8 | 8 | `0.056447-0.065956-0.022929-0.038786-0.403935-0.801055-0.488307-0.893085` |

## 2. Outputs received

| Function | Week 1 output | Best so far |
|---|---|---|
| F1 | 7.71e-16 | 7.71e-16 (W1) |
| F2 | 0.6965 | 0.6965 (W1) |
| F3 | -0.0334 | -0.0334 (W1) |
| F4 | -4.0256 | -4.0256 (W1) |
| F5 | 1088.86 | 1088.86 (W1) |
| F6 | -0.6992 | -0.6992 (W1) |
| F7 | 1.3650 | 1.3650 (W1) |
| F8 | 9.5985 | 9.5985 (W1) |

Week 1 was a baseline, so these are simply the best points from the starting data, checked through the portal.

## 3. What went wrong in my first attempt

My first try at Week 2 gave bad answers, and I threw it away. I am keeping a short record here, because checking the output is as important as the result.

1. **Three answers were just random numbers.** F2, F3 and F6 all started with `0.374540-0.950714`. Those are the first numbers numpy gives with seed 42. The optimiser found a flat surface, did not move, and gave back its own starting point.
2. **The model had collapsed.** On those functions the length scale sat at its lowest limit (1e-05), so the model learned nothing.
3. **The exploration setting was wrong.** I used a fixed value of 0.01 for all functions, but their output ranges are completely different. For F1 the whole range is about 0.004, so Expected Improvement was forced to zero for F1, F4 and F8.
4. **Some length scales were far too big.** For F2 the model decided x2 did not matter at all, with a length scale of 100. On inputs between 0 and 1 that makes no sense. I set the upper limit to 3.0.
5. **I used one output transform for all eight functions.** I tested raw and rank outputs properly for each function and they split four and four.

## 4. Method used for Week 2

I fitted a Gaussian Process for each function on the starting data plus the Week 1 result. The kernel is ARD Matern 2.5 (one length scale per input), with length scales bounded to 0.05 to 3.0 and a white noise term. I chose raw or rank outputs for each function by leave one out Spearman. I used Spearman and not R2 to compare, because a transform that squashes the outputs makes R2 look better than it is. I found the Expected Improvement point with a wide random screen followed by local polishing. I also found a pure exploit point (highest predicted mean) as a second, separate check.

| Function | Transform | LOO R2 | LOO Spearman | Model trust |
|---|---|---|---|---|
| F1 | rank | -0.07 | 0.55 | Very low |
| F2 | raw | 0.41 | 0.65 | Low |
| F3 | rank | 0.50 | 0.75 | Moderate |
| F4 | raw | 0.97 | 0.98 | High |
| F5 | raw | 0.94 | 0.57 | Moderate |
| F6 | rank | 0.73 | 0.86 | High |
| F7 | rank | 0.64 | 0.77 | Moderate to high |
| F8 | raw | 0.98 | 0.98 | High |

F5 has a high R2 but only 0.57 Spearman. One very large value controls most of the spread, so the Spearman figure is the honest one.

## 5. Week 2 inputs

The gap column is the distance between the EI point and the exploit point. A small gap means two separate methods picked nearly the same place.

| Function | Dim | Input submitted | Gap | Confidence |
|---|---|---|---|---|
| F1 | 2 | `0.747350-0.757252` | 0.02 | Low (probe) |
| F2 | 2 | `0.718372-0.000000` | 0.81 | Low (probe) |
| F3 | 3 | `0.614976-0.699593-0.383667` | 0.12 | Moderate |
| F4 | 4 | `0.440364-0.425179-0.378308-0.397055` | 0.0001 | High |
| F5 | 4 | `0.203449-0.958957-0.999999-0.960107` | 0.005 | High |
| F6 | 5 | `0.447694-0.000000-0.909797-0.999999-0.000000` | 0.035 | High |
| F7 | 6 | `0.000000-0.117995-0.800238-0.320528-0.316723-0.893535` | 0.26 | Moderate |
| F8 | 8 | `0.105641-0.000000-0.134347-0.000000-0.999999-0.471787-0.151664-0.399205` | 0.036 | High |

### Reasoning for each function

**F1 (low).** The model has no real skill here. The one large value in the data is negative (-3.6e-03 at 0.650-0.682), and the best positive value is almost zero, which looks like a point where the sign changes. I take a small step past the best point, away from the negative one, hoping to reach a positive region.

**F2 (low).** Both methods agree that x1 should be about 0.70 to 0.72, but they disagree a lot on x2. That suggests x2 has little effect. I test the low x2 end.

**F3 (moderate).** EI and exploit are fairly close. The point moves all three inputs up a little from the best.

**F4 (high).** EI and exploit agree almost exactly. The sensitivity plots also show all four inputs peaking together near 0.43.

**F5 (high).** With rank outputs, EI wanted to jump to a corner with x1 = 0 and leave the good region. Raw outputs predict F5 better, and with raw outputs EI stays near x1 = 0.20, right beside the best point, and agrees with exploit to within 0.005. So I follow the better model.

**F6 (high).** The model predicts a real gain, and the two methods agree to within 0.035.

**F7 (moderate).** EI predicts only a small change. I take its point as a careful step.

**F8 (high).** One of the two strongest models. EI and exploit agree to within 0.036.

## 6. Honest limits

This is the first real model based week. The models for F1 and F2 have little skill, so those two are probes that buy information rather than score. I expect the best chance of a gain on F4, F5, F6 and F8.

## 7. Next steps

1. Fill in the outputs table when the portal replies.
2. Check if F8, the strongest model, improved. A miss there would teach me the most.
3. Check if F1 gave anything above 1e-16.
4. Keep one file per week (Week_3_Progress.md next) with the same sections.

## 8. Week 2 outputs

| Function | Output received | Better than best so far? | New best |
|---|---|---|---|
| F1 | 1.62e-23 | No | 7.71e-16 (W1) |
| F2 | 0.5388 | No | 0.6965 (W1) |
| F3 | -0.0166 | Yes | -0.0166 (W2) |
| F4 | 0.2626 | Yes | 0.2626 (W2) |
| F5 | 3452.92 | Yes | 3452.92 (W2) |
| F6 | -1.0053 | No | -0.6992 (W1) |
| F7 | 1.5281 | Yes | 1.5281 (W2) |
| F8 | 9.9254 | Yes | 9.9254 (W2) |
