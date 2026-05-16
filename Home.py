import streamlit as st

st.set_page_config(
    page_title="SME Credit Risk System",
    page_icon="🏦",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3, h4 {
    color: white;
}

.stMetric {
    background-color: #161B22;
    padding: 15px;
    border-radius: 10px;
}

section[data-testid="stSidebar"] {
    background-color: #161B22;
    color: white;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🏦 SME Credit Risk Prediction System")

st.markdown("""
### AI-powered supply chain finance risk assessment platform for SME lending decisions.
""")

st.divider()

st.header("📌 Project Overview")

st.write("""
This project uses Machine Learning and Data Analytics
to evaluate SME loan applications and predict
the likelihood of loan default after 180 days.

The application provides:

- SME loan analytics dashboard
- Credit risk monitoring
- Machine learning inference engine
- Model observability and evaluation
- Interactive financial visualisations

The platform was developed as a fintech-focused
credit intelligence prototype for SME lending decisions.
""")

st.divider()

st.header("🧠 Machine Learning Models")

st.write("""
The project compares multiple machine learning algorithms:

- Logistic Regression
- Random Forest Classifier

The best-performing model is automatically selected
and saved for real-time prediction.
""")

st.divider()

st.header("📊 Dataset Information")

st.write("""
Dataset Source:
electricsheepafrica/africa-synth-banking-sme-loans-nigeria

Dataset Features Include:

- Business sector
- Business state
- Annual revenue
- Number of employees
- Loan principal
- Interest rate
- Collateral value
- Credit score
- Default indicators

Target Variables:

- default_90d
- default_180d
""")

st.divider()

st.header("🚀 System Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    📊 Dashboard Analytics
    
    - Loan trends
    - Default trends
    - Credit score analytics
    - Sector analysis
    """)

with col2:
    st.success("""
    🧠 AI Inference Engine
    
    - Real-time prediction
    - Risk classification
    - Loan risk evaluation
    - Financial assessment
    """)

with col3:
    st.warning("""
    📈 Model Observability
    
    - Accuracy monitoring
    - Feature importance
    - Confusion matrix
    - Model comparison
    """)

st.divider()

st.success("Use the sidebar navigation to explore the application.")