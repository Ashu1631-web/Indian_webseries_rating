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

fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(top10.index, top10.values)
ax1.set_title("Top 10 Web Series Ratings")
ax1.set_ylabel("Average Rating")
plt.xticks(rotation=45)

st.pyplot(fig1)

# -------------------------------
# LINE GRAPH
# -------------------------------
st.subheader("📈 Line Graph (Trend Over Users)")

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(ratings.values[:30], marker="o")
ax2.set_title(f"Line Trend for {selected_series}")
ax2.set_xlabel("Users")
ax2.set_ylabel("Ratings")

st.pyplot(fig2)

# -------------------------------
# PIE CHART
# -------------------------------
st.subheader("🥧 Pie Chart (Ratings Distribution)")

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
    title=f"Pie Distribution for {selected_series}"
)
st.plotly_chart(fig3)

# -------------------------------
# HISTOGRAM
# -------------------------------
st.subheader("📊 Histogram (Frequency Distribution)")

fig4 = px.histogram(
    ratings,
    nbins=10,
    title=f"Histogram of Ratings for {selected_series}"
)
st.plotly_chart(fig4)

# -------------------------------
# SCATTER PLOT
# -------------------------------
st.subheader("🔵 Scatter Plot (Correlation Between Two Series)")

series_x = st.selectbox("Select X-Axis Series", series_list, index=0)
series_y = st.selectbox("Select Y-Axis Series", series_list, index=1)

scatter_df = df[[series_x, series_y]].dropna()

fig5 = px.scatter(
    scatter_df,
    x=series_x,
    y=series_y,
    title=f"Scatter Plot: {series_x} vs {series_y}"
)
st.plotly_chart(fig5)

# -------------------------------
# AREA CHART
# -------------------------------
st.subheader("🌊 Area Chart (Cumulative Trend)")

fig6 = px.area(
    ratings.head(30),
    title=f"Area Chart for {selected_series}"
)
st.plotly_chart(fig6)

# -------------------------------
# BOX PLOT
# -------------------------------
st.subheader("📦 Box Plot (Outliers & Distribution)")

fig7 = px.box(
    ratings,
    title=f"Box Plot for {selected_series}"
)
st.plotly_chart(fig7)

# -------------------------------
# BUBBLE CHART
# -------------------------------
st.subheader("🫧 Bubble Chart (Multi-Dimensional View)")

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
    title="Bubble Chart: Popularity vs Ratings"
)
st.plotly_chart(fig8)

# -------------------------------
# HEATMAP BONUS
# -------------------------------
st.subheader("🔥 Heatmap (Correlation Between Series)")

corr = df[series_list].corr()

fig9, ax9 = plt.subplots(figsize=(12, 6))
sns.heatmap(corr, cmap="coolwarm", ax=ax9)

st.pyplot(fig9)

# -------------------------------
# Preview Dataset
# -------------------------------
st.subheader("📂 Dataset Preview")
st.dataframe(df.head())

st.success("✅ Complete Visualization Dashboard Ready!")
