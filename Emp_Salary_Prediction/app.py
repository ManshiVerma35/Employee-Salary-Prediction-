import streamlit as st
import joblib
import numpy as np

st.title("Salary Predicition Application")

st.divider()


st.write("With this app, you can get estimations for the salaries of the company employees")

years = st.number_input("Enter the years at company",value = 1, step = 1, min_value = 0)
jobrate = st.number_input("Enter the job rate",value = 3.5 , step = 0.5, min_value = 0.0)

x = [years, jobrate]

model = joblib.load("linearmodel.pkl")

st.divider()

predict = st.button("press the button for salary prediction")

st.divider()

if predict: 

    st.balloons()

    x1 = np.array([x])

    prediction = model.predict(x1)[0]
    
    st.write(f"Salary predicition is {prediction:,.2f}")


else: 
    "Please press the button for app to make the prediction"










