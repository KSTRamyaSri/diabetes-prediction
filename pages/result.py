import streamlit as st
import joblib
import numpy as np

def show_dashboard_result():
    if 'diabetes_input' not in st.session_state:
        st.warning("Please fill the input form first!")
        return

    data = st.session_state['diabetes_input']

    with st.spinner("Predicting your diabetes risk... ⏳"):
        model = joblib.load('models/models/diabetes_rf.pkl')
        scaler = joblib.load('models/models/diabetes_scaler.pkl')

        user_data = np.array([[data['pregnancies'], data['glucose'], data['bp'],
                               data['skin'], data['insulin'], data['bmi'],
                               data['dpf'], data['age']]])
        user_data_scaled = scaler.transform(user_data)
        prediction = model.predict(user_data_scaled)[0]

    color = "#e93b7a" if prediction == 1 else "#58c988"
    message = "You are at risk of Diabetes!" if prediction == 1 else "No Diabetes detected — keep healthy habits!"

    st.markdown(f"""
    <div style='text-align:center; padding:20px; color:{color}; background:#f3eaff; border-radius:12px; margin-top:20px; font-weight:bold;'>
        {message}
    </div>
    """, unsafe_allow_html=True)
