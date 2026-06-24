import streamlit as st

# Define application identity before any UI renders.
# Streamlit requires this to be the first Streamlit command.
st.set_page_config(
    page_title="InsightForge AI",
    page_icon=":📊:",
    layout="wide",
)
st.title("📊 InsightForge AI")
st.subheader("Transform Raw Data into Actionable Business Decisions")
st.divider()
st.markdown(
    """
    Welcome to InsightForge AI! This application is designed to help you analyze and visualize your data effectively. 
    Whether you're looking to generate insights, create reports, or make data-driven decisions, InsightForge AI has got you covered.
    
    **Features:**
    - Data Upload: Easily upload your datasets in various formats.
    - Data Cleaning: Preprocess and clean your data for better analysis.
    - Visualization: Create interactive charts and graphs to visualize your data.
    - Insights Generation: Use AI-powered tools to extract meaningful insights from your data.
    
    Get started by uploading your dataset and exploring the powerful features of InsightForge AI!
    ### Overview

    InsightForge AI helps organizations:

    - Assess Data Quality
    - Analyze Business Performance
    - Forecast Future Revenue
    - Generate Executive Insights

    ### Workflow

    Upload Dataset
    → Data Quality Assessment
    → Analytics
    → Forecasting
    → Executive Recommendations
    """
)
