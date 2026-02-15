import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Web Series Dashboard",
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
st.markdown("### 📊 Professional Multi-Chart Visualization with Insights")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🎛 Select Web Series")

selected_series = st.sidebar.selectbox("Choose Series", series_list)

ratings = df[selected_series].dropna()

# -------------------------------
# Download Dataset Button
# -------------------------------
st.sidebar.subheader("⬇ Download Dataset")

st.download_button(
    label="📥 Download CSV",
    data=df.to_csv(index=False),
    file_name="webseries_ratings.csv",
    mime="text/csv"
)

# -------------------------------
# KPI Metrics
# -------------------------------
st.subheader("📌 Key Insights")

avg_rating = round(ratings.mean(), 2)
max_rating = round(ratings.max(), 2)
min_rating = round(ratings.min(), 2)

col1, col2, col3 = st.columns(3)
col1.metric("⭐ Average", avg_rating)
col2.metric("🔥 Highest", max_rating)
col3.metric("⚡ Lowest", min_rating)

st.info("Insight: Ratings range from " + str(min_rating) +
        " to " + str(max_rating) +
        " with an average of " + str(avg_rating))

# -------------------------------
# BAR GRAPH
# -------------------------------
st.subheader("📊 Bar Graph: Top 10 Rated Series")

top10 = df[series_list].mean().sort_values(ascending=False).head(10)

fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(top10.index, top10.values, color="orange")
ax1.set_ylabel("Average Rating")
plt.xticks(rotation=45)

st.pyplot(fig1)
st.success("Insight: Bar chart shows top-rated web series overall.")

# -------------------------------
# LINE GRAPH
# -------------------------------
st.subheader("📈 Line Graph: Rating Trend")

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(ratings.values[:30], marker="o", color="green")
ax2.set_ylabel("Ratings")

st.pyplot(fig2)
st.warning("Insight: Line graph shows fluctuations in user ratings.")

# -------------------------------
# PIE CHART
# -------------------------------
st.subheader("🥧 Pie Chart: Rating Distribution")

dist = pd.DataFrame({
    "Category": ["Low (0-3)", "Medium (4-7)", "High (8-10)"],
    "Count": [
        (ratings <= 3).sum(),
        ((ratings > 3) & (ratings <= 7)).sum(),
        (ratings > 7).sum()
    ]
})

fig3 = px.pie(
    dist,
    names="Category",
    values="Count",
    title="Ratings Breakdown",
    color_discrete_sequence=px.colors.qualitative.Set2
)

st.plotly_chart(fig3)
st.info("Insight: Pie chart shows proportions of low/medium/high ratings.")

# -------------------------------
# HISTOGRAM
# -------------------------------
st.subheader("📊 Histogram: Frequency of Ratings")

fig4 = px.histogram(
    ratings,
    nbins=10,
    title="Ratings Frequency",
    color_discrete_sequence=["purple"]
)

st.plotly_chart(fig4)
st.success("Insight: Histogram shows most common rating values.")

# -------------------------------
# SCATTER PLOT
# -------------------------------
st.subheader("🔵 Scatter Plot: Compare Two Series")

series_x = st.selectbox("X-Axis Series", series_list, index=0)
series_y = st.selectbox("Y-Axis Series", series_list, index=1)

scatter_df = df[[series_x, series_y]].dropna()

fig5 = px.scatter(
    scatter_df,
    x=series_x,
    y=series_y,
    title="Scatter Relationship",
    color_discrete_sequence=["red"]
)

st.plotly_chart(fig5)
st.warning("Insight: Scatter plot shows correlation between two series.")

# -------------------------------
# AREA CHART
# -------------------------------
st.subheader("🌊 Area Chart: Cumulative Ratings Trend")

fig6 = px.area(
    ratings.head(30),
    title="Area Trend",
    color_discrete_sequence=["skyblue"]
)

st.plotly_chart(fig6)
st.info("Insight: Area chart highlights cumulative rating pattern.")

# -------------------------------
# BOX PLOT
# -------------------------------
st.subheader("📦 Box Plot: Outliers & Spread")

fig7 = px.box(
    ratings,
    title="Box Plot Distribution",
    color_discrete_sequence=["gold"]
)

st.plotly_chart(fig7)
st.success("Insight: Box plot detects outliers and rating spread.")

# -------------------------------
# BUBBLE CHART
# -------------------------------
st.subheader("🫧 Bubble Chart: Popularity vs Rating")

bubble_df = pd.DataFrame({
    "Series": series_list,
    "AvgRating": df[series_list].mean(),
    "TotalRatings": df[series_list].count()
})

fig8 = px.scatter(
    bubble_df,
    x="TotalRatings",
    y="AvgRating",
    size="AvgRating",
    hover_name="Series",
    title="Bubble Chart",
    color="AvgRating",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig8)
st.warning("Insight: Bigger bubbles represent higher rated series.")

# -------------------------------
# HEATMAP
# -------------------------------
st.subheader("🔥 Heatmap: Correlation Matrix")

corr = df[series_list].corr()

fig9, ax9 = plt.subplots(figsize=(12, 6))
sns.heatmap(corr, cmap="coolwarm", ax=ax9)

st.pyplot(fig9)
st.info("Insight: Heatmap shows similarity between web series ratings.")

# -------------------------------
# Dataset Preview
# -------------------------------
st.subheader("📂 Dataset Preview")
st.dataframe(df.head())

st.success("✅ Dashboard Completed Successfully!")
