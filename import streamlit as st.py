import streamlit as st
import joblib
import pandas as pd

# load model
model = joblib.load("model.pkl")

st.title("🎓 Student Performance Prediction")

# inputs
age = st.number_input("Age")
gender = st.selectbox("Gender", ["male", "female"])
school_type = st.selectbox("School Type", ["public", "private"])
parent_education = st.selectbox("Parent Education", ["high_school", "graduate"])
study_hours = st.number_input("Study Hours")
attendance = st.number_input("Attendance %")
internet = st.selectbox("Internet Access", ["yes", "no"])
travel_time = st.selectbox("Travel Time", ["<15 min", "15-30 min", "30-60 min", ">60 min"])
extra = st.selectbox("Extra Activities", ["yes", "no"])
study_method = st.selectbox("Study Method", ["group", "solo"])
math = st.number_input("Math Score")
science = st.number_input("Science Score")
english = st.number_input("English Score")
overall = st.number_input("Overall Score")

if st.button("Predict"):
    data = pd.DataFrame([{
        "student_id": 1,
        "age": age,
        "gender": gender,
        "school_type": school_type,
        "parent_education": parent_education,
        "study_hours": study_hours,
        "attendance_percentage": attendance,
        "internet_access": internet,
        "travel_time": travel_time,
        "extra_activities": extra,
        "study_method": study_method,
        "math_score": math,
        "science_score": science,
        "english_score": english,
        "overall_score": overall
    }])

    prediction = model.predict(data)[0]

    st.success(f"🎯 Predicted Grade: {prediction}")