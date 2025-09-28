# 🚓 SecureCheck: A Python-SQL Digital Ledger for Police Post Logs  

## 📌 Project Overview  
**SecureCheck** is a centralized digital logging and monitoring system designed for **police check posts**.  
It uses **Python, SQL, and Streamlit** to modernize vehicle stop logging, real-time monitoring, and violation tracking.  
The system replaces manual record-keeping with a **digital ledger** that ensures **fast, accurate, and actionable insights** for law enforcement.  

---

## 🎯 Problem Statement  
Police check posts currently rely on **manual logging and inefficient databases**, which slows down operations and reduces the effectiveness of security checks.  

This project builds an **SQL-powered check post database** with a **Python + Streamlit dashboard** for:  
- Real-time log entries  
- Automated suspect vehicle identification  
- Data-backed crime analysis  
- Efficient monitoring across multiple locations  

---

## 🚀 Business Use Cases  
- ✅ Real-time logging of vehicles and personnel  
- ✅ Automated suspect vehicle identification using SQL queries  
- ✅ Efficiency monitoring through analytics (stop duration, officer activity)  
- ✅ Crime pattern analysis (age, race, gender, violation-based)  
- ✅ Centralized database for multi-location check posts  

---

## 🛠️ Approach  

### 🔹 Step 1: Python for Data Processing  
- Remove columns containing only missing values  
- Handle `NaN` values  
- Clean and preprocess driver age, violations, and stop outcomes  

### 🔹 Step 2: Database Design (SQL)  
- Create SQL schema for storing **stop records**  
- Insert cleaned dataset into MySQL/PostgreSQL  

### 🔹 Step 3: Streamlit Dashboard  
- Display vehicle logs, violations, and officer reports  
- Implement **SQL-based search filters**  
- Generate analytics & trends (high-risk vehicles, drug-related stops, arrests by location)  

---

## 📊 Example Record  
> A **27-year-old male driver** was stopped for **Speeding** at **2:30 PM**.  
> No search was conducted, and he received a citation.  
> The stop lasted **6-15 minutes** and was **not drug-related**.  

---

## 📈 Results  
- 🚀 Faster check post operations using SQL queries  
- 🚨 Automated alerts for flagged vehicles  
- 📡 Real-time reporting of violations & arrests  
- 📊 Data-driven decision making for law enforcement  

---

## 📐 Project Evaluation Metrics  
- ⚡ **Query Execution Time** → Optimized SQL queries for fast lookups  
- ✅ **Data Accuracy** → Ensure correct log entries & flagged reports  
- 📶 **System Uptime** → Real-time updates without lag  
- 👮 **User Engagement** → Officer interaction with dashboard  
- 🔎 **Violation Detection Rate** → % of flagged vehicles identified  

---

## 🗂️ Dataset Explanation  

| Column              | Description |
|---------------------|-------------|
| stop_date           | Date of the stop |
| stop_time           | Time of the stop |
| country_name        | Location of stop |
| driver_gender       | Gender of driver |
| driver_age_raw      | Recorded age before cleaning |
| driver_age          | Cleaned driver age |
| driver_race         | Driver’s race/ethnicity |
| violation_raw       | Raw reason for stop |
| violation           | Cleaned violation type |
| search_conducted    | Whether a search was conducted |
| search_type         | Type of search conducted |
| stop_outcome        | Outcome (Warning, Citation, Arrest) |
| is_arrested         | Arrest status |
| stop_duration       | Duration of stop |
| drugs_related_stop  | Whether drug-related |

---

## 🧑‍💻 SQL Queries  

### 🔹 Vehicle-Based  
- Top 10 vehicles in drug-related stops  
- Most frequently searched vehicles  

### 🔹 Demographic-Based  
- Age group with highest arrest rate  
- Gender distribution of drivers by country  
- Race & gender combination with highest search rate  

### 🔹 Time & Duration Based  
- Time of day with most stops  
- Avg. stop duration by violation  
- Night vs day arrest likelihood  

### 🔹 Violation-Based  
- Violations most associated with arrests  
- Common violations among drivers <25  
- Violations rarely leading to arrest  

### 🔹 Location-Based  
- Country with highest drug-related stops  
- Arrest rate by country & violation  
- Country with most searches conducted  

### 🔹 Complex Analysis  
- Yearly breakdown of stops & arrests (Subquery + Window Functions)  
- Driver violation trends (Joins + Subqueries)  
- Time analysis (Year, Month, Hour breakdown)  
- Violations with highest arrest/search rates  
- Demographics by country (age, gender, race)  
- Top 5 violations with highest arrest rates  

---

## 🖥️ Tech Stack  

- **Python** → Data preprocessing (Pandas, SQLAlchemy)  
- **SQL (MySQL / PostgreSQL / SQLite)** → Centralized storage & queries  
- **Streamlit** → Interactive dashboard for officers  
- **Matplotlib / Plotly** → Visual analytics  

---

## 📦 Project Deliverables  
- ✅ SQL Database Schema (MySQL/PostgreSQL)  
- ✅ Python Scripts for Data Cleaning & Processing  
- ✅ Streamlit Dashboard for Real-time Monitoring  
- ✅ Automated SQL Reports & Logs  
- ✅ Documentation for Usage  

---

## 📂 Repository Structure  

