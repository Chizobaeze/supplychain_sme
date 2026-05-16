import streamlit as st

from src.data_loader import load_data
from src.preprocessing import preprocess

from src.visualisation import (
    loan_volume_chart,
    default_trend_chart,
    sector_chart,
    credit_score_chart
)

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

st.title("📊 SME Credit Analytics Dashboard")

raw_df = load_data()

df = preprocess(raw_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Loans",
    len(df)
)

col2.metric(
    "Default Rate",
    f"{df['default_180d'].mean()*100:.2f}%"
)

col3.metric(
    "Average Credit Score",
    f"{df['credit_score'].mean():.0f}"
)

col4.metric(
    "High Risk Loans",
    int(df['default_180d'].sum())
)

st.divider()

chart1, chart2 = st.columns(2)

with chart1:

    st.plotly_chart(
        loan_volume_chart(raw_df),
        use_container_width=True
    )

with chart2:

    st.plotly_chart(
        default_trend_chart(raw_df),
        use_container_width=True
    )

st.divider()

chart3, chart4 = st.columns(2)

with chart3:

    st.plotly_chart(
        sector_chart(raw_df),
        use_container_width=True
    )

with chart4:

    st.plotly_chart(
        credit_score_chart(raw_df),
        use_container_width=True
    )