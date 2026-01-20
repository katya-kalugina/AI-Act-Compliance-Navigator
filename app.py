import streamlit as st

st.set_page_config(page_title="AI Act Navigator", layout="centered")

st.title("EU AI Act Compliance Navigator")
st.markdown("""
This tool provides a deterministic logic tree for classifying AI systems according to **Regulation (EU) 2024/1689**.
*Methodology: Computational Law approach to Art. 5, 6, and Annex III.*
""")

# --- NAVIGATION ---
step = st.sidebar.radio("Compliance Steps", ["1. Prohibited Practices", "2. High-Risk Classification", "3. Obligations Summary"])

# --- STEP 1: PROHIBITED PRACTICES ---
if step == "1. Prohibited Practices":
    st.header("Step 1: Prohibited AI Practices (Article 5)")
    st.info("If any of the following apply, the system is prohibited in the EU.")
    
    p1 = st.checkbox("Cognitive behavioral manipulation leading to physical/psychological harm")
    p2 = st.checkbox("Untargeted scraping of facial images from the internet/CCTV")
    p3 = st.checkbox("Social scoring based on social behavior or personality traits")
    p4 = st.checkbox("Biometric categorization based on sensitive traits (race, religion, etc.)")

    if any([p1, p2, p3, p4]):
        st.error("🚨 RESULT: PROHIBITED. Under Article 5, this AI system cannot be placed on the market.")
    else:
        st.success("✅ No prohibited practices detected. Proceed to Step 2.")

# --- STEP 2: HIGH-RISK AI ---
elif step == "2. High-Risk Classification":
    st.header("Step 2: Risk Classification (Article 6)")
    
    st.subheader("Criteria A: Regulated Products (Art 6.1)")
    is_annex_i = st.toggle("Is the AI a safety component of a product covered by Annex I (e.g., Medical Devices, Toys, Machinery)?")
    
    if is_annex_i:
        st.warning("⚠️ RESULT: HIGH-RISK AI. System falls under Article 6(1).")
    else:
        st.subheader("Criteria B: Specific Domains (Annex III)")
        domain = st.selectbox("Does the AI system operate in any of these areas?", [
            "None of the below",
            "Biometrics (Identification/Categorization)",
            "Critical Infrastructure (Water, Gas, Electricity)",
            "Education and Vocational Training",
            "Employment and HR Management",
            "Access to Essential Private/Public Services (Credit, Emergency, etc.)",
            "Law Enforcement",
            "Migration, Asylum, and Border Control",
            "Administration of Justice and Democratic Processes"
        ])
        
        if domain != "None of the below":
            st.info(f"System identified in Annex III domain: {domain}")
            
            # --- ARTICLE 6(3) FILTER: THE "AUXILIARY TASK" EXCEPTION ---
            st.subheader("The 'Significant Risk' Filter (Article 6(3))")
            st.markdown("Even if listed in Annex III, a system is NOT high-risk if it does not pose a significant risk to rights.")
            
            e1 = st.checkbox("The system performs a narrow procedural task")
            e2 = st.checkbox("The system improves the result of a previously completed human activity")
            e3 = st.checkbox("The system is purely preparatory to an assessment")
            
            if any([e1, e2, e3]):
                st.success("✅ RESULT: NON-HIGH-RISK (Art 6.3 Exception). Only general transparency rules apply.")
            else:
                st.warning("⚠️ RESULT: HIGH-RISK AI. Must comply with Title III requirements.")
        else:
            st.success("✅ RESULT: MINIMAL/LOW RISK. General transparency and voluntary codes of conduct apply.")

# --- STEP 3: OBLIGATIONS ---
else:
    st.header("Step 3: Key Obligations (Article 17)")
    st.markdown("""
    If your system is classified as **High-Risk**, the provider must implement:
    1. **Risk Management System:** A continuous iterative process throughout the lifecycle.
    2. **Data Governance:** Training, validation, and testing datasets must be relevant and representative.
    3. **Technical Documentation:** Comprehensive "Model Cards" and system architecture descriptions.
    4. **Human Oversight:** Design that allows for meaningful human intervention (Human-in-the-loop).
    5. **Accuracy & Robustness:** Guaranteed levels of performance and cybersecurity.
    """)
    st.download_button("Download Compliance Checklist (Draft)", "1. Risk Mgmt\n2. Data Gov\n3. Technical Doc", file_name="check-list.txt")

st.sidebar.markdown("---")
st.sidebar.caption("Tool developed by Ekaterina Kalugina based on Regulation (EU) 2024/1689 official text.")
