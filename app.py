import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("bike_price_model.pkl")
encoder = joblib.load("label_encoder.pkl")

st.title("🛵 Used Bike Price Predictor")

# Input fields
bike_name = st.text_input("Bike Name", "TVS Star City Plus Dual Tone 110cc")
city = st.selectbox("City", ["Ahmedabad", "Bangalore", "Chennai", "Delhi", "Hyderabad", "Mumbai", "Pune"])
kms_driven = st.number_input("Kilometers Driven", value=15000.0)
owner = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner"])
age = st.number_input("Age of Bike (in years)", value=3.0)
power = st.number_input("Power (cc)", value=110.0)
brand = st.selectbox("Brand", ["TVS", "Honda", "Bajaj", "Yamaha", "Hero"])

# Predict
if st.button("Predict Price"):
    input_df = pd.DataFrame([[bike_name, city, kms_driven, owner, age, power, brand]],
                            columns=['bike_name', 'city', 'kms_driven', 'owner', 'age', 'power', 'brand'])

    # Encode categorical features
    for col in ['bike_name', 'city', 'owner', 'brand']:
        input_df[col] = encoder.fit_transform(input_df[col])

    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Price: ₹{prediction:,.2f}")