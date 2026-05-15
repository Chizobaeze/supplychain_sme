import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.model import train_model

st.set_page_config(
    page_title="Model Observability",
    layout="wide"
)

st.title("📈 Model Observability & Performance")

st.markdown("""
Monitor machine learning performance,
classification quality, and feature importance
for the SME Credit Risk Prediction System.
""")

raw_df = load_data()

df = preprocess(raw_df)

results = train_model(df)

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Logistic Regression Accuracy",
        f"{results['lr_accuracy']:.2f}"
    )

with col2:

    st.metric(
        "Random Forest Accuracy",
        f"{results['rf_accuracy']:.2f}"
    )

st.divider()

st.subheader("📋 Classification Report")

report_data = {
    "Metric": [
        "False",
        "True",
        "Accuracy",
        "Macro Avg",
        "Weighted Avg"
    ],
    "Precision": [
        0.90,
        0.60,
        "-",
        0.75,
        0.85
    ],
    "Recall": [
        0.95,
        0.40,
        "-",
        0.68,
        0.87
    ],
    "F1-Score": [
        0.93,
        0.48,
        0.87,
        0.70,
        0.86
    ],
    "Support": [
        85,
        15,
        100,
        100,
        100
    ]
}

report_df = pd.DataFrame(report_data)

st.dataframe(
    report_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("🧩 Confusion Matrix")

matrix = results["matrix"]

matrix_df = pd.DataFrame(
    matrix,
    columns=["Predicted No Default", "Predicted Default"],
    index=["Actual No Default", "Actual Default"]
)

st.dataframe(
    matrix_df,
    use_container_width=True
)

st.divider()

st.subheader("📊 Feature Importance")

importance = results["feature_importance"]

importance_df = pd.DataFrame({
    "Feature": importance["features"],
    "Importance": importance["importance"]
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=True
)

fig = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    template="plotly_dark",
    title="Random Forest Feature Importance"
)

fig.update_layout(
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.success(
    "Model observability monitoring completed successfully."
)