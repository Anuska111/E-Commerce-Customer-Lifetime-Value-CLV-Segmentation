import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained model
model = joblib.load("clv_model.pkl")

st.set_page_config(
    page_title="Customer Lifetime Value Prediction",
    page_icon="🛒",
    layout="centered"
)

st.title("🛍️ E-Commerce Customer Lifetime Value Prediction")
st.write("Enter customer details to predict Customer Lifetime Value (CLV).")

# Input fields
recency = st.number_input("Recency (Days)", min_value=0, value=30)
frequency = st.number_input("Frequency", min_value=0, value=5)
monetary = st.number_input("Monetary Value", min_value=0.0, value=5000.0)

# Predict
if st.button("Predict CLV"):
    input_df = pd.DataFrame({
        "Recency": [recency],
        "Frequency": [frequency],
        "Monetary": [monetary],
        "LogFrequency": [np.log1p(frequency)],
        "LogRecency": [np.log1p(recency)]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Customer Lifetime Value: ₹ {prediction:,.2f}")
