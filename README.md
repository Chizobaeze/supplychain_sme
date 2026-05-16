# SME Credit Risk Prediction System

A Streamlit-based supply chain finance prototype for SME credit risk assessment. This app loads a synthetic Nigerian SME loan dataset, builds and compares machine learning models, and delivers:

- Interactive analytics dashboard
- Credit risk inference engine
- Model observability and performance monitoring
- Loan and default trend visualisations

## Project Structure

- `Home.py` - Main landing page for the Streamlit app.
- `pages/1_Dashboard.py` - Analytics dashboard with loan volume, default trends, sector counts, and credit score distribution.
- `pages/2_Inference.py` - Credit risk inference engine for real-time loan default prediction.
- `pages/3_Observability.py` - Model evaluation and observability page showing accuracy, confusion matrix, and feature importance.
- `src/data_loader.py` - Loads the `electricsheepafrica/africa-synth-banking-sme-loans-nigeria` dataset.
- `src/preprocessing.py` - Applies simple label encoding to categorical features.
- `src/model.py` - Trains Logistic Regression and Random Forest models, saves the best model, and performs predictions.
- `src/visualisation.py` - Builds Plotly charts for dashboard analytics.

## Features

- Load and preprocess SME loan data
- Train and compare Logistic Regression and Random Forest classifiers
- Save best model as `credit_risk_model.pkl`
- Predict default risk from business, loan, and borrower inputs
- Display model performance metrics and feature importance
- Visualize portfolio and credit risk trends

## Requirements

This project uses the following Python libraries:

- streamlit
- pandas
- scikit-learn
- joblib
- datasets
- plotly

## Installation

1. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

1. Install dependencies:

```bash
pip install streamlit pandas scikit-learn joblib datasets plotly
```

## Running the App

From the project root, run:

```bash
streamlit run Home.py
```

Then open the local URL shown in the terminal.

## Usage

- Use the sidebar to navigate between the dashboard, inference engine, and observability pages.
- In the `Inference` page, provide SME and loan details to predict default risk after 180 days.
- In `Observability`, review model accuracy, classification report, confusion matrix, and feature importance.

## Notes

- The dataset is loaded from the Hugging Face `electricsheepafrica/africa-synth-banking-sme-loans-nigeria` dataset.
- The app currently uses a subset of the dataset (`head(1000)`) for faster local loading.
- The saved model file is `credit_risk_model.pkl`.
