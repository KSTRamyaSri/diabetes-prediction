import streamlit as st

def main():
    st.markdown("""
      <style>
      .stApp {
          background: linear-gradient(135deg, #E6E6FA, #FFD6EC);
          min-height: 100vh;
      }
      header, footer, [data-testid="stSidebar"], .stDeployButton {
          display: none !important;
      }
      .about-title {
          font-size: 2.5rem;
          font-weight: 800;
          text-align: center;
          color: #6B1EE6;
          margin-top: 30px;
          margin-bottom: 15px;
          font-family: "Trebuchet MS", Arial, sans-serif;
      }
      .about-desc {
          font-size: 1.15rem;
          text-align: center;
          color: #40266d;
          margin-bottom: 22px;
      }
      .cards-row {
          display: flex;
          flex-wrap: wrap;
          gap: 32px;
          justify-content: center;
          margin-top: 22px;
      }
      .img-card {
          background: linear-gradient(120deg, #ffeafd 60%, #dee3ff 100%);
          border-radius: 18px;
          box-shadow: 0 6px 24px #bd87ff33;
          width: 260px;
          padding: 24px 18px 20px 18px;
          display: flex;
          flex-direction: column;
          align-items: center;
          animation: fadeInCard 1.4s 0.1s both;
          transition: transform 0.15s;
      }
      .img-card:hover {
          transform: scale(1.07) rotate(-2deg);
          box-shadow: 0 12px 32px #bd87ff5b;
      }
      @keyframes fadeInCard {
          from {opacity:0; transform:translateY(40px);}
          to {opacity:1; transform:translateY(0);}
      }
      .card-image {
          width: 72px;
          height: 72px;
          border-radius: 50%;
          object-fit: cover;
          box-shadow: 0 2px 18px #9d84f888;
          margin-bottom: 14px;
      }
      .card-label {
          font-size: 1.08rem;
          font-weight: 700;
          color: #3e217d;
          text-align: center;
      }
      </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="about-title">About Us</div>', unsafe_allow_html=True)
    st.markdown('<div class="about-desc">Welcome to the <b>Diabetes Prediction Dashboard</b>. <br>This dashboard helps users understand their risk of diabetes using Machine Learning models.<br></div>', unsafe_allow_html=True)

    st.markdown('<div class="cards-row">', unsafe_allow_html=True)
    st.markdown('''
      <div class="img-card">
         <img class="card-image" src="https://cdn.pixabay.com/photo/2017/05/10/15/26/doctor-2301330_960_720.png">
         <div class="card-label">🩺 User-friendly Prediction Form</div>
      </div>
      <div class="img-card">
         <img class="card-image" src="https://cdn.pixabay.com/photo/2016/08/20/14/20/graph-1600058_960_720.png">
         <div class="card-label">📊 Visual Charts & Risk Tracking</div>
      </div>
      <div class="img-card">
         <img class="card-image" src="https://cdn.pixabay.com/photo/2020/01/31/09/28/lightbulb-4800270_960_720.png">
         <div class="card-label">💡 Informative Insights</div>
      </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Back button (use st.rerun for latest Streamlit versions)
    if st.button("← Back to Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
