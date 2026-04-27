import streamlit as st

st.set_page_config(page_title="DeepPhish Detector", page_icon="🛡️")

st.title("🛡️ DeepPhish: URL Phishing Detection")
st.write("Machine Learning Solution for identifying malicious links.")

# Input for URL
url = st.text_input("Enter URL to check:", placeholder="e.g., http://secure-login.com")

if st.button("Analyze"):
    if url:
        # This simulates the logic your LSTM model would perform
        suspicious_terms = ['login', 'verify', 'update', 'banking', 'secure', 'bit.ly']
        is_phishing = any(term in url.lower() for term in suspicious_terms)
        
        if is_phishing:
            st.error(f"🚨 ALERT: '{url}' matches phishing patterns!")
        else:
            st.success(f"✅ SUCCESS: '{url}' looks safe for now.")
    else:
        st.warning("Please enter a URL first.")

st.sidebar.markdown("---")
st.sidebar.write("Developed by Avinash")
st.sidebar.write("BCA 3rd Year | Vels University")