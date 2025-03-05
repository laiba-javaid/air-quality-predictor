import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model/AirQualityPredictor.sav", "rb"))

# Streamlit UI
st.markdown("""
    <h1 style='text-align: center;'>🌍 Air Quality Predictor</h1>
    <p style='text-align: center;'>Enter air quality parameters to predict AQI (Air Quality Index).</p>
""", unsafe_allow_html=True)
# User inputs
pm25 = st.number_input("PM2.5 Level", min_value=0.0, step=0.1)
pm10 = st.number_input("PM10 Level", min_value=0.0, step=0.1)
no = st.number_input("NO Level", min_value=0.0, step=0.1)
no2 = st.number_input("NO2 Level", min_value=0.0, step=0.1)
nox = st.number_input("NOx Level", min_value=0.0, step=0.1)
nh3 = st.number_input("NH3 Level", min_value=0.0, step=0.1)
so2 = st.number_input("SO2 Level", min_value=0.0, step=0.1)
co = st.number_input("CO Level", min_value=0.0, step=0.1)
o3 = st.number_input("O3 Level", min_value=0.0, step=0.1)


# Predict AQI on button click
if st.button("Predict AQI"):
    # Convert input to DataFrame
    input_data = pd.DataFrame([[pm25, pm10, no, no2, nox, nh3, so2, co, o3]], 
                               columns=['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'SO2', 'CO', 'O3'])
    
    # Predict AQI
    predicted_aqi = model.predict(input_data)[0]

    # Display result in dialog box
    st.success(f"🌟 Predicted AQI: {predicted_aqi:.2f}")
