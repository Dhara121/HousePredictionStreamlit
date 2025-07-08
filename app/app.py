import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import joblib
from src.preprocess import preprocess_data

# Load model and expected features
model = joblib.load("models/house_price_model.pkl")
expected_features = joblib.load("models/feature_columns.pkl")

# 🔷 Styling & Title
st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B;'>🏡 House Price Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# 🔹 Input Form
with st.form("prediction_form"):
    st.subheader("Enter Property Details:")

    col1, col2 = st.columns(2)

    with col1:
        overall_qual = st.slider("Overall Quality (1–10)", 1, 10, 5)
        gr_liv_area = st.number_input("Ground Living Area (sq ft)", 500, 6000, 1500)
        garage_cars = st.slider("Garage Cars Capacity", 0, 5, 1)

    with col2:
        total_bsmt_sf = st.number_input("Basement Area (sq ft)", 0, 3000, 800)
        year_built = st.number_input("Year Built", 1900, 2023, 2000)
        lot_frontage = st.number_input("Lot Frontage (ft)", 20, 150, 60)

    neighborhood = st.selectbox(
        "Neighborhood",
        ['NAmes', 'CollgCr', 'OldTown', 'Somerst', 'NridgHt', 'Sawyer', 'NoRidge', 'Mitchel', 'Gilbert']
    )

    submitted = st.form_submit_button("🔍 Predict Price")

# 🔮 Prediction Logic
if submitted:
    input_df = pd.DataFrame([{
        "OverallQual": overall_qual,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt_sf,
        "YearBuilt": year_built,
        "LotFrontage": lot_frontage,
        "Neighborhood": neighborhood
    }])

    # One-hot encode Neighborhood
    input_df = pd.get_dummies(input_df, columns=["Neighborhood"])

    # Add missing columns
    for col in expected_features:
        if col not in input_df.columns:
            input_df[col] = 0

    # Ensure correct order
    input_df = input_df[expected_features]

    # Predict
    predicted_price = model.predict(input_df)[0]

    # Stylish result box
    st.markdown(f"""
    <div style="padding: 1.5rem; background-color: #f0f2f6; border-radius: 10px; border-left: 8px solid #FF4B4B;">
        <h3>💰 Estimated Sale Price</h3>
        <h2 style="color: #FF4B4B;">${predicted_price:,.0f}</h2>
    </div>
    """, unsafe_allow_html=True)
