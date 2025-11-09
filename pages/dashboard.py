# import streamlit as st
# import joblib
# import numpy as np
# import time
# import plotly.graph_objects as go
# from streamlit_lottie import st_lottie
# import requests

# def main():
#     st.set_page_config(page_title="💜 Diabetes Risk Predictor", layout="centered", page_icon="💜")

#     # ---------------------- Helper functions ----------------------
#     def load_lottie_url(url):
#         r = requests.get(url)
#         if r.status_code != 200:
#             return None
#         return r.json()

#     # ---------------------- Session State ----------------------
#     if "submitted" not in st.session_state:
#         st.session_state.submitted = False
#     if "data" not in st.session_state:
#         st.session_state.data = {}

#     # ---------------------- Title ----------------------
#     st.markdown("<h2 style='text-align:center;color:#6C29A9;'>💜 Diabetes Risk Predictor</h2>", unsafe_allow_html=True)

#     # ---------------------- Form ----------------------
#     if not st.session_state.submitted:
#         gender = st.selectbox("Gender", ["Female", "Male"])
#         pregnancies = st.number_input("Pregnancies", 0, 20, 0) if gender == "Female" else 0
#         glucose = st.number_input("Glucose", 0, 200, 120)
#         bp = st.number_input("Blood Pressure", 0, 140, 70)
#         skin = st.number_input("Skin Thickness", 0, 99, 20)
#         insulin = st.number_input("Insulin", 0, 900, 80)
#         bmi = st.number_input("BMI", 0.0, 80.0, 25.4)
#         dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
#         age = st.number_input("Age", 18, 120, 35)

#         if st.button("Predict 💜"):
#             st.session_state.submitted = True
#             st.session_state.data = {
#                 "pregnancies": pregnancies,
#                 "glucose": glucose,
#                 "bp": bp,
#                 "skin": skin,
#                 "insulin": insulin,
#                 "bmi": bmi,
#                 "dpf": dpf,
#                 "age": age
#             }

#     # ---------------------- Prediction & Results ----------------------
#     if st.session_state.submitted:
#         # --- Loader animation using Lottie ---
#         lottie_url = "https://assets4.lottiefiles.com/packages/lf20_usmfx6bp.json"  # spinning loader
#         lottie_json = load_lottie_url(lottie_url)
#         if lottie_json:
#             st_lottie(lottie_json, height=150, key="loader")

#         time.sleep(2)  # simulate prediction delay

#         # --- Load model & scaler ---
#         model = joblib.load("models/models/diabetes_rf.pkl")
#         scaler = joblib.load("models/models/diabetes_scaler.pkl")

#         data = st.session_state.data
#         user_array = np.array([[data["pregnancies"], data["glucose"], data["bp"],
#                                 data["skin"], data["insulin"], data["bmi"],
#                                 data["dpf"], data["age"]]])
#         user_scaled = scaler.transform(user_array)
#         prediction = model.predict(user_scaled)[0]
#         prediction_proba = model.predict_proba(user_scaled)[0][1]*100  # risk percentage

#         # ---------------------- Gradient Card Result ----------------------
#         if prediction == 1:
#             st.markdown(f"""
#             <div style="background:linear-gradient(135deg,#FFB6B9,#E93B7A);padding:20px;border-radius:15px;">
#                 <h3 style='text-align:center;color:white;'>⚠️ High Risk of Diabetes</h3>
#                 <p style='text-align:center;color:white;font-size:16px;'>Risk Percentage: {prediction_proba:.1f}%</p>
#             </div>
#             """, unsafe_allow_html=True)
#         else:
#             st.markdown(f"""
#             <div style="background:linear-gradient(135deg,#B9FBC0,#3ECF8E);padding:20px;border-radius:15px;">
#                 <h3 style='text-align:center;color:white;'>✅ Low Risk of Diabetes</h3>
#                 <p style='text-align:center;color:white;font-size:16px;'>Risk Percentage: {prediction_proba:.1f}%</p>
#             </div>
#             """, unsafe_allow_html=True)

