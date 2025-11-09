import streamlit as st
from pages import about, contact, dashboard


st.set_page_config(
    page_title="Diabetes Prediction Dashboard",
    # layout="wide",
    # initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #E6E6FA, #FFD6EC) !important;
    min-height: 100vh !important;
}
header, footer, [data-testid="stSidebar"], .stDeployButton {display: none !important;}
.main-title {
    font-family: "Trebuchet MS", Arial, sans-serif;
    color: #000;
    font-size: 4rem;
    font-weight: 800;
    text-align: center;
    margin-top: 6vh;
    z-index: 2;
    position: relative;
}
.animated-welcome {
    font-size: 1.7rem;
    font-weight: 600;
    text-align: center;
    margin-top: 1.5rem;
    margin-bottom: 2.3rem;
    color: #7B5FC0;
    font-family: "Trebuchet MS";
    animation: fadeInUp 2.5s;
}
@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(40px);}
    60% { opacity: 0.7; transform: translateY(-7px);}
    100% { opacity: 1; transform: translateY(0);}
}
/* Style columns to mimic button look */
.stButton>button {
    background: #7B5FC0!important;
    color: #fff !important;
    font-size: 22px !important;
    font-weight: bold !important;
    border-radius: 14px !important;
    border: none !important;
    padding: 16px 48px !important;
    box-shadow: 0 2px 18px #cecece6e;
    letter-spacing: 1px;
    margin: 12px 0 !important;
    transition: 0.17s !important;
}
.stButton>button:hover {
    background: linear-gradient(to right, #8a6fd0,#BE93E4, #FAE6FA) !important;
    color: #fff !important;
    box-shadow: 0 6px 38px #bba3e978 !important;
    scale: 1.07;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Welcome"  # Or "Welcome" as landing if you wish

# def nav_page(page_module, name=None):
#     st.session_state.page = name or page_module.__name__.split('.')[-1]
#     st.rerun()

def nav_page(page_module, name=None):
    st.session_state.page = name or page_module.__name__.split('.')[-1]
    st.session_state.current_module = page_module
    st.rerun()




# ---- NAVIGATION LOGIC ----

if st.session_state.page == "Welcome":
    st.markdown('<div class="main-title">Diabetes Prediction Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="animated-welcome">✨ Welcome! <span style="color:#A850E8">Choose a page below</span> ✨</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1], gap='large')
    with col1:
        if st.button("About Us", use_container_width=True):
            nav_page(about, "About")
    with col2:
        if st.button("Contact Us", use_container_width=True):
            nav_page(contact, "Contact")
    with col3:
        if st.button("Dashboard", use_container_width=True):
            nav_page(dashboard, "DashboardMain")

elif st.session_state.page == "About":
    about.main()
    # if st.button("⬅ Back", use_container_width=True):
    #     nav_page("Dashboard")

elif st.session_state.page == "Contact":
    contact.main()
    # if st.button("⬅ Back", use_container_width=True):
    #     nav_page("Dashboard")

elif st.session_state.page == "DashboardMain":
    dashboard.main()
    


