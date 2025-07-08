📊 Customer Churn Prediction – Streamlit ML App
🔍 Project Description:
This project is a machine learning-based web application that predicts whether a customer is likely to churn (i.e., leave the service) based on their demographic, billing, and service usage data. The goal is to help telecom companies proactively identify at-risk customers and improve customer retention.

The project uses ensemble learning (Voting Classifier), combining the strengths of Random Forest, Gradient Boosting, and XGBoost, and is deployed using Streamlit for an interactive user interface.

🚀 Features:
Interactive Streamlit UI for real-time predictions

Accepts user inputs such as:

Contract type

Internet service

Monthly charges

Tenure

And many more

Predicts churn probability based on 19 customer features

Displays clear results: ✅ “Will Stay” or ⚠️ “Likely to Churn”

Deployed live using Streamlit Cloud

Easily extendable with new features or datasets

🧠 Machine Learning Details:
Dataset: Telco Customer Churn Dataset

Target variable: Churn (Yes/No)

Features: 19 (encoded + numerical)

Models used:

Logistic Regression (baseline)

Random Forest

Gradient Boosting

XGBoost

Voting Classifier (ensemble)

Accuracy Achieved: ~89% with ensemble

🗂️ Tech Stack:
Python

Pandas, NumPy, Scikit-learn, XGBoost

Streamlit for web deployment

GitHub for version control

Streamlit Cloud for hosting
