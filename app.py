from cmath import pi
from operator import ge
import re
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
data = pickle.load(open('data.pkl', 'rb'))

st.title('Heart Disease Predictor')

age = st.number_input('Enter Person age:')

gender = st.selectbox('Gender', ['Male','Female'])

chest_pain = st.selectbox('Chest pain type', ['Typical Angina', 'Atypical Angina', 'Non-anginal pain', 'Aymptomatic'])

rbp = st.number_input("Enter resting blood pressure value")

chol = st.number_input("Enter cholestoral value")

fbs = st.selectbox("Fasting blood sugar >120mg/dl", ['Yes','No'])

restecg = st.selectbox('Select restecg phase',['Normal', 'ST - T', 'hypertrophy'])

thal = st.number_input("Enter maximum heart rate achieved:")

slope = st.selectbox("Slope of peak exercise segment",['low','medium','high'])

if st.button('Predict'):

    if gender == 'Male':
        gender = 1
    else:
        gender = 0


    if chest_pain == 'Typical Angina':
        chest_pain = 0
    elif chest_pain == 'Atypical Angina':
        chest_pain = 1
    elif chest_pain == 'Non-anginal pain':
        chest_pain = 2
    else:
        chest_pain = 3


    if fbs == "Yes":
        fbs = 1
    else:
        fbs = 0


    if restecg == 'Normal':
        restecg = 0
    elif restecg == 'ST - T':
        restecg = 1
    else:
        restecg = 2

    if slope == 'low':
        slope = 0
    elif slope == 'medium':
        slope = 1
    else:
        slope = 2


    query = np.array([age, gender, chest_pain, rbp, chol, fbs, restecg, thal, slope])
    query = query.reshape(1,9)
    x = model.predict(query)
    if(x[0]==0):
        st.title('You have a healthy heart')
    else:
        st.title('You need to consult a doctor')

