import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('svm_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Cancer Predictor", layout="centered")
st.title("🩺 Breast Cancer Risk Checker")
st.markdown("### Please fill the details below:")

# Friendly input labels (top 6 important features)
input_labels = {
    'mean radius': "Size of the lump (in mm)",
    'mean texture': "Texture of the lump",
    'mean concavity': "Indentation depth of the lump surface",
    'mean perimeter': "Boundary length of the lump",
    'mean compactness': "How tight the cells are grouped",
    'mean concave points': "Number of inward curves in the lump"
}

# Collect input
user_input = []
for key, label in input_labels.items():
    val = st.slider(label, min_value=0.0, max_value=40.0, step=0.1)
    user_input.append(val)

if st.button("🧪 Check Cancer Risk"):
    try:
        # Prepare input for model
        input_array = np.zeros((1, 30))  # Model expects 30 features
        feature_indices = {
            'mean radius': 0,
            'mean texture': 1,
            'mean perimeter': 2,
            'mean compactness': 5,
            'mean concavity': 6,
            'mean concave points': 7
        }
        for feature, value in zip(input_labels.keys(), user_input):
            index = feature_indices[feature]
            input_array[0, index] = value

        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]

        # Show result
        if prediction == 1:
            st.success("✅ The result suggests the lump is **Benign** (non-cancerous).")
        else:
            st.error("❗ The result suggests the lump might be **Malignant** (cancerous). Please consult a doctor.")
    except Exception as e:
        st.error(f"Error during prediction: {e}")

