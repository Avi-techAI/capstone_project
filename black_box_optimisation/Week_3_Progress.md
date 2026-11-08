# Black Box Capstone: Week 3 Progress

**Cohort:** IMP-PCMLAI-26-06
**Student:** Avdhesh Thakur
**Course:** Imperial College London Professional Certificate in ML and AI

This file is my Week 3 update. I submitted my Week 3 inputs and recorded the outputs in section 8. My Week 4 plan is in Week_4_Progress.md.

## 1. What I submitted in Weeks 1 and 2

| Function | Size | Week 1 input | Week 2 input |
|---|---|---|---|
| F1 | 2 | `0.731024-0.733000` | `0.747350-0.757252` |
| F2 | 2 | `0.702637-0.926564` | `0.718372-0.000000` |
| F3 | 3 | `0.492581-0.611593-0.340176` | `0.614976-0.699593-0.383667` |
| F4 | 4 | `0.577766-0.428772-0.425826-0.249007` | `0.440364-0.425179-0.378308-0.397055` |
| F5 | 4 | `0.224189-0.846480-0.879484-0.878516` | `0.203449-0.958957-0.999999-0.960107` |
| F6 | 5 | `0.728186-0.154693-0.732552-0.693997-0.056401` | `0.447694-0.000000-0.909797-0.999999-0.000000` |
| F7 | 6 | `0.057896-0.491672-0.247422-0.218118-0.420428-0.730970` | `0.000000-0.117995-0.800238-0.320528-0.316723-0.893535` |
| F8 | 8 | `0.056447-0.065956-0.022929-0.038786-0.403935-0.801055-0.488307-0.893085` | `0.105641-0.000000-0.134347-0.000000-0.999999-0.471787-0.151664-0.399205` |

## 2. What the outputs were

| Function | Week 1 output | Week 2 output | Best so far | What happened |
|---|---|---|---|---|
| F1 | 7.71e-16 | 1.62e-23 | 7.71e-16 | Worse. The output is still almost zero. |
| F2 | 0.6965 | 0.5388 | 0.6965 | Worse. Week 1 is still the best. |
| F3 | -0.0334 | -0.0166 | -0.0166 | Better. |
| F4 | -4.0256 | 0.2626 | 0.2626 | Much better. It is the first positive value. |
| F5 | 1088.86 | 3452.92 | 3452.92 | Better. It is about 3.2 times higher. |
| F6 | -0.6992 | -1.0053 | -0.6992 | Worse. Week 1 is still the best. |
| F7 | 1.3650 | 1.5281 | 1.5281 | Better. |
| F8 | 9.5985 | 9.9254 | 9.9254 | Better. |

Five of the eight functions got better in Week 2. They are F3, F4, F5, F7 and F8. Three did not get better, which are F1, F2 and F6. For those three, my best result is still from Week 1, so I did not lose anything.

## 3. What I learned about each function

**F1.** Almost every output is close to zero. The only large value is negative, at -0.0036. It looks like a very narrow peak. In Week 2 I moved a small step in one direction and the output dropped a lot. This tells me to try the other direction.

**F2.** High values appear when x1 is close to 0.70. There are two good areas for x2. One is near 0.93 and gives 0.6965. The other is near 0.0 to 0.12 and gives about 0.539.

**F3.** All outputs are negative, so the best value is probably close to zero. My Week 2 step made the output better, so the direction looks right.

**F4.** This function behaves smoothly and my model predicts it well. When I moved all four inputs closer to 0.4, the output went from -4.03 to 0.26.

**F5.** The outputs are very large and the peak looks narrow. In Week 2 I raised the last three inputs close to the top edge and lowered x1 a little. The output became about three times bigger.

**F6.** My Week 2 step was too big, and the output got worse. Moving many inputs to the edge at the same time did not help.

**F7.** The output improved a little, from 1.365 to 1.528. Small steps look safer here.

**F8.** My model works well on this function. The Week 2 step improved the output from 9.60 to 9.93.

## 4. How I picked the Week 3 inputs

I trained a model (a Gaussian Process) for each function. I used the starting data and my results from Weeks 1 and 2. Before I trusted a model, I tested it by hiding one data point at a time and checking if the model could predict it. A model that predicts well gets more trust from me.

For each function I looked at three candidate points:

