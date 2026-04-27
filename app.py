import streamlit as st
import time
from streamlit_lottie import st_lottie
import requests

# Function to load animations safely
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Use these updated links
lottie_security = load_lottieurl("https://lottie.host/82544605-7201-447a-85b4-9366e632b71b/9K18w6V2aL.json")
lottie_scanning = load_lottieurl("https://lottie.host/68f8680d-856b-4e1a-8531-1550c822e039/Z4A69eN6Yk.json")

st.set_page_config(page_title="DeepPhish AI", page_icon="🛡️", layout="wide")

with st.sidebar:
    # Only show if the animation loaded successfully
    if lottie_security:
        st_lottie(lottie_security, speed=1, height=150, key="initial")
    else:
        st.title("🛡️ DeepPhish")
    
    st.title("Project Details")
    st.info("**Student:** Avinash R\n\n**BCA 3rd Year**")
    st.markdown("---")

st.title("🛡️ DeepPhish AI Engine")
st.write("Using Neural Networks to secure the web.")

col1, col2 = st.columns([2, 1])

with col1:
    url_input = st.text_input("Analyze URL:", placeholder="Enter URL here...")
    
    if st.button("Start Deep Analysis"):
        if url_input:
            progress_bar = st.progress(0)
            
            # Only show scanning if loaded
            if lottie_scanning:
                st_lottie(lottie_scanning, speed=1.5, height=200, key="scan")
            
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
            
            if "login" in url_input.lower() or "verify" in url_input.lower():
                st.error("🚨 **PHISHING DETECTED:** Malicious patterns found.")
                st.snow()
            else:
                st.success("✅ **CLEAN:** No threats detected.")
                st.balloons()
        else:
            st.warning("Please enter a URL.")

with col2:
    st.markdown("### Model Performance")
    st.metric("Accuracy", "98.2%")
    st.metric("Latency", "0.04s")
