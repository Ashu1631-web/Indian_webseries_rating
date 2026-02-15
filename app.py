import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Web Series Ratings Dashboard",
    page_icon="🎬",
    layout="wide"
)

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("indian_webseries_ratings.csv")
    return df

df = load_data()

st.title("🎬 Indian Web Series Ratings Dashboard")
st.markdown("Professional Streamlit Analytics App with Charts & Trends")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🎛 Dashboard Filters")

series_list = df.columns[1:]
selected_series = st.sidebar.selectbox("Select Web Series", series_list)

# -------------------------------
# KPI Metrics
# -------------------------------
st.subheader("📌 Key Insights")

avg_rating = df[selected_series].mean()
total_users = df.shape[0]

top_series = df[series_list].mean().idxmax()
top_rating = df[series_list].mean().max()

col1, col2, col3 = st.columns(3)
col1.metric("⭐ Average Rating", round(avg_rating, 2))
col2.metric("👥 Total Users", total_users)
col3.metric("🏆 Top Series", f"{top_series} ({round(top_rating,2)})")

# -------------------------------
# Bar Chart: Top Rated Series
# -------------------------------
st.subheader("📊 Top Rated Web Series (Bar Chart)")

series_avg = df[series_list].mean().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
ax.bar(series_avg.index, series_avg.values)
plt.xticks(rotation=45)
plt.ylabel("Average Rating")

st.pyplot(fig)

# -------------------------------
# Pie Chart: Rating Distribution
# -------------------------------
st.subheader("🥧 Ratings Distribution (Pie Chart)")

ratings = df[selected_series].dropna()

labels = ["Low (0-3)", "Medium (4-7)", "High (8-10)"]
sizes = [
    (ratings <= 3).sum(),
    ((ratings > 3) & (ratings <= 7)).sum(),
    (ratings > 7).sum()
]

fig2, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct="%1.1f%%")

st.pyplot(fig2)

# -------------------------------
# Heartwave Chart (Trend Line)
# -------------------------------
st.subheader("💓 Heartwave Rating Trend")

user_ratings = ratings.head(30)

fig3, ax3 = plt.subplots()
ax3.plot(user_ratings.values, marker="o")
plt.title(f"Heartwave Trend for {selected_series}")
plt.xlabel("Users")
plt.ylabel("Ratings")

st.pyplot(fig3)

# -------------------------------
# Dataset Preview
# -------------------------------
st.subheader("📂 Dataset Preview")
st.dataframe(df.head())

st.success("✅ Dashboard Loaded Successfully!")
