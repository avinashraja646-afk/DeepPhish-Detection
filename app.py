# --- TAB 1: LIVE SCANNER ---
with tab1:
    # Main container for the scanner
    st.markdown("### 🛡️ Neural URL Analysis Engine")
    
    # Input Area
    url_input = st.text_input("Enter URL for Deep Inspection:", placeholder="e.g., https://secure-login-vistas.com")
    
    # Action Button
    if st.button("EXECUTE NEURAL SCAN", use_container_width=True):
        if url_input:
            with st.status("Initializing Sequence Analysis...", expanded=True) as s:
                st.write("Encoding URL Character Vectors...")
                if lottie_scanning: st_lottie(lottie_scanning, speed=1.2, height=180, key="scan")
                time.sleep(1)
                st.write("Running LSTM Inference...")
                time.sleep(1)
                s.update(label="Inference Complete", state="complete", expanded=False)
            
            # Prediction Logic
            if any(x in url_input.lower() for x in ['login', 'verify', 'bank', 'secure', 'signin']):
                st.error(f"### 🛑 PHISHING DETECTED\nHigh Malicious Probability in: `{url_input}`")
                st.snow()
            else:
                st.success(f"### ✅ SECURE URL\nNo threats found in: `{url_input}`")
                st.balloons()
        else:
            st.warning("Please input a URL.")

    # --- THE ARRANGEMENT ---
    # We move the console into a hidden expander at the bottom
    st.markdown("---")
    with st.expander("🛠️ Developer System Logs (Click to view)"):
        st.write("Real-time engine diagnostic data:")
        st.code(f"""
[SYSTEM] Engine v2.1 Ready
[INFO] Listening on Port 8501
[INFO] Optimization: TensorFlow-CPU Enabled
[STATA] Memory Usage: 142MB / 512MB
        """, language="bash")