1. The point with the best Expected Improvement score. This point balances a high guess with high uncertainty.
2. The point where the model predicts the highest output.
3. A point close to my current best input.

Then I made the final choice myself. I used these three points and the direction that worked from Week 1 to Week 2. So the final inputs are my own choices and not a direct answer from the model. I kept the steps small where the model is weak.

| Function | How well the model predicts (0 to 1) | How much I trust it |
|---|---|---|
| F1 | 0.71 | Low |
| F2 | 0.69 | Low to medium |
| F3 | 0.82 | Medium |
| F4 | 0.99 | High |
| F5 | 0.63 | Low to medium |
| F6 | 0.61 | Low to medium |
| F7 | 0.80 | Medium |
| F8 | 0.98 | High |

## 5. My Week 3 inputs and my thinking

| Function | Week 3 input | What the data showed | My thinking | Confidence |
|---|---|---|---|---|
| F1 | `0.715000-0.709000` | My Week 2 step went the wrong way and the output dropped by seven orders of magnitude. | I go the opposite way by the same distance. This is a test of a new area. A bad result costs me nothing because my best value is almost zero. | Low |
| F2 | `0.698000-0.990000` | High values appear when x1 is near 0.70. My best point has x2 near 0.93. | Both methods agree on x1 near 0.70 and x2 near the top edge. I stay just inside the edge. | Low to medium |
| F3 | `0.660000-0.730000-0.400000` | My last step improved the output from -0.0334 to -0.0166. | The trend is still good, so I take about half of the same step again. | Medium |
| F4 | `0.410500-0.417300-0.352000-0.434500` | All inputs near 0.4 gave a big gain, and the model is very reliable. | Both methods agree, so I use a mix of the two points. I expect a small gain and not a big jump. | High |
| F5 | `0.150000-0.999999-0.999999-0.999999` | A lower x1 with the other inputs near the top edge made the output three times bigger. | I follow the same direction with a smaller step on x1. This function could give the biggest gain, but the peak is narrow, so a wrong step can cost a lot. | Low to medium |
| F6 | `0.650000-0.230000-0.650000-0.770000-0.030000` | My Week 2 step was too big and the output got worse. | I go back close to my Week 1 best and take a small step that the model suggests. | Low to medium |
| F7 | `0.000000-0.060000-0.860000-0.360000-0.280000-0.950000` | The output improved a little, from 1.365 to 1.528. | I take a small step in the same direction, because big steps look risky here. | Medium |
| F8 | `0.125000-0.060000-0.160000-0.000000-0.999999-0.490000-0.200000-0.470000` | The model is good, and the Week 2 gain was from 9.60 to 9.93. | The model predicts a gain with low uncertainty, so I take a slightly shorter step. | High |

## 6. What I am not sure about

I only have two weeks of results, so this is a small amount of data. The models for F1, F2, F5 and F6 are not strong. My Week 2 results on F2 and F6 show that the model can point the wrong way. I cannot give an exact predicted gain for the final inputs, because I adjusted them myself. I expect small gains on F4 and F8. I think gains are possible on F3, F5 and F7. I am not sure about F1, F2 and F6.

## 7. My next steps

1. I will submit these inputs in the portal and record the outputs in section 8.
2. I will add the Week 3 results to `submissions.json` and train the eight models again.
3. I will check if the same direction still helps for F3, F5 and F7. If a result drops, I will go back towards the best point.
4. For F1, if the output is still near zero, I will try a new area.
5. For F2, I will try the low x2 area after I understand the high x2 area.
6. I will write one file for each week. The next file will be `Week_4_Progress.md`, with the same sections.

## 8. Week 3 outputs

| Function | Output received | Better than best so far? | New best |
|---|---|---|---|
| F1 | 3.84e-10 | Yes, about 500,000 times higher | 3.84e-10 (W3) |
| F2 | 0.5961 | No, but inside the noise | 0.6965 (W1) |
| F3 | -0.0376 | No | -0.0166 (W2) |
| F4 | 0.5540 | Yes, about double | 0.5540 (W3) |
| F5 | 4443.11 | Yes, up about 29% | 4443.11 (W3) |
| F6 | -0.4242 | Yes | -0.4242 (W3) |
| F7 | 1.0610 | No | 1.5281 (W2) |
| F8 | 9.9437 | Yes, slightly | 9.9437 (W3) |
