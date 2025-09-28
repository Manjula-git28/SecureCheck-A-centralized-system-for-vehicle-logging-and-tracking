import streamlit as st
import pandas as pd
import plotly.express as px

# =============================
# Page Config
# =============================
st.set_page_config(
    page_title="SecureCheck: Police Post Dashboard",
    layout="wide",
    page_icon="🚓"
)

# =============================
# Load Data
# =============================
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\manjula\Downloads\traffic_stops - traffic_stops_with_vehicle_number (1).csv")
    return df

df = load_data()

# =============================
# Sidebar Navigation
# =============================
st.sidebar.title("🔐 SecureCheck")
menu = st.sidebar.radio("Navigate", ["Dashboard", "Add Police Log", "Advanced Insights"])

# =============================
# Dashboard (KPIs + Charts)
# =============================
if menu == "Dashboard":
    st.title("🚓 Police Check Post Dashboard")

    # KPIs
    total_stops = len(df)
    total_searches = df[df["search_conducted"] == 1].shape[0]
    total_arrests = df[df["stop_outcome"].str.contains("Arrest", case=False, na=False)].shape[0]
    drug_related = df[df["drugs_related_stop"] == 1].shape[0]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Stops", total_stops)
    col2.metric("Total Searches", total_searches)
    col3.metric("Total Arrests", total_arrests)
    col4.metric("Drug-Related Stops", drug_related)

    # Chart Example
    st.subheader("📊 Driver Gender Distribution")
    gender_chart = df["driver_gender"].value_counts().reset_index()
    gender_chart.columns = ["Gender", "Count"]
    fig = px.pie(gender_chart, names="Gender", values="Count", title="Driver Gender Distribution")
    st.plotly_chart(fig, use_container_width=True)

# =============================
# Add Police Log (Form)
# =============================
elif menu == "Add Police Log":
    st.title("📝 Add New Police Log & Predict Violation")

    with st.form("log_form"):
        stop_date = st.date_input("Stop Date")
        stop_time = st.time_input("Stop Time")
        county_name = st.text_input("County Name")
        driver_gender = st.selectbox("Driver Gender", ["male", "female"])
        driver_age = st.number_input("Driver Age", min_value=16, max_value=100, step=1)
        driver_race = st.text_input("Driver Race")
        search_conducted = st.selectbox("Was a Search Conducted?", [0, 1])
        search_type = st.text_input("Search Type")
        drugs_related = st.selectbox("Was it Drug Related?", [0, 1])
        stop_duration = st.selectbox("Stop Duration", ["0-15 Min", "16-30 Min", "30+ Min"])
        vehicle_number = st.text_input("Vehicle Number")

        submitted = st.form_submit_button("✅ Submit Log")

    if submitted:
        st.success("Police log has been submitted! (Future: save to DB & run ML prediction)")

# =============================
# Advanced Insights
# =============================
elif menu == "Advanced Insights":
    st.title("📊 Advanced Insights")

    query = st.selectbox("Select a Query", [
        "Top 5 Most Frequent Search Types",
        "Top 10 Vehicles in Drug-Related Stops",
        "Driver Age Group with Highest Arrest Rate"
    ])

    if st.button("Run Query"):
        if query == "Top 5 Most Frequent Search Types":
            result = df["search_type"].value_counts().head(5).reset_index()
            result.columns = ["Search Type", "Count"]
            st.dataframe(result)
            st.bar_chart(result.set_index("Search Type"))

        elif query == "Top 10 Vehicles in Drug-Related Stops":
            result = df[df["drugs_related_stop"] == 1]["vehicle_number"].value_counts().head(10).reset_index()
            result.columns = ["Vehicle Number", "Count"]
            st.dataframe(result)
            st.bar_chart(result.set_index("Vehicle Number"))

        elif query == "Driver Age Group with Highest Arrest Rate":
            df["age_group"] = pd.cut(df["driver_age"], bins=[0,18,30,45,60,100], labels=["<18","18-30","31-45","46-60","60+"])
            arrests = df[df["stop_outcome"].str.contains("Arrest", case=False, na=False)]
            result = arrests["age_group"].value_counts().reset_index()
            result.columns = ["Age Group", "Arrest Count"]
            st.dataframe(result)
            st.bar_chart(result.set_index("Age Group"))
