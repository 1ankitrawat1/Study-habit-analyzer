
import streamlit as st
import pandas as pd
import plotly.express as px

from data_manager import load_data, save_entry
from analyzer import analyze_data

st.set_page_config(page_title="Study Optimizer", page_icon="📚", layout="wide")

st.title("📊 Study Optimizer")
st.caption("Data-driven study performance analyzer for students")
st.divider()

# Input section
st.sidebar.header("Add Study Entry")

date = st.sidebar.date_input("Date")
subject = st.sidebar.text_input("Subject")
hours = st.sidebar.number_input("Study Hours", min_value=0.0, max_value=24.0, step=0.5)
focus = st.sidebar.slider("Focus Level", 1, 5)

if st.sidebar.button("Save Entry"):
    if subject.strip() == "":
        st.sidebar.warning("Enter subject name")
    else:
        save_entry(date, subject, hours, focus)
        st.sidebar.success("Entry saved!")

# Load data
df = load_data()

st.header("Study Data")
st.dataframe(df)

st.divider()

# Analysis
result = analyze_data(df)

if result:
    st.header("Overall Analysis")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Hours", result["total_hours"])
    col2.metric("Avg Hours", result["avg_hours"])
    col3.metric("Consistency", result["consistency"])
    col4.metric("Productivity Score", f'{result["productivity_score"]}/100') 
    st.divider()
    
    
    
#    daily study hours by subject 
    df["date"] = pd.to_datetime(df["date"])

    date_subject = (
    df.groupby(["date", "subject"])["hours"]
    .sum()
    .reset_index()
    )

    st.subheader("📊 Date-wise Study by Subject")
    
    fig = px.bar(
    date_subject,
    x="date",
    y="hours",
    color="subject",
    barmode="group",
    title="Daily Study Hours by Subject"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.divider()

# focus vs study time
    st.subheader("🎯 Focus vs Study Time")

    fig_focus = px.scatter(
    df,
    x="hours",
    y="focus",
    color="subject",
    size="hours",
    title="Focus Efficiency Analysis"
    )

    st.plotly_chart(fig_focus, use_container_width=True)
    st.divider()


# subject-wise study time
    st.subheader("Subject-wise Study Time")
    st.bar_chart(result["subject_summary"])
    st.divider()



    st.subheader("Insights")
    st.success(f'Most studied subject: {result["top_subject"]}')
    st.divider()


    st.subheader("Recommendation")
    st.info(result["tip"])
else:
    st.warning("Add study data to see analysis.")