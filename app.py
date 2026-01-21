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
    st.info("AI systems categorized here are strictly banned from the European Union market.")
    
    with st.container():
        st.subheader("Assessment Criteria")
        p1 = st.checkbox("Cognitive behavioral manipulation or deceptive techniques intended to distort behavior")
        p2 = st.checkbox("Exploitation of vulnerabilities (age, disability, or specific socio-economic situations)")
        p3 = st.checkbox("Social scoring by public or private actors leading to unfavorable treatment")
        p4 = st.checkbox("Real-time remote biometric identification in public spaces for law enforcement (with narrow exceptions)")
        p5 = st.checkbox("Untargeted scraping of facial images from CCTV or the internet for facial recognition databases")
        p6 = st.checkbox("Emotion recognition in the workplace or educational institutions (except for safety/medical reasons)")

    if any([p1, p2, p3, p4, p5, p6]):
        st.error("🚨 DETERMINATION: PROHIBITED PRACTICE. Under Article 5, this AI system cannot be placed on the market or used in the EU.")
    else:
        st.success("✅ No prohibited practices identified. Proceed to Risk Classification.")

# --- MODULE 2: HIGH-RISK CLASSIFICATION (Art 6) ---
elif module == "2. High-Risk Classification (Art 6)":
    st.header("Module 2: Risk Classification Logic (Article 6)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Category A: Annex I Products")
        is_annex_i = st.toggle("Is the AI a safety component or the product itself covered by Annex I legislation (e.g., Medical Devices, Aviation, Machinery)?")
    
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
        st.markdown("*Filter criteria:* An Annex III system is NOT high-risk if it performs only auxiliary tasks.")
        
        is_auxiliary = st.checkbox("Does the system perform a narrow procedural task with no material influence on the final decision?")
        is_improvement = st.checkbox("Does the system only improve the result of a previously completed human activity?")
        
        if is_auxiliary or is_improvement:
            st.success("✅ DETERMINATION: NON-HIGH RISK (Art 6.3 Exception applies). Note: Specific transparency rules may still apply.")
        else:
            st.warning("⚠️ DETERMINATION: HIGH-RISK (Art 6.2). Compliance with Article 17 (Quality Management System) and human oversight is mandatory.")
    else:
        st.success("✅ DETERMINATION: MINIMAL/LOW RISK. Encouraged to follow voluntary codes of conduct.")

# --- MODULE 3: TRANSPARENCY (ARTICLE 50) - FINAL TEXT COMPLIANCE ---
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

# --- MODULE 4: GPAI DEFINITION & SYSTEMIC RISK (Art 51-55) ---
else:
    st.header("Module 4: General-Purpose AI (GPAI) Models")
    st.markdown("This section applies specifically to the underlying AI **models**, as clarified in the Feb 2025 Commission Guidelines.")

    # --- PART 1: DEFINITION CHECK (Art 3(63) & Guidelines) ---
    st.subheader("1. General-Purpose Definition Check")
    st.write("Determine if the model meets the criteria of 'generality':")
    
    g1 = st.checkbox("Does the model display significant generality and competence in performing a wide range of distinct tasks?")
    g2 = st.checkbox("Can the model be integrated into a variety of downstream AI systems?")
    exclusion = st.checkbox("Is this model used strictly for R&D/Prototyping before being placed on the market?")

    if g1 and g2 and not exclusion:
        st.success("🎯 CLASSIFICATION: THIS IS A GPAI MODEL.")
        
        st.divider()
        # --- PART 2: SYSTEMIC RISK ASSESSMENT (Art 51) ---
        st.subheader("2. Systemic Risk Assessment (Article 51)")
        st.write("A GPAI model poses a **systemic risk** if it meets any of the following:")
        
        c1 = st.checkbox("It has high-impact capabilities (evaluated through technical methodologies).")
        c2 = st.checkbox("The total cumulative compute used for training is greater than 10^25 FLOPs.")
        c3 = st.checkbox("The Commission has designated it as systemic (Art 51.2).")

        if any([c1, c2, c3]):
            st.error("🚨 CLASSIFICATION: GPAI MODEL WITH SYSTEMIC RISK")
            st.subheader("Additional Obligations (Article 55):")
            st.markdown("""
            - **Model Evaluation:** Adversarial testing and 'Red Teaming'.
            - **Risk Mitigation:** Assessment and mitigation of systemic risks at the Union level.
            - **Incident Reporting:** Mandatory reporting of serious incidents to the AI Office.
            - **Cybersecurity:** High-level protection for the model and infrastructure.
            """)
        else:
            st.warning("⚠️ CLASSIFICATION: GENERAL GPAI MODEL (Non-Systemic)")
            st.subheader("Core Obligations (Article 53):")
            st.markdown("""
            - **Technical Documentation:** For the AI Office and national authorities.
            - **Downstream Transparency:** Information for providers who integrate the model.
            - **Copyright Policy:** Compliance with EU copyright laws.
            - **Training Data Summary:** Detailed summary of the content used for training.
            """)
    elif exclusion:
        st.info("The model is excluded from the AI Act scope as it is restricted to R&D/Prototyping (Art 2).")
    else:
        st.info("The criteria for 'generality' are not met. This is likely a specific/narrow AI model.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Ekaterina Kalugina. Based on the official text of Regulation (EU) 2024/1689.")
