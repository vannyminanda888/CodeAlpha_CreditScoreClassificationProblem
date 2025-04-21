# Credit Score Classification Model

This project was developed as part of my online internship program in **Machine Learning**. The goal was to build a supervised classification model that predicts an individual's **credit score** category — **High**, **Average**, or **Low** — based on a set of socio-economic features.

## 🎯 Objective

To predict the credit score category of individuals using machine learning, based on:

- Age
- Gender
- Income
- Education Level
- Marital Status
- Number of Children
- Home Ownership Status

## 🧠 Problem Statement

Credit scoring is a crucial part of financial services, helping institutions assess an individual’s creditworthiness. This project focuses on classifying individuals into credit score bands using structured data. The classifier helps automate decision-making for lending or offering financial products.

## 💡 Solution Approach

1. **Data Preprocessing**:
   - Handling missing values
   - Encoding categorical variables (e.g., gender, education)
   - Normalizing numerical features

2. **Exploratory Data Analysis (EDA)**:
   - Feature distribution
   - Correlation analysis
   - Class balance visualization

3. **Modeling**:
   - Trained multiple classifiers (e.g., Logistic Regression, Random Forest, XGBoost)
   - Hyperparameter tuning using GridSearchCV
   - Selected the best-performing model based on accuracy, precision, recall, and F1-score

4. **Evaluation**:
   - Confusion matrix and classification report
   - ROC curves

## 📊 Results

- Achieved **TBU** on the test dataset
- Best model: TBU
- Model performance remained consistent across all credit score categories

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook

## 🚀 How to Run

Clone the repo and install the dependencies:

```bash
git clone https://github.com/vannyminanda888/CodeAlpha_CreditScoreClassificationProblem.git
cd CodeAlpha_CreditScoreClassificationProblem
pip install -r requirements.txt
