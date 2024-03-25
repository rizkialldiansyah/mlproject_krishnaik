import streamlit as st
import json
import requests
import pandas as pd

df = pd.read_csv("artifacts/data.csv")

st.title("Math Score Prediction.")

# CATEGORY INPUT
gender = st.selectbox('Gender', df['gender'].unique())
race_ethnicity = st.selectbox('Race Ethnicity', df['race_ethnicity'].unique())
parental_level_of_education = st.selectbox('Parental Level of Education', df['parental_level_of_education'].unique())
lunch = st.selectbox('Lunch', df['lunch'].unique())
test_preparation_course = st.selectbox('Test Preparation Course', df['test_preparation_course'].unique())

# NUMBER INPUT
writing_score = st.slider('Writing Score', 0, 100, 50)
reading_score = st.slider('Reading Score', 0, 100, 50)

# CONVER INPUT TO JSON
inputs = {
    'gender': gender,
    'race_ethnicity': race_ethnicity,
    'parental_level_of_education': parental_level_of_education,
    'lunch': lunch,
    'test_preparation_course': test_preparation_course,
    'reading_score': reading_score,
    'writing_score': writing_score}

if st.button('Calculate'):
    res = requests.post(url="http://127.0.0.1:8000/predict", data=json.dumps(inputs))
    result = res.json()
    st.subheader(f"Your math score is: {result['math_score_predicted']}")


