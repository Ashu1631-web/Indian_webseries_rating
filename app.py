import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Web Series Visualization Dashboard",
    page_icon="🎬",
    layout="wide"
)

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("indian_webseries_ratings.csv")

df = load_data()
series_list = df.columns[1:]

# -------------------------------
# Title
# -------------------------------
st.title("🎬 Web Series Ratings Dashboard")
st.markdown("### 📊 Professional Multi-Chart Analytics with Insights")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🎛 Filters")

selected_series = st.sidebar.selectbox("Select Web Series", series_list)

ratings = df[selected_series].dropna()

# -------------------------------
# Download Feature
# -------------------------------
st.sidebar.subheader("⬇ Download Data")

st.download_button(
    label="📥 Download Dataset CSV",
    data=df.to_csv(index=False),
    file_name="webseries_ratings.csv",
    mime="text/csv"
)

# -------------------------------
# KPI Metrics
# -------------------------------
st.subheader("📌 Key Insights")

avg_rating = ratings.mean()
max_rating = ratings.max()
min_rating = ratings.min()

col1, col2, col3 = st.columns(3)

col1.metric("⭐ Average Rating", round(avg_rating, 2))
col2.metric("🔥 Highest Rating", round(max_rating, 2))
col3.metric("⚡ Lowest Rating", round(min_rating, 2))

st.info(
    f"Insight: **{selected_series}** has an average rating of "
    f"**{round(avg_r_**
