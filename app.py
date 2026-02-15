import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Web Series Ratings Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("indian_webseries_ratings.csv")

df = load_data()
series_list = df.columns[1:]

st.title("Web Series Ratings Dashboard")
st.write("Professional Data Visualization Dashboard with Insights")

st.sidebar.header("Dashboard Controls")
selected_series = st.sidebar.selectbox("Select Web Series", series_list)
ratings = df[selected_series].dropna()

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

st.subheader("Bar Chart: Top 10 Web Series")

top10 = df[series_list].mean().sort_values(ascending=False).head(10)

bar_df = pd.DataFrame({"Series": top10.index, "AvgRating": top10.values})

fig1 = px.bar(bar_df, x="Series", y="AvgRating", color="Series", title="Top Rated Web Series")
st.plotly_chart(fig1, use_container_width=True)
st.success("Insight: This chart shows the highest rated web series overall.")

st.subheader("Line Chart: User Rating Trend")

trend_df = pd.DataFrame({
    "UserIndex": list(range(1, len(ratings[:30]) + 1)),
    "Rating": ratings.values[:30]
})

fig2 = px.line(trend_df, x="UserIndex", y="Rating", markers=True, title="Rating Trend Over Users")
st.plotly_chart(fig2, use_container_width=True)
st.warning("Insight: Ratings fluctuate across different users.")

st.subheader("Pie Chart: Ratings Distribution")

pie_df = pd.DataFrame({
    "Category": ["Low (0-3)", "Medium (4-7)", "High (8-10)"],
    "Count": [
        (ratings <= 3).sum(),
        ((ratings > 3) & (ratings <= 7)).sum(),
        (ratings > 7).sum()
    ]
})

fig3 = px.pie(pie_df, names="Category", values="Count", title="Ratings Breakdown", hole=0.4)
st.plotly_chart(fig3, use_container_width=True)
st.info("Insight: Most ratings fall in Medium or High category.")

st.subheader("Histogram: Ratings Frequency")

fig4 = px.histogram(ratings, nbins=10, title="Ratings Frequency Histogram")
st.plotly_chart(fig4, use_container_width=True)
st.success("Insight: Histogram shows most common rating values.")

st.subheader("Scatter Plot: Compare Two Series")

series_x = st.selectbox("Select X Series", series_list, index=0)
series_y = st.selectbox("Select Y Series", series_list, index=1)

scatter_df = df[[series_x, series_y]].dropna()

fig5 = px.scatter(scatter_df, x=series_x, y=series_y, title="Scatter Plot Relationship")
st.plotly_chart(fig5, use_container_width=True)
st.warning("Insight: Scatter plot shows correlation between two series.")

st.subheader("Box Plot: Outliers and Spread")

fig6 = px.box(ratings, title="Box Plot Distribution")
st.plotly_chart(fig6, use_container_width=True)
st.success("Insight: Box plot identifies rating spread and outliers.")

st.subheader("Bubble Chart: Popularity vs Rating")

bubble_df = pd.DataFrame({
    "Series": series_list,
    "AvgRating": df[series_list].mean(),
    "TotalRatings": df[series_list].count()
})

fig7 = px.scatter(
    bubble_df,
    x="TotalRatings",
    y="AvgRating",
    size="AvgRating",
    color="Series",
    hover_name="Series",
    title="Bubble Chart of Web Series"
)

st.plotly_chart(fig7, use_container_width=True)
st.info("Insight: Bigger bubbles represent higher rated and popular series.")

st.sidebar.subheader("Download Dataset")

st.download_button(
    label="Download Full CSV",
    data=df.to_csv(index=False),
    file_name="webseries_ratings.csv",
    mime="text/csv"
)

st.success("Dashboard Loaded Successfully!")
