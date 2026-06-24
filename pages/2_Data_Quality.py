import streamlit as st

# Define application identity before rendering any UI.
st.set_page_config(
    page_title="InsightForge AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 InsightForge AI")

st.subheader(
    "Transform Raw Data into Actionable Business Decisions"
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Modules", "5")

with col2:
    st.metric("Supported Datasets", "Sales")

with col3:
    st.metric("Version", "1.0 MVP")

st.markdown("## Platform Workflow")

st.markdown(
    """
    📤 Upload Dataset

    ↓

    🛡️ Assess Data Quality

    ↓

    📊 Generate Business Analytics

    ↓

    📈 Forecast Future Performance

    ↓

    🧠 Produce Executive Recommendations
    """
)