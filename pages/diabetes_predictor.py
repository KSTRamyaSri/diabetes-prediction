import streamlit as st
import streamlit.components.v1 as components
import joblib
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time

st.set_page_config(page_title="💜 Diabetes Risk Predictor", layout="centered")

def show_dashboard():
    # Title
    st.markdown("""
    <h2 style='text-align:center;color:#6C29A9;margin-top:24px;'>💜 Diabetes Risk Predictor</h2>
    <p style='text-align:center;color:#7B5FC0;'>Enter your details below to assess your diabetes risk.</p>
    """, unsafe_allow_html=True)

    # ---------------------- FORM ----------------------
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    if not st.session_state.submitted:
        form_html = """
        <div class="wrapper">
        <div class="form-card">
            <h3>Health Information</h3>
            <label>Gender:</label>
            <select id="gender">
              <option value="Female">Female</option>
              <option value="Male">Male</option>
            </select>
            <div id="pregnancyDiv">
              <label>Pregnancies:</label>
              <input type="number" id="pregnancies" min="0" max="20" step="1" placeholder="e.g. 2">
            </div>
            <label>Glucose:</label>
            <input type="number" id="glucose" min="0" max="200" step="1" placeholder="e.g. 120">
            <label>Blood Pressure:</label>
            <input type="number" id="bp" min="0" max="140" step="1" placeholder="e.g. 70">
            <label>Skin Thickness:</label>
            <input type="number" id="skin" min="0" max="99" step="1" placeholder="e.g. 20">
            <label>Insulin:</label>
            <input type="number" id="insulin" min="0" max="900" step="1" placeholder="e.g. 80">
            <label>BMI:</label>
            <input type="number" id="bmi" min="0" max="80" step="0.1" placeholder="e.g. 25.4">
            <label>Diabetes Pedigree Function:</label>
            <input type="number" id="dpf" min="0" max="2.5" step="0.01" placeholder="e.g. 0.5">
            <label>Age:</label>
            <input type="number" id="age" min="18" max="120" step="1" placeholder="e.g. 35">
            <button id="predictBtn">Predict</button>
        </div></div>

        <style>
        .wrapper{display:flex;justify-content:center;margin-top:30px;}
        .form-card{
          background: rgba(255,255,255,0.8);
          backdrop-filter: blur(12px);
          padding: 30px 40px;
          border-radius: 20px;
          box-shadow: 0 6px 24px rgba(171, 124, 255, 0.3);
          width: 340px;
          animation: fadeIn 1s ease;
        }
        h3{text-align:center;color:#6C29A9;margin-bottom:12px;}
        label{display:block;color:#6C29A9;margin-top:8px;font-weight:600;}
        input, select{
          width:100%;padding:8px;margin-top:5px;border-radius:10px;
          border:1px solid #d6b6eb;outline:none;text-align:center;
        }
        button{
          margin-top:16px;width:100%;
          background:linear-gradient(90deg,#7B5FC0,#FFC5E6);
          color:white;font-weight:700;font-size:16px;border:none;
          border-radius:14px;padding:10px;cursor:pointer;transition:0.2s;
          box-shadow:0 4px 18px rgba(171,124,255,0.3);
        }
        button:hover{transform:scale(1.05);}
        @keyframes fadeIn{from{opacity:0;transform:translateY(20px);}to{opacity:1;transform:translateY(0);}}
        </style>

        <script>
          const genderSelect=document.getElementById("gender");
          const pregnancyDiv=document.getElementById("pregnancyDiv");
          genderSelect.addEventListener("change",()=>{
              pregnancyDiv.style.display=genderSelect.value==="Female"?"block":"none";
          });
          document.getElementById("predictBtn").addEventListener("click",()=>{
              const data={
                  gender:document.getElementById("gender").value,
                  pregnancies:parseInt(document.getElementById("pregnancies").value||0),
                  glucose:parseFloat(document.getElementById("glucose").value),
                  bp:parseFloat(document.getElementById("bp").value),
                  skin:parseFloat(document.getElementById("skin").value),
                  insulin:parseFloat(document.getElementById("insulin").value),
                  bmi:parseFloat(document.getElementById("bmi").value),
                  dpf:parseFloat(document.getElementById("dpf").value),
                  age:parseInt(document.getElementById("age").value)
              };
              Streamlit.setComponentValue(data);
          });
        </script>
        """
        data = components.html(form_html, height=950)

        if isinstance(data, dict):
            st.session_state.form_data = data
            st.session_state.submitted = True
            st.rerun()

    # ---------------------- PREDICTION ----------------------
    elif st.session_state.submitted:
        st.markdown("<div style='text-align:center;'><div class='loader'></div><p>Predicting...</p></div>", unsafe_allow_html=True)
        st.markdown("""
        <style>
        .loader {
          border: 5px solid #f3f3f3;
          border-top: 5px solid #9b63f8;
          border-radius: 50%;
          width: 60px;
          height: 60px;
          animation: spin 1s linear infinite;
          margin: 0 auto;
        }
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
        </style>
        """, unsafe_allow_html=True)

        time.sleep(2.5)  # simulate loading

        try:
            model = joblib.load('models/models/diabetes_rf.pkl')
            scaler = joblib.load('models/models/diabetes_scaler.pkl')
        except FileNotFoundError:
            st.error("⚠️ Model files not found!")
            return

        data = st.session_state.form_data
        user_data = np.array([[data['pregnancies'], data['glucose'], data['bp'],
                               data['skin'], data['insulin'], data['bmi'],
                               data['dpf'], data['age']]])
        user_data_scaled = scaler.transform(user_data)
        prediction = model.predict(user_data_scaled)[0]

        st.session_state.prediction = prediction
        st.session_state.submitted = "done"
        st.rerun()

    # ---------------------- RESULTS ----------------------
    elif st.session_state.submitted == "done":
        data = st.session_state.form_data
        prediction = st.session_state.prediction

        if prediction == 1:
            st.markdown("<h3 style='text-align:center;color:#e93b7a;'>🚨 You are at Risk of Diabetes</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='text-align:center;color:#4CC68A;'>💚 No Diabetes Detected</h3>", unsafe_allow_html=True)

        # ----- Radar Chart -----
        features = ['Pregnancies', 'Glucose', 'BP', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age']
        values = [data['pregnancies'], data['glucose'], data['bp'], data['skin'], data['insulin'], data['bmi'], data['dpf'], data['age']]
        values += values[:1]
        angles = np.linspace(0, 2 * np.pi, len(features), endpoint=False).tolist()
        angles += angles[:1]

        fig = plt.figure(figsize=(5, 5))
        plt.polar(angles, values, color='#A850E8', linewidth=2)
        plt.fill(angles, values, color='#A195F7', alpha=0.25)
        plt.xticks(angles[:-1], features, color='#6C29A9', fontsize=9)
        plt.title('Feature Radar', color='#6C29A9', fontsize=14)
        st.pyplot(fig, clear_figure=True)

        # ----- Plotly Gauge Chart -----
        risk = np.mean(values) / 100
        fig2 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk * 100,
            title={'text': "Health Risk Index"},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': "#A850E8"},
                   'steps': [
                       {'range': [0, 50], 'color': "#BFFFCF"},
                       {'range': [50, 75], 'color': "#FFF3C0"},
                       {'range': [75, 100], 'color': "#FFD1D1"}],
                   }))
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("""
        <div style='text-align:center;margin-top:30px;'>
        <button onclick="window.location.reload()" 
        style='background:linear-gradient(90deg,#7B5FC0,#FFC5E6);border:none;padding:10px 18px;
        border-radius:14px;color:white;font-weight:bold;cursor:pointer;'>🔁 Test Again</button>
        </div>
        """, unsafe_allow_html=True)


# Run dashboard
show_dashboard()
