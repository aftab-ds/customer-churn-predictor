import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("📞 Telco Customer Churn Prediction")
st.write("Enter customer details below to predict whether they are likely to churn.")

# User Input Fields
gender = st.selectbox("Gender", ['Male', 'Female'])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner", ['Yes', 'No'])
dependents = st.selectbox("Has Dependents", ['Yes', 'No'])
tenure = st.slider("Tenure (months)", 0, 72, 12)
phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
multiple_lines = st.selectbox("Multiple Lines", ['No phone service', 'No', 'Yes'])
internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox("Online Security", ['No', 'Yes', 'No internet service'])
online_backup = st.selectbox("Online Backup", ['No', 'Yes', 'No internet service'])
contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
paperless = st.selectbox("Paperless Billing", ['Yes', 'No'])
payment = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly = st.number_input("Monthly Charges ($)", 0.0, 150.0, 70.0)
total = st.number_input("Total Charges ($)", 0.0, 10000.0, 1500.0)
device_protection = st.selectbox("Device Protection", ['No', 'Yes', 'No internet service'])
tech_support = st.selectbox("Tech Support", ['No', 'Yes', 'No internet service'])
streaming_tv = st.selectbox("Streaming TV", ['No', 'Yes', 'No internet service'])
streaming_movies = st.selectbox("Streaming Movies", ['No', 'Yes', 'No internet service'])


# Label Encoding (must match training)
def encode_inputs():
    mapping = {
        'Yes': 1, 'No': 0,
        'Male': 1, 'Female': 0,
        'No internet service': 2,
        'No phone service': 2,
        'DSL': 0, 'Fiber optic': 1, 'No': 2,
        'Month-to-month': 0, 'One year': 1, 'Two year': 2,
        'Electronic check': 0, 'Mailed check': 1,
        'Bank transfer (automatic)': 2, 'Credit card (automatic)': 3
    }

    return [
        mapping[gender],                   # gender
        senior,                            # SeniorCitizen
        mapping[partner],                  # Partner
        mapping[dependents],               # Dependents
        tenure,                            # tenure
        mapping[phone_service],            # PhoneService
        mapping[multiple_lines],           # MultipleLines
        mapping[internet_service],         # InternetService
        mapping[online_security],          # OnlineSecurity
        mapping[online_backup],            # OnlineBackup
        mapping[device_protection],        # DeviceProtection
        mapping[tech_support],             # TechSupport
        mapping[streaming_tv],             # StreamingTV
        mapping[streaming_movies],         # StreamingMovies
        mapping[contract],                 # Contract
        mapping[paperless],                # PaperlessBilling
        mapping[payment],                  # PaymentMethod
        monthly,                           # MonthlyCharges
        total                              # TotalCharges
    ]

# Predict
if st.button("Predict"):
    input_data = np.array([encode_inputs()])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ The customer is likely to churn.")
    else:
        st.success("✅ The customer is likely to stay.")
