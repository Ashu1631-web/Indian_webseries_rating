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
    page_icon="📊",
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
st.title("📊 Complete Data Visualization Dashboard")
st.markdown("### All Graph Types in One Professional Streamlit App")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🎛 Filters")

selected_series = st.sidebar.selectbox("Select Web Series", series_list)

# Ratings Data
ratings = df[selected_series].dropna()

# -------------------------------
# Download Feature
# -------------------------------
st.sidebar.subheader("⬇ Download Data")

st.download_button(
    label="📥 Download Full Dataset CSV",
    data=df.to_csv(index=False),
    file_name="webseries_ratings.csv",
    mime="text/csv"
)

# -------------------------------
# BAR GRAPH
# -------------------------------
st.subheader("📊 Bar Graph (Category Comparison)")

top10 = df[series_list].mean().sort_values(ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.bar(top10.index, top10.values)
ax1.set_title("Top 10 Web Series Ratings")
ax1.set_ylabel("Average Rating")
plt.xticks(rotation=45)
st.pyplot(fig1)

# -------------------------------
# LINE GRAPH
# -------------------------------
st.subheader("📈 Line Graph (Trend Over Users)")

fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(ratings.values[:30], marker="o")
ax2.set_title(f"Line Trend for {selected_seri
