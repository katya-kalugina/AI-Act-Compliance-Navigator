import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="AI Act Navigator", layout="wide")

st.title("EU AI Act Compliance Navigator")
st.markdown("""
**Operationalizing Regulation (EU) 2024/1689**  
*A deterministic logic tree for AI system classification, risk assessment, and transparency obligations.*
""")

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Regulatory Modules")
module = st.sidebar.radio("Navigate through the Act:", 
    ["1. Prohibited Practices (Art 5)", 
     "2. High-Risk Classification (Art 6)", 
     "3. Transparency Obligations (Art 50)",
     "4. GPAI & Systemic Risk (Art 51-55)"])

# --- MODULE 1: PROHIBITED PRACTICES ---
if module == "1. Prohibited Practices (Art 5)":
    st.header("Step 1: Prohibited AI Practices (Article 5)")
    st.info("AI systems categorized here are strictly banned from the European Union market.")
    
    with st.expander("Identify Prohibited Criteria"):
        p1 = st.checkbox("Cognitive behavioral manipulation or deceptive techniques intended to distort behavior")
        p2 = st.checkbox("Exploitation of vulnerabilities (age, disability, or specific socio-economic situations)")
        p3 = st.checkbox("Social scoring by public or private actors leading to unfavorable treatment")
        p4 = st.checkbox("Real-time remote biometric identification in public spaces for law enforcement (with narrow exceptions)")
        p5 = st.checkbox("Untargeted scraping of facial images from CCTV or the internet for facial recognition databases")
        p6 = st.checkbox("Emotion recognition in the workplace or educational institutions (except for safety/medical reasons)")

    if any([p1, p2, p3, p4, p5, p6]):
        st.error("🚨 DETERMINATION: PROHIBITED PRACTICE. Under Article 5, this AI system cannot be placed on the market or used.")
    else:
        st.success("✅ No prohibited practices identified. Proceed to Risk Classification.")

# --- MODULE 2: HIGH-RISK CLASSIFICATION ---
elif module == "2. High-Risk Classification (Art 6)":
    st.header("Step 2: Risk Classification Logic (Article 6)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Category A: Annex I Products")
        is_annex_i = st.toggle("Is the AI a safety component or the product itself covered by Annex I legislation (e.g., Medical Devices, Machinery, Aviation)?")
    
    with col2:
        st.subheader("Category B: Annex III Domains")
        domain = st.selectbox("Select the domain of application:", 
            ["None / Other", "Biometrics", "Critical Infrastructure", "Education", "Employment", "Essential Private/Public Services", "Law Enforcement", "Migration", "Justice"])

    # High-Risk Logic
    if is_annex_i:
        st.warning("⚠️ DETERMINATION: HIGH-RISK (Art 6.1). Subject to comprehensive Title III compliance and Article 17 requirements.")
    elif domain != "None / Other":
        st.info(f"System identified in Annex III domain: {domain}")
        
        # --- ARTICLE 6(3) DEROGATION FILTER ---
        st.subheader("Significant Risk Filter (Article 6(3))")
        st.markdown("*New in Regulation 2024/1689:* An Annex III system is NOT high-risk if it performs only auxiliary tasks.")
        
        is_auxiliary = st.checkbox("Does the system perform a narrow procedural/preparatory task with no material influence on the human decision?")
        
        if is_auxiliary:
            st.success("✅ DETERMINATION: NON-HIGH RISK (Art 6.3 Exception applies). Note: Specific transparency rules may still apply.")
        else:
            st.warning("⚠️ DETERMINATION: HIGH-RISK (Art 6.2). Compliance with Article 17 (Quality Management System) and human oversight is mandatory.")
    else:
        st.success("✅ DETERMINATION: MINIMAL/LOW RISK. Encouraged to follow voluntary codes of conduct.")

# --- MODULE 3: TRANSPARENCY (ART 50) ---
elif module == "3. Transparency Obligations (Art 50)":
    st.header("Step 3: Specific Transparency Obligations (Article 50)")
    st.write("These rules apply regardless of risk level when AI interacts with people or generates content.")

    t1 = st.checkbox("Does the AI system interact directly with natural persons (e.g., Chatbots)?")
    t2 = st.checkbox("Is it an emotion recognition or biometric categorization system?")
    t3 = st.checkbox("Does it generate or manipulate 'Deepfakes' (image, audio, or video)?")
    t4 = st.checkbox("Does it generate text published for informining the public on matters of public interest?")

    if any([t1, t2, t3, t4]):
        st.warning("📢 MANDATORY DISCLOSURE: Providers/Deployers must inform users that they are interacting with AI (Article 50(1)-(4)).")
    else:
        st.success("No specific transparency obligations under Article 50 identified for this configuration.")

# --- MODULE 4: GPAI & SYSTEMIC RISK ---
else:
    st.header("Step 4: General-Purpose AI (GPAI) Models (Art 51-55)")
    
    is_gpai = st.toggle("Is the system a General-Purpose AI model (e.g., a foundation model like GPT-4 or Llama)?")
    
    if is_gpai:
        st.subheader("Systemic Risk Assessment (Article 51)")
        compute_power = st.number_input("Total cumulative compute used for training (expressed in FLOPs):", value=0.0, format="%.2e")
        
        if compute_power > 1e25:
            st.error("🚨 CLASSIFICATION: GPAI WITH SYSTEMIC RISK. Subject to Article 53-55: adversarial testing, model evaluations, and systemic risk mitigation.")
        else:
            st.warning("⚠️ CLASSIFICATION: GENERAL GPAI MODEL. Subject to technical documentation, transparency towards downstream providers, and copyright law compliance.")
    else:
        st.info("System is not classified as a General-Purpose AI model.")

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Ekaterina Kalugina. Source: Official Text of the EU AI Act.")
