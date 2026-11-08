# Black Box Capstone: Week 1 Progress

**Cohort:** IMP-PCMLAI-26-06 | **Student:** Avdhesh Thakur
**Course:** Imperial College London Professional Certificate in ML and AI
**Status:** I submitted my Week 1 inputs and recorded the outputs in section 8.

---

## 1. The starting data I was given

There are eight black box functions. Each one takes between 2 and 8 inputs, each between 0 and 1, and returns one number. The goal is to make every output as high as possible by Week 13. I can send one input per function each week.

The course gave me some starting data for each function.

| Function | Dim | Initial points | Best initial output |
|---|---|---|---|
| F1 | 2 | 10 | 7.71e-16 |
| F2 | 2 | 10 | 0.6112 |
| F3 | 3 | 15 | -0.0348 |
| F4 | 4 | 30 | -4.0255 |
| F5 | 4 | 20 | 1088.86 |
| F6 | 5 | 20 | -0.7143 |
| F7 | 6 | 30 | 1.3650 |
| F8 | 8 | 40 | 9.5985 |

## 2. How I chose the Week 1 inputs

For Week 1 I did not run Bayesian Optimisation yet. I looked at the starting data for each function and picked the input that gave the highest output. Then I sent that same input to the portal.

I did this for two reasons. First, it gives me a confirmed starting point from the portal itself. Second, it shows whether the portal gives the same answer for the same input, which tells me if the functions are noisy.

## 3. What I learned from the starting data

**F1.** Nearly every output is almost exactly zero, from about 1e-124 up to 1e-16. The only clear value is negative (-3.6e-03 at 0.650-0.682). There is very little signal to work with.

**F2.** The best values have x1 near 0.70. Points far from that score much lower.

**F3.** Every output is negative, so the maximum is probably close to zero.

**F4.** Every output is negative, from about -33 up to -4. There is a lot of room to improve.

**F5.** The outputs are very large and spread out, from about 0.1 to 1089. One point is far above the rest.

**F6.** Every output is negative, from about -2.6 up to -0.71.

**F7.** Outputs go from near zero up to 1.365.

**F8.** Outputs go from about 5.6 up to 9.6. This looks like a smooth function.

## 4. My Week 1 inputs

| Function | Dim | My input | Style |
|---|---|---|---|
| F1 | 2 | `0.731024-0.733000` | Baseline |
| F2 | 2 | `0.702637-0.926564` | Baseline |
| F3 | 3 | `0.492581-0.611593-0.340176` | Baseline |
| F4 | 4 | `0.577766-0.428772-0.425826-0.249007` | Baseline |
| F5 | 4 | `0.224189-0.846480-0.879484-0.878516` | Baseline |
| F6 | 5 | `0.728186-0.154693-0.732552-0.693997-0.056401` | Baseline |
| F7 | 6 | `0.057896-0.491672-0.247422-0.218118-0.420428-0.730970` | Baseline |
| F8 | 8 | `0.056447-0.065956-0.022929-0.038786-0.403935-0.801055-0.488307-0.893085` | Baseline |

Every input is the best point from the starting data, so there is no separate reasoning for each function this week.

## 5. What I am not sure about

This week does not try to improve anything. It only confirms where I start. The real search starts in Week 2.

## 6. My next steps

1. I will record the outputs in section 8 when the portal replies.
2. I will fit a Gaussian Process for each function on the starting data plus the Week 1 result.
3. I will use Expected Improvement to choose my Week 2 inputs.
4. I will keep one file per week (Week_2_Progress.md next) with the same sections.

## 7. Notes I added later

The Week 1 results turned out to be useful in a way I did not expect. For F2, the same input gave 0.6112 in the starting data and 0.6965 from the portal. That means F2 is noisy. F3 and F6 also came back slightly different from the starting data. I only noticed this properly in Week 4, and it changed how I treat F2.

## 8. Week 1 outputs

| Function | Output received | Initial best | Same as initial? |
|---|---|---|---|
| F1 | 7.71e-16 | 7.71e-16 | Yes |
| F2 | 0.6965 | 0.6112 | No, higher (noise) |
| F3 | -0.0334 | -0.0348 | Slightly higher |
| F4 | -4.0256 | -4.0255 | Yes |
| F5 | 1088.858 | 1088.860 | Yes |
| F6 | -0.6992 | -0.7143 | Slightly higher |
| F7 | 1.3650 | 1.3650 | Yes |
| F8 | 9.5985 | 9.5985 | Yes |
