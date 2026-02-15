import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Web Series Ratings Dashboard",
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
st.title("Web Series Ratings Dashboard")
st.write("Professional Data Visualization Dashboard with Insights")

# -------------------------------
# Sidebar Filter
# -------------------------------
st.sidebar.header("Dashboard Controls")

selected_series = st.sidebar.selectbox("Select Web Series", series_list)
ratings = df[selected_series].dropna()

# -------------------------------
# KPI Metrics
# -------------------------------
st.subheader("Key Insights Summary")

avg_rating = round(ratings.mean(), 2)
max_rating = round(ratings.max(), 2)
min_rating = round(ratings.min(), 2)

col1, col2, col3 = st.columns(3)
col1.metric("Average Rating", avg_rating)
col2.metric("Highest Rating", max_rating)
col3.metric("Lowest Rating", min_rating)

st.info(
    "Insight: Ratings range from "
    + str(min_rating)
    + " to "
    + str(max_rating)
    + " with an average of "
    + str(avg_rating)
)

# -------------------------------
# Bar Chart
# -------------------------------
st.subheader("Bar Chart: Top 10 Web Series")

top10 = df[series_list].mean().sort_values(ascending=False).head(10)

bar_df = pd.DataFrame({
    "Series": top10.index,
    "AvgRating": top10.values
})

fig1 = px.bar(
    bar_df,
    x="Series",
    y="AvgRating",
    color="Series",
    title="Top Rated Web Series"
)

st.plotly_chart(fig1, use_container_width=True)
st.success("Insight: This chart shows the highest rated web series overall.")

# -------------------------------
# Line Chart
# -------------------------------
st.subheader("Line Chart: User Rating Trend")

trend_df = pd.DataFrame({
    "UserIndex": list(range(1, len(ratings[:30]) + 1)),
    "Rating": ratings.values[:30]
})

fig2 = px.line(
    trend_df,
    x="UserIndex",
    y="Rating",
    markers=True,
    title="Rating Trend Over Users"
)

st.plotly_chart(fig2, use_container_width=True)
st.warning("Insight: Ratings fluctuate across different users.")

# -------------------------------
# Pie Chart
# -------------------------------
st.subheader("Pie Chart: Ratings Distribution")

pie_df = pd.DataFrame({
    "
