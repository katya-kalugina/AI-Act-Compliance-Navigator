import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="AI Act Navigator", layout="wide")

# Применяем строгий стиль оформления
st.title("EU AI Act Compliance Navigator")
st.markdown("""
**Operationalizing Regulation (EU) 2024/1689**  
*A deterministic logic framework for AI classification, risk assessment, and transparency obligations. 
Updated with Feb 2025 Commission Guidelines on the definition of AI and GPAI.*
""")

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Regulatory Modules")
module = st.sidebar.radio("Navigate through the Act:", 
    ["1. Prohibited Practices (Art 5)", 
     "2. High-Risk Classification (Art 6)", 
     "3. Transparency Obligations (Art 50)",
     "4. GPAI Models (Art 51-55)"])

# --- MODULE 1: PROHIBITED PRACTICES (Art 5) ---
if module == "1. Prohibited Practices (Art 5)":
    st.header("Module 1: Prohibited AI Practices (Article 5)")
    st.info("AI systems falling under these categories are banned from the EU market since February 2, 2025.")

    with st.container():
        st.subheader("Critical Prohibitions Check")
        
        # 1(a) & 1(b): Manipulative & Vulnerability exploitation
        p_manipulate = st.checkbox("System uses subliminal, manipulative, or deceptive techniques to distort behavior and cause significant harm (Art 5.1.a)")
        p_vulnerable = st.checkbox("System exploits vulnerabilities (age, disability, socio-economic situation) to distort behavior and cause significant harm (Art 5.1.b)")
        
        # 1(c): Social Scoring
        p_scoring = st.checkbox("System performs social scoring (classification based on social behavior or personality traits leading to unfavorable treatment) (Art 5.1.c)")
        
        # 1(d): Individual Predictive Policing
        st.write("---")
        p_predictive = st.checkbox("System makes risk assessments to predict the risk of a person committing criminal offences based solely on profiling or personality traits (Art 5.1.d)")
        if p_predictive:
            st.warning("⚠️ **Exception check:** Does the system ONLY support human assessment based on objective, verifiable facts already linked to a criminal activity?")
            p_predictive_exception = st.radio("Is this exception met?", ["No", "Yes"])
            if p_predictive_exception == "Yes": p_predictive = False # Clear prohibition if exception applies
        
        # 1(e): Facial Recognition Databases
        p_scraping = st.checkbox("System creates/expands facial recognition databases via untargeted scraping of facial images from the internet or CCTV (Art 5.1.e)")
        
        # 1(f): Emotion Recognition
        st.write("---")
        p_emotion = st.checkbox("System infers emotions of natural persons in workplace or education settings (Art 5.1.f)")
        if p_emotion:
            st.warning("⚠️ **Exception check:** Is the system intended for medical or safety reasons?")
            p_emotion_exception = st.radio("Is medical/safety intent present?", ["No", "Yes"])
            if p_emotion_exception == "Yes": p_emotion = False

        # 1(g): Biometric Categorization
        p_bio_cat = st.checkbox("System categorizes persons based on biometric data to deduce sensitive traits (race, religion, sexual orientation, etc.) (Art 5.1.g)")
        
        # 1(h): Real-time RBI for Law Enforcement
        st.write("---")
        p_rbi = st.checkbox("System uses 'real-time' remote biometric identification in publicly accessible spaces for law enforcement (Art 5.1.h)")
        if p_rbi:
            st.warning("⚠️ **Strict Necessity Check (Exceptions):** Is the use strictly necessary for: (i) victims of trafficking/missing persons, (ii) imminent threat to life/terrorist attack, or (iii) locating suspects of specific serious crimes?")
            p_rbi_exception = st.radio("Is one of these narrow objectives met and authorized?", ["No", "Yes"])
            if p_rbi_exception == "Yes": p_rbi = False

    # FINAL VERDICT FOR MODULE 1
    if any([p_manipulate, p_vulnerable, p_scoring, p_predictive, p_scraping, p_emotion, p_bio_cat, p_rbi]):
        st.error("🚨 DETERMINATION: PROHIBITED PRACTICE identified. Placement on the market or use is forbidden under Article 5.")
    else:
        st.success("✅ No prohibited practices identified under the current configuration.")

# --- MODULE 2: HIGH-RISK (Art 6) --
elif module == "2. High-Risk Classification (Art 6)":
    st.header("Module 2: Risk Classification Logic (Article 6)")
    
    st.subheader("1. Criteria for Regulated Products (Article 6(1))")
    st.write("A system is high-risk if BOTH conditions are met:")
    c1_a = st.checkbox("The AI is a safety component or is itself a product covered by Annex I (e.g., Medical Devices, Machinery, Lifts).")
    c1_b = st.checkbox("The product is required to undergo a **third-party conformity assessment** under Annex I legislation.")
    
    is_high_risk_6_1 = c1_a and c1_b

    st.divider()
    st.subheader("2. Criteria for Specific Domains (Article 6(2) & Annex III)")
    domain = st.selectbox("Does the system operate in an Annex III domain?", [
        "None / Other", "Biometrics", "Critical Infrastructure", "Education", "Employment", 
        "Access to Services", "Law Enforcement", "Migration", "Justice"
    ])
    
    is_annex_iii = domain != "None / Other"

    # --- THE LOGIC ENGINE FOR ARTICLE 6 ---
    if is_high_risk_6_1:
        st.warning("⚠️ DETERMINATION: HIGH-RISK AI (under Art 6(1)).")
        st.info("Your system is a safety component of a regulated product requiring third-party assessment.")
        
    elif is_annex_iii:
        st.info(f"System identified in Annex III domain: {domain}")
        
        # ARTICLE 6(3) DEROGATION & PROFILING OVERRIDE
        st.subheader("Significant Risk Filter (Article 6(3))")
        
        is_profiling = st.toggle("Does the AI system perform **Profiling** of natural persons?", 
                                help="Profiling always leads to High-Risk classification regardless of other exceptions.")
        
        if is_profiling:
            st.warning("⚠️ DETERMINATION: HIGH-RISK AI (Art 6.3 override).")
            st.error("Profiling of natural persons in Annex III domains is ALWAYS high-risk.")
        else:
            st.write("Check if any 'Non-Significant Risk' exceptions apply:")
            e1 = st.checkbox("Narrow procedural task")
            e2 = st.checkbox("Improvement of a previous human activity")
            e3 = st.checkbox("Detection of decision patterns (preparatory/auxiliary)")
            e4 = st.checkbox("Purely preparatory task to an assessment")

            if any([e1, e2, e3, e4]):
                st.success("✅ DETERMINATION: NON-HIGH RISK (Art 6.3 Exception applies).")
                st.markdown("""
                **Mandatory Actions (Art 6.4):**
                - Document the assessment before placing on the market.
                - Register the system in the EU database (Art 49.2).
                """)
            else:
                st.warning("⚠️ DETERMINATION: HIGH-RISK AI (Art 6.2). Compliance with Title III required.")
    else:
        st.success("✅ DETERMINATION: LOW/MINIMAL RISK (unless Art 50 applies).")

