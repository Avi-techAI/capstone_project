# Black Box Optimisation Capstone

**Student:** Avi Thakur | **Cohort:** IMP-PCMLAI-26-06
**Course:** Imperial College London Professional Certificate in Machine Learning and Artificial Intelligence

## The challenge

There are eight unknown functions, from 2 to 8 inputs each. Every input is a number between 0 and 1. I cannot see inside the functions. Each week I may send one input point per function and get back one output value. The goal is to find the input that gives the highest output for each function, with as few queries as possible.

| Function | Inputs | What it stands for |
|---|---|---|
| F1 | 2 | Finding a radiation source. The output is close to zero except near a source. |
| F2 | 2 | A noisy log likelihood with local optima. |
| F3 | 3 | Drug discovery. Side effects are negated, so closer to zero is better. |
| F4 | 4 | Warehouse placement with many local optima. |
| F5 | 4 | Chemical yield, usually with a single peak. |
| F6 | 5 | A cake recipe. The score is negative by design, so closer to zero is better. |
| F7 | 6 | Tuning six settings of a machine learning model. |
| F8 | 8 | Tuning eight settings of a machine learning model. |

## My method

1. For each function I fit a Gaussian Process model on the starting data plus every weekly result so far.
2. The model uses a Matern 2.5 kernel with a separate length scale for each input, so it shows which inputs matter most. A noise term handles functions that give different outputs for the same input.
3. For each function I test two versions of the output, the raw values and their ranks. I usually keep the one that predicts better in leave one out testing, and I say so in the weekly notes when I make an exception.
4. I produce several candidate points: the Expected Improvement point, the point with the highest predicted value, and the same two inside a small box around the best point so far.
5. I choose the final input by judgement. I compare the candidates with the real trend from earlier weeks, and decide each week whether the function needs exploration (a new area) or exploitation (a small step near the best).

## Best result so far (after Week 4)

| Function | Best output | Week found |
|---|---|---|
| F1 | 5.66e-06 | 4 |
| F2 | 0.6965 | 1 |
| F3 | -0.0166 | 2 |
| F4 | 0.5540 | 3 |
| F5 | 4443.11 | 3 |
| F6 | -0.4142 | 4 |
| F7 | 2.0818 | 4 |
| F8 | 9.9453 | 4 |

![Best output so far for each function](figures/01_convergence.png)

## Weekly notes

Each week has its own file with the inputs, the outputs, what I learned and the plan for the next round.

* [Week 1](Week_1_Progress.md)
* [Week 2](Week_2_Progress.md)
* [Week 3](Week_3_Progress.md)
* [Week 4](Week_4_Progress.md)
* [Week 5](Week_5_Progress.md)

## Files in this repository

| File | What it holds |
|---|---|
| `submissions.json` | Every weekly input and output, and the reason for each choice |
| `visualise_progress.py` | Fits the models and draws every chart in `figures/` |
| `figures/` | Progress charts, model quality and input sensitivity |
| `initial_data/` | The starting data given by the course |
| `requirements.txt` | Python packages needed to run the script |

To redraw the charts, run:

```
pip install -r requirements.txt
python visualise_progress.py
```
