import pandas as pd
import plotly.express as px


def loan_volume_chart(df):

    data = df.copy()

    data["application_date"] = pd.to_datetime(
        data["application_date"]
    )

    data["month"] = (
        data["application_date"]
        .dt.to_period("M")
        .astype(str)
    )

    monthly = (
        data.groupby("month")
        .size()
        .reset_index(name="Loans")
    )

    fig = px.line(
        monthly,
        x="month",
        y="Loans",
        title="Monthly Loan Volume Trend",
        markers=True,
        template="plotly_dark"
    )

    return fig


def default_trend_chart(df):

    data = df.copy()

    data["application_date"] = pd.to_datetime(
        data["application_date"]
    )

    data["month"] = (
        data["application_date"]
        .dt.to_period("M")
        .astype(str)
    )

    data["default_180d_int"] = (
        data["default_180d"]
        .astype(int)
    )

    trend = (
        data.groupby("month")["default_180d_int"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        trend,
        x="month",
        y="default_180d_int",
        title="Default Risk Trend",
        markers=True,
        template="plotly_dark"
    )

    return fig


def sector_chart(df):

    data = (
        df.groupby("business_sector")
        .size()
        .reset_index(name="Loans")
    )

    fig = px.bar(
        data,
        x="business_sector",
        y="Loans",
        title="Loans by Business Sector",
        template="plotly_dark"
    )

    return fig


def credit_score_chart(df):

    fig = px.histogram(
        df,
        x="credit_score",
        nbins=30,
        title="Credit Score Distribution",
        template="plotly_dark"
    )

    return fig