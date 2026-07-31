import streamlit as st
import numpy as np
import pickle

# load model
pickle.load(open(r"C:\Users\muham\Downloads\model.pkl", "rb"))

st.title("🧬 Cancer Prediction App")

st.write("Enter 30 features:")

inputs = []

for i in range(30):
    val = st.number_input(f"Feature {i+1}", step=0.01)
    inputs.append(val)

if st.button("Predict"):
    data = np.array(inputs).reshape(1, -1)
    prediction = model.predict(data)

    if prediction[0] == 0:
        st.error("❌ Malignant (Cancer Detected)")
    else:
        st.success("✅ Benign (No Cancer)")