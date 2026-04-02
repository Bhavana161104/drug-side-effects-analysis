import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("models/drug_model.pkl", "rb"))




import os
import pickle

model_path = os.path.join("models", "drug_model.pkl")

model = pickle.load(open(model_path, "rb"))





# Page config
st.set_page_config(page_title="Drug Side Effects Dashboard", layout="centered")

# Title
st.title("💊 Drug Side Effects Prediction Dashboard")
st.markdown("### Analyze drug sentiment based on user data")

# Sidebar
st.sidebar.header("Input Features")

useful_count = st.sidebar.slider("Useful Count", 0, 1000, 10)
condition = st.sidebar.number_input("Condition Encoded", min_value=0, value=1)

# Main section
st.subheader("🔍 Prediction")

if st.button("Predict Sentiment"):
    prediction = model.predict([[useful_count, condition]])

    if prediction[0] == "Positive":
        st.success("✅ Positive Sentiment (Safe Drug)")
    elif prediction[0] == "Neutral":
        st.warning("⚠️ Neutral Sentiment")
    else:
        st.error("❌ Negative Sentiment (Possible Side Effects)")

# Info section
st.markdown("---")
st.subheader("📊 About Project")

st.write("""
- This model predicts drug sentiment using machine learning.
- Sentiment categories:
  - Positive → Safe
  - Neutral → Moderate
  - Negative → Risky
""")

import pandas as pd

data = pd.DataFrame({
    "Feature": ["Useful Count", "Condition"],
    "Value": [useful_count, condition]
})

st.subheader("📈 Input Visualization")
st.bar_chart(data.set_index("Feature"))





# Footer
st.markdown("---")
st.markdown("👩‍💻 Developed by Bhavana Thota")