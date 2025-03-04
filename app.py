import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model/AirQualityPredictor.sav", "rb"))

# Streamlit UI
st.markdown("""
    <h1 style='text-align: center;'>🌍 Air Quality Predictor</h1>
    <p style='text-align: center;'>Enter air quality parameters to predict AQI.</p>
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

# Centered button
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Predict AQI"):
    # Convert input to DataFrame
    input_data = pd.DataFrame([[pm25, pm10, no, no2, nox, nh3, so2, co, o3]], 
                               columns=['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'SO2', 'CO', 'O3'])
    
    # Predict AQI
    predicted_aqi = model.predict(input_data)[0]

    # Determine AQI Category
    if predicted_aqi <= 50:
        category = "✅ Good"
        color = "green"
    elif predicted_aqi <= 100:
        category = "🌿 Satisfactory / Moderate"
        color = "blue"
    elif predicted_aqi <= 200:
        category = "😷 Unhealthy for Sensitive Groups"
        color = "orange"
    elif predicted_aqi <= 300:
        category = "❌ Poor"
        color = "red"
    elif predicted_aqi <= 400:
        category = "🚨 Very Poor"
        color = "purple"
    else:
        category = "☠️ Severe / Hazardous"
        color = "black"

    # Display result with AQI category
    st.markdown(f"""
        <div style='text-align: center;'>
            <h2 style='color:{color};'>🌟 Predicted AQI: {predicted_aqi:.2f} ({category})</h2>
        </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