# --- MODULE 3: TRANSPARENCY (ARTICLE 50) - 
elif module == "3. Transparency Obligations (Art 50)":
    st.header("Module 3: Transparency for Specific AI Systems")
    st.write("This module identifies obligations based on the final text of Art. 50 (1)-(4).")

    # --- 50(1): INTERACTION (Providers) ---
    with st.expander("A. Interaction with Humans (Art 50.1)", expanded=True):
        t1 = st.checkbox("Does the AI system interact directly with natural persons (e.g., Chatbots)?")
        if t1:
            st.info("ℹ️ **Provider's Obligation:** Inform natural persons they are interacting with AI (unless obvious).")

    # --- 50(2): SYNTHETIC CONTENT MARKING (Providers)
    with st.expander("B. Synthetic Content Generation (Art 50.2)", expanded=True):
        st.write("Obligation for providers of AI generating synthetic audio, image, video, or text.")
        t2 = st.checkbox("Does the system generate synthetic content (audio, image, video, or text)?")
        
        if t2:
            st.warning("🛠️ **Provider's Obligation:** Ensure outputs are marked in a **machine-readable format** and are **detectable** as AI-generated.")
            
            # Sub-check for technical feasibility
            st.markdown("*Technical feasibility factors (State-of-the-Art):*")
            st.caption("Solutions must be effective, interoperable, robust, and reliable.")
            
            # Exceptions logic from Art 50.2
            st.subheader("Exemptions from Marking:")
            e1 = st.checkbox("Assistive function for standard editing (no substantial alteration)")
            e2 = st.checkbox("Authorized by law to investigate/prosecute criminal offences")
            
            if e1 or e2:
                st.success("✅ This specific use case is EXEMPT from marking obligations under Art 50(2).")

    # --- 50(3): EMOTION RECOGNITION (Deployers) ---
    with st.expander("C. Emotion Recognition & Biometric Categorization (Art 50.3)"):
        t3 = st.checkbox("Is the system used for Emotion Recognition or Biometric Categorization?")
        if t3:
            st.warning("⚠️ **Deployer's Obligation:** Inform natural persons exposed thereto of the system's operation.")

    # --- 50(4): DEEPFAKES (Deployers) ---
    with st.expander("D. Deepfakes & Public Information (Art 50.4)"):
        t4 = st.checkbox("Does the system generate 'Deepfakes'?")
        t5 = st.checkbox("Does it generate text published to inform the public on matters of public interest?")
        if t4 or t5:
            st.warning("📢 **Deployer's Obligation:** Disclose that content is artificially generated/manipulated.")

# --- MODULE 4: GPAI MODELS (Art 51-55) - 
elif module == "4. GPAI Models (Art 51-55)":
    st.header("Module 4: General-Purpose AI (GPAI) Models")
    st.markdown("Based on Art 3(63) and February 2025 Commission Guidelines.")

    st.subheader("1. Generality Assessment (Definition Check)")
    g1 = st.checkbox("Does the model perform a wide range of distinct tasks (text, code, reasoning)?")
    g2 = st.checkbox("Can it be integrated into various downstream systems?")
    
    if g1 and g2:
        st.success("🎯 CLASSIFICATION: THIS IS A GPAI MODEL.")
        
        st.divider()
        st.subheader("2. Systemic Risk Classification (Art 51)")
        compute = st.number_input("Cumulative training compute (FLOPs):", value=0.0, format="%.2e")
        high_impact = st.checkbox("Model has high-impact capabilities (Commission designation)")

        if compute >= 1e25 or high_impact:
            st.error("🚨 CLASSIFICATION: GPAI WITH SYSTEMIC RISK")
            st.markdown("""
            **Mandatory Obligations (Art 55):**
            - Adversarial testing (Red Teaming).
            - Systemic risk assessment & mitigation.
            - Incident reporting to the AI Office.
            - High-level cybersecurity protection.
            """)
        else:
            st.warning("⚠️ CLASSIFICATION: GENERAL GPAI (Non-Systemic)")
            st.markdown("""
            **Core Obligations (Art 53):**
            - Technical documentation for authorities.
            - Documentation for downstream providers.
            - Copyright law compliance policy.
            - Detailed summary of training data content.
            """)
    else:
        st.info("Identify 'generality' criteria to see applicable GPAI obligations.")

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Ekaterina Kalugina. Precise Regulatory Implementation.")
