import streamlit as st
import requests

st.title("Student Score Predictor")

hours = st.number_input("Hours Studied", min_value=0, max_value=24)
attendance = st.number_input("Attendance Percentage", min_value=0, max_value=100)

if st.button("predict"):
    response = requests.post("http://127.0.0.1:8000/predict",
                              json={"hours": hours, "attendance": attendance})
    result = response.json()
    st.write("Predicted Score:", result["predicted_score"])