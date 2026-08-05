**Module 5 Capstone Component 5.1 – Analysing How Data Splitting Affects Model Performance**

This notebook explores how different data splitting strategies affect the performance of a machine learning model. The experiment is part of the Professional Certificate in Machine Learning and AI at Imperial College London Business School.

**Dataset**

The Wine dataset from scikit-learn is used in this notebook. It contains 178 samples with 13 chemical features, classified into three wine categories.

**What this notebook does**

The notebook runs two experiments using Logistic Regression on the same dataset, with the only variable being the data split ratio.

Experiment 1 uses a 60:20:20 split (training, validation, test). This gave a validation accuracy of 94.44% and a test accuracy of 97.22%.

Experiment 2 uses a 70:15:15 split. This gave a validation accuracy of 100% and a test accuracy of 96.30%. The 100% validation score is discussed in the notebook as a potentially misleading result due to the small validation set size.

**Key finding**

A larger validation and test set produces a more reliable estimate of how the model will perform on unseen data. More training data does not always lead to better generalisation.

**Libraries used**

scikit-learn, Python 3

**How to run**

Open the notebook in Google Colab or any Jupyter environment and run all cells in order.