#         st.markdown("---")

#         # ---------------------- Plotly Gauge Chart ----------------------
#         gauge_fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=prediction_proba,
#             title={'text': "Diabetes Risk (%)"},
#             gauge={
#                 'axis': {'range': [0, 100]},
#                 'bar': {'color': "#E93B7A" if prediction_proba>50 else "#3ECF8E"},
#                 'steps': [
#                     {'range':[0,50],'color':'#B9FBC0'},
#                     {'range':[50,100],'color':'#FFB6B9'}
#                 ],
#                 'threshold': {'line': {'color': "black", 'width': 4}, 'value': prediction_proba}
#             }
#         ))
#         st.plotly_chart(gauge_fig)

#         # ---------------------- Bar Chart: Features vs Healthy ----------------------
#         features = ['Glucose','BP','BMI','Age']
#         values = [data['glucose'], data['bp'], data['bmi'], data['age']]
#         healthy = [120, 80, 25, 35]  # example healthy ranges

#         bar_fig = go.Figure()
#         bar_fig.add_trace(go.Bar(x=features, y=values, name="Your Values", marker_color='#A850E8'))
#         bar_fig.add_trace(go.Bar(x=features, y=healthy, name="Healthy Range", marker_color='#B9FBC0'))
#         bar_fig.update_layout(barmode='group', title="Health Metrics Comparison")
#         st.plotly_chart(bar_fig)

#         # ---------------------- Donut Chart: Risk Distribution ----------------------
#         donut_labels = ['Low Risk', 'High Risk']
#         donut_values = [100-prediction_proba, prediction_proba]
#         donut_fig = go.Figure(data=[go.Pie(labels=donut_labels, values=donut_values, hole=.5)])
#         donut_fig.update_traces(marker=dict(colors=['#3ECF8E','#E93B7A']))
#         donut_fig.update_layout(title="Diabetes Risk Distribution")
#         st.plotly_chart(donut_fig)

#         # ---------------------- Predict Again Button ----------------------
#         if st.button("🔄 Predict Again"):
#             st.session_state.submitted = False
#             st.session_state.data = {}

import streamlit as st
import joblib
import numpy as np
import time
import plotly.graph_objects as go


