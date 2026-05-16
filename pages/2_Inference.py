import streamlit as st

from src.model import predict_risk

st.set_page_config(layout="wide")

st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background-color: #161B22 !important;
    color: white !important;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Credit Risk Inference Engine")

st.markdown("""
Input SME financial information below
to predict whether the business
is likely to default after 180 days.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    business_sector = st.selectbox(
        "Business Sector",
        [0, 1, 2, 3, 4]
    )

    business_state = st.selectbox(
        "Business State",
        [0, 1, 2, 3, 4]
    )

    years = st.slider(
        "Years in Business",
        0,
        30,
        5
    )

    revenue = st.number_input(
        "Annual Revenue (NGN)",
        value=500000
    )

    employees = st.slider(
        "Employees",
        1,
        500,
        10
    )

with col2:

    principal = st.number_input(
        "Loan Amount (NGN)",
        value=100000
    )

    interest = st.slider(
        "Interest Rate",
        1.0,
        40.0,
        12.0
    )

    tenor = st.slider(
        "Loan Tenor",
        1,
        60,
        12
    )

    lender = st.selectbox(
        "Lender",
        [0, 1, 2, 3]
    )

    collateral = st.number_input(
        "Collateral Value",
        value=100000
    )

    credit_score = st.slider(
        "Credit Score",
        300,
        850,
        650
    )

st.divider()

if st.button("Predict Credit Risk"):

    features = [
        business_sector,
        business_state,
        years,
        revenue,
        employees,
        principal,
        interest,
        tenor,
        lender,
        collateral,
        credit_score
    ]

    prediction = predict_risk(features)

    if prediction == 1:

        st.error(
            "⚠️ HIGH CREDIT RISK — Business likely to default"
        )

    else:

        st.success(
            "✅ LOW CREDIT RISK — Business likely to repay"
        )