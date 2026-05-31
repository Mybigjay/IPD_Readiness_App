import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===================================================
# 1. PAGE CONFIGURATION
# ===================================================
st.set_page_config(
    page_title="IPD Research Tool - CMG 6402",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ Integrated Project Delivery (IPD) Research Support Tool")
st.subheader("CMG 6402 – Canadian Public Sector IPD Analysis (Group 5)")

st.markdown("""
This tool operationalizes your research on **Integrated Project Delivery (IPD)** in Canadian public sector construction.
It evaluates how project procurement structure, governance framework, collaboration maturity, and risk allocation align with IPD principles (CCDC 30).
""")

st.write("**Group 5 Members:** | Blessing Ngozi Emelogu | Collins Gyasi | Danielle Johnson | Omotayo Moyosore Akinwale*")
st.write("**Supervised by: Prof. Babak Rahmani**")
st.divider()

# ===================================================
# 2. ASSESSMENT INPUT LAYER
# ===================================================
st.header("📋 Assessment Inputs")
st.markdown("Select the delivery parameters that describe the target public project jurisdiction:")

col1, col2 = st.columns(2)

with col1:
    procurement = st.selectbox(
        "1. Procurement Model Selection",
        ["Design-Bid-Build (DBB)", "Design-Build (DB)", "Construction Management (CM)",
         "Integrated Project Delivery (IPD / CCDC 30)"]
    )

    governance = st.selectbox(
        "2. Governance Structure",
        ["Highly centralized", "Moderately centralized", "Collaborative", "Fully integrated IPD team"]
    )

with col2:
    collaboration = st.selectbox(
        "3. Organizational Collaboration Level",
        ["Low (siloed teams)", "Moderate", "High", "Fully co-located IPD team"]
    )

    risk_model = st.selectbox(
        "4. Risk Sharing & Allocation Model",
        ["Traditional risk transfer", "Partial risk sharing", "Target value delivery", "Shared risk-reward pool (IPD)"]
    )

st.markdown(" ")
generate_assessment = st.button("Generate IPD Evaluation Results", type="primary")
st.divider()

# ===================================================
# 3. SCORING AND ANALYSIS COMPUTATION ENGINE
# ===================================================
if generate_assessment:

    score_map = {
        "Design-Bid-Build (DBB)": 25,
        "Design-Build (DB)": 50,
        "Construction Management (CM)": 70,
        "Integrated Project Delivery (IPD / CCDC 30)": 100,

        "Highly centralized": 20,
        "Moderately centralized": 50,
        "Collaborative": 80,
        "Fully integrated IPD team": 100,

        "Low (siloed teams)": 20,
        "Moderate": 50,
        "High": 80,
        "Fully co-located IPD team": 100,

        "Traditional risk transfer": 20,
        "Partial risk sharing": 50,
        "Target value delivery": 80,
        "Shared risk-reward pool (IPD)": 100
    }

    p_score = score_map[procurement]
    g_score = score_map[governance]
    c_score = score_map[collaboration]
    r_score = score_map[risk_model]

    overall_score = int(np.mean([p_score, g_score, c_score, r_score]))

    st.header("📊 Computed IPD Evaluation Results")

    if overall_score >= 75:
        st.success(f"### High IPD Alignment Score: {overall_score}%")
    elif overall_score >= 50:
        st.warning(f"### Moderate IPD Alignment Score: {overall_score}%")
    else:
        st.error(f"### Low IPD Alignment Score: {overall_score}%")

    # Display Side-by-Side: Chart on left, written barriers analysis on right
    chart_col, text_col = st.columns([1, 1])

    with chart_col:
        # Generate clean Polar Radar Chart
        categories = ["Procurement", "Governance", "Collaboration", "Risk Model"]
        base_values = [p_score, g_score, c_score, r_score]

        radar_values = base_values + base_values[:1]
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        radar_angles = angles + angles[:1]

        fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))

        # Plot styling based on score thresholds
        plot_color = "#2ca02c" if overall_score >= 75 else "#ff7f0e" if overall_score >= 50 else "#d62728"
        ax.plot(radar_angles, radar_values, color=plot_color, linewidth=2, linestyle="solid")
        ax.fill(radar_angles, radar_values, color=plot_color, alpha=0.2)

        ax.set_xticks(angles)
        ax.set_xticklabels(categories, fontsize=9, fontweight='bold')

        ax.set_ylim(0, 100)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(["20%", "40%", "60%", "80%", "100%"], color="grey", fontsize=8)
        ax.grid(True, linestyle="--", alpha=0.5)

        st.pyplot(fig)

    with text_col:
        st.subheader("🚧 Key IPD Barriers Found (Section 8 Mapping)")

        barriers_exist = False
        if procurement != "Integrated Project Delivery (IPD / CCDC 30)":
            st.markdown(
                "🔴 **Procurement Rigidity:** Statutory low-bid environments limit multi-party qualifications selection.")
            barriers_exist = True
        if governance in ["Highly centralized", "Moderately centralized"]:
            st.markdown(
                "🔴 **Centralized Oversight:** Traditional public command structures impede Joint Management Committee (JMC) collective choices.")
            barriers_exist = True
        if collaboration in ["Low (siloed teams)", "Moderate"]:
            st.markdown(
                "🔴 **Cultural Fragmentation:** Fragmented stakeholder interfaces diminish design validation transparency.")
            barriers_exist = True
        if risk_model == "Traditional risk transfer":
            st.markdown(
                "🔴 **Adversarial Terms:** Unilateral risk shifting runs directly counter to standard CCDC 30 risk-reward pooling mechanisms.")
            barriers_exist = True

        if not barriers_exist:
            st.success(
                "No systemic delivery barriers identified. The organizational landscape matches IPD core parameters.")

    # ===================================================
    # 4. CASE STUDY ALIGNMENT MATRIX
    # ===================================================
    st.divider()
    st.header("🏗️ IPD Empirical Case Study Matrix (Sections 5 & 6 Mapping)")

    case_studies = pd.DataFrame({
        "Empirical Research Project Case": [
            "St. Paul’s Hospital (Canada)",
            "Humber River Hospital (Canada)",
            "Sutter Health Projects (USA)",
            "UCSF Medical Center (USA)"
        ],
        "Delivery Model Framework": [
            "Formal CCDC 30 IPD",
            "IPD-Lean Collaborative Variant",
            "Full Multi-Party IPD",
            "Integrated Poly-Party Agreement"
        ],
        "Core Performance Diagnostic Insight": [
            "Strong public owner leadership enabled localized procurement success.",
            "Early trade contractor integration eliminated design coordination variance.",
            "Shared financial risk-reward pools generated reliable structural project savings.",
            "Big Room co-location environments accelerated multi-party decision schedules."
        ]
    })
    st.dataframe(case_studies, use_container_width=True)

    # ===================================================
    # 5. IMPLEMENTATION ROADMAP
    # ===================================================
    st.divider()
    st.header("🗺️ Recommended CCDC 30 Implementation Roadmap")

    if overall_score >= 75:
        st.success("""
        **Phase 3: Direct CCDC 30 Execution** - Proceed to execute full multi-party contract framework.
        - Instantiate formal shared risk-reward pool boundaries.
        - Set up a co-located Big Room structure to maximize Lean design optimization.
        """)
    elif overall_score >= 50:
        st.warning("""
        **Phase 2: Hybrid Collaborative Transition** - Introduce collaborative procurement pilots with early constructor qualification.
        - Establish custom multi-party Memorandums of Understanding (MoU) to share target incentives.
        - Shift internal tracking mechanisms toward transparency-based collaborative management.
        """)
    else:
        st.error("""
        **Phase 1: Institutional & Legislative Reform** - Audit current public purchasing regulations to allow alternative procurement paths.
        - Transition tracking metrics away from low-bid methods toward Qualification-Based Selection ($QBS$).
        - Organize educational design workshops focused on collaborative risk alignment structures.
        """)

    # ===================================================
    # 6. DATA EXPORT SYSTEM
    # ===================================================
    st.divider()
    st.subheader("💾 Export Assessment Diagnostics")

    results_df = pd.DataFrame({
        "IPD Assessment Dimension": categories,
        "Assigned Diagnostic Score": base_values
    })
    csv_bytes = results_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Download Diagnostic Matrix Report (CSV)",
        data=csv_bytes,
        file_name="ipd_readiness_assessment_results.csv",
        mime="text/csv",
        type="secondary"
    )

# ===================================================
# SYSTEM FOOTER
# ===================================================
st.divider()
st.caption("CMG 6402 Group 5 Research Artifact — IPD Multi-Party Decision Framework Prototype")