def main():

    st.set_page_config(page_title="💜 Diabetes Risk Predictor", layout="centered")

    # ---------------- Session State ----------------
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    if "data" not in st.session_state:
        st.session_state.data = {}
    if "predicted" not in st.session_state:
        st.session_state.predicted = False

    # ---------------- Title ----------------
    st.markdown("<h2 style='text-align:center;color:#6C29A9;'>💜 Diabetes Risk Predictor</h2>", unsafe_allow_html=True)

    # ---------------- Form ----------------
    if not st.session_state.submitted:
        gender = st.selectbox("Gender", ["Female", "Male"])
        pregnancies = st.number_input("Pregnancies", 0, 20, 0) if gender == "Female" else 0
        glucose = st.number_input("Glucose", 0, 200, 120)
        bp = st.number_input("Blood Pressure", 0, 140, 70)
        skin = st.number_input("Skin Thickness", 0, 99, 20)
        insulin = st.number_input("Insulin", 0, 900, 80)
        bmi = st.number_input("BMI", 0.0, 80.0, 25.4)
        dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
        age = st.number_input("Age", 18, 120, 35)

        if st.button("Predict 💜"):
            # store data and mark submitted
            st.session_state.submitted = True
            st.session_state.data = {
                "pregnancies": pregnancies,
                "glucose": glucose,
                "bp": bp,
                "skin": skin,
                "insulin": insulin,
                "bmi": bmi,
                "dpf": dpf,
                "age": age
            }
            st.rerun()  # rerun to show spinner

    # ---------------- Spinner & Prediction ----------------
    elif st.session_state.submitted and not st.session_state.predicted:
        # Spinner placeholder
        placeholder = st.empty()

        emoji_frames = ["🧬", "💉", "🍬", "⚡️", "❤️‍🔥", "🩺"]
        message_frames = ["Analyzing...", "Measuring Glucose...", "Calculating Risk...", "Almost Done..."]

        for i in range(12):
            emoji = emoji_frames[i % len(emoji_frames)]
            msg = message_frames[i % len(message_frames)]
            placeholder.markdown(
                f"""
                <div style='
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    height:60vh;
                    font-size:2rem;
                    color:#6C29A9;
                    font-weight:bold;
                '>
                    {emoji} {msg} {emoji}
                </div>
                """, unsafe_allow_html=True
            )
            time.sleep(0.3)

        placeholder.empty()  # remove spinner

        # --- Load model & scaler ---
        model = joblib.load("models/models/diabetes_rf.pkl")
        scaler = joblib.load("models/models/diabetes_scaler.pkl")

        data = st.session_state.data
        user_array = np.array([[data["pregnancies"], data["glucose"], data["bp"],
                                data["skin"], data["insulin"], data["bmi"],
                                data["dpf"], data["age"]]])
        user_scaled = scaler.transform(user_array)
        prediction = model.predict(user_scaled)[0]
        risk_percent = model.predict_proba(user_scaled)[0][1]*100
        accuracy = model.score(user_scaled, [prediction])*100

        st.session_state.prediction = prediction
        st.session_state.risk_percent = risk_percent
        st.session_state.accuracy = accuracy
        st.session_state.predicted = True
        st.rerun()  # rerun to show result

    # ---------------- Result ----------------
    elif st.session_state.predicted:
        prediction = st.session_state.prediction
        risk_percent = st.session_state.risk_percent
        accuracy = st.session_state.accuracy

        # Result card
        if prediction == 1:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#FFB6B9,#E93B7A);
                        padding:25px;border-radius:20px;box-shadow:0 8px 20px rgba(0,0,0,0.2);">
                <h3 style='text-align:center;color:white;'>⚠️ High Risk of Diabetes</h3>
                <p style='text-align:center;color:white;font-size:16px;'>Predicted Risk: {risk_percent:.1f}%</p>
                <p style='text-align:center;color:white;font-size:14px;'>Model Accuracy: {accuracy:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#B9FBC0,#3ECF8E);
                        padding:25px;border-radius:20px;box-shadow:0 8px 20px rgba(0,0,0,0.2);">
                <h3 style='text-align:center;color:white;'>✅ Low Risk of Diabetes</h3>
                <p style='text-align:center;color:white;font-size:16px;'>Predicted Risk: {risk_percent:.1f}%</p>
                <p style='text-align:center;color:white;font-size:14px;'>Model Accuracy: {accuracy:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)

        # Modern gauge
        gauge_fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=risk_percent,
            delta={'reference':50, 'increasing': {'color':'#E93B7A'}, 'decreasing':{'color':'#3ECF8E'}},
            title={'text': "Diabetes Risk (%)", 'font': {'size':24, 'color':'#6C29A9'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth':2, 'tickcolor':"#6C29A9"},
                'bar': {'color': "#E93B7A" if risk_percent>50 else "#3ECF8E", 'thickness':0.35},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#6C29A9",
                'steps': [
                    {'range':[0,50],'color':'#B9FBC0'},
                    {'range':[50,100],'color':'#FFB6B9'}
                ],
                'threshold': {'line': {'color': "black", 'width':4}, 'value': risk_percent}
            }
        ))
        gauge_fig.update_layout(height=400)
        st.plotly_chart(gauge_fig)

        # Predict again
        if st.button("🔄 Predict Again"):
            st.session_state.submitted = False
            st.session_state.predicted = False
            st.session_state.data = {}
            st.rerun()
