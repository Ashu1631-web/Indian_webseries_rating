import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Animated Web Series Dashboard",
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
st.title("🎬 Animated Web Series Ratings Dashboard")
st.markdown("### Professional Dashboard with Insights + Colors + Animation")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("🎛 Controls")

selected_series = st.sidebar.selectbox("Select Web Series", series_list)

ratings = df[selected_series].dropna()

# -------------------------------
# KPI Insights
# -------------------------------
st.subheader("📌 Key Insights")

avg_rating = round(ratings.mean(), 2)
max_rating = round(ratings.max(), 2)
min_rating = round(ratings.min(), 2)

col1, col2, col3 = st.columns(3)
col1.metric("⭐ Average Rating", avg_rating)
col2.metric("🔥 Highest Rating", max_rating)
col3.met
