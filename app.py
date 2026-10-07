import streamlit as st
import joblib
import numpy as np
import panda as pd
# Load the pre-trained model
model = joblib.load(r"C:\Users\ASUS\OneDrive\Desktop\House Price Prediction\model.pkl")

# Title of the app
st.title("House Price Prediction App")

st.divider()

# Description of the app
st.write("This app uses machine learning for predicting house prices based on given features of the house. You can enter the inputs below, then click the 'Predict' button to get the estimated house price.")

st.divider()

# Input fields for the user
Bedrooms = st.number_input("Number of bedrooms you want", min_value=0, value=0)
Bathrooms = st.number_input("Number of bathrooms you want", min_value=0, value=0)
LivingArea = st.number_input("Living Area (sq ft)", min_value=0, value=2000)
LotArea = st.number_input("Lot Area (sq ft)", min_value=0, value=5000)  # Added Lot Area input
Floors = st.number_input("Number of floors", min_value=0.0, value=1.5, step=0.1)
Condition = st.number_input("Condition (1=poor, 5=excellent)", min_value=1, max_value=5, value=3)  # Set valid range
Number_oF_Schools = st.number_input("Number of schools nearby", min_value=0, value=0)
Distance_from_Airport = st.number_input("Distance from the airport (miles)", min_value=0.0, value=5.0)  # Added Distance from Airport input
Area_Excluding_Basement = st.number_input("Area of the house (excluding basement) (sq ft)", min_value=0, value=1500)  # Added Area Excluding Basement input
Area_Basement = st.number_input("Area of the basement (sq ft)", min_value=0, value=500)  # Added Area of Basement input

st.divider()

# Predict button
Predict_Button = st.button("Predict!")

if Predict_Button:
    st.balloons()  
    
    # Prepare the input array in the correct order
    x = np.array([[Bedrooms, Bathrooms, LivingArea, LotArea, Floors, Condition, Area_Excluding_Basement, Area_Basement, Number_oF_Schools, Distance_from_Airport]])

    # Make prediction
    prediction = model.predict(x)

    # Display the predicted house price
    st.write(f"Predicted House Price: ${prediction[0]:,.2f}")
    
else:
    st.write("Please enter the values and click 'Predict!' to get the price prediction.")
