import streamlit as st
from main import narrative_consistency_pipeline

st.set_page_config(
    page_title="Narrative Consistency Checker",
    layout="centered"
)

st.title("📘 Narrative Consistency Checker")
st.markdown(
    "Multi-Agent Debate System for Narrative Consistency Detection"
)

# Sidebar configuration
st.sidebar.header("⚙️ Settings")

max_chunk_size = st.sidebar.slider(
    "Max sentences per chunk",
    2, 10, 5
)

confidence_threshold = st.sidebar.slider(
    "Judge confidence threshold",
    0.5, 0.9, 0.7
)

min_agreement = st.sidebar.slider(
    "Agent agreement threshold",
    0.4, 0.9, 0.6
)

# Text input
st.subheader("📄 Enter text")
text_input = st.text_area(
    "Paste your narrative here",
    height=250
)

# Run analysis
if st.button("🔍 Analyze"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            config = {
                "max_chunk_size": max_chunk_size,
                "confidence_threshold": confidence_threshold,
                "min_agreement": min_agreement
            }

            report = narrative_consistency_pipeline(text_input, config)

        st.success("Analysis complete!")

        st.metric("Consistency Score", report["consistency_score"])
        st.metric(
            "Verdict",
            "Consistent ✅" if report["is_consistent"] else "Inconsistent ❌"
        )
        st.metric("Confidence", report["confidence"])

        st.subheader("⚠️ Issues detected")
        if report["issues_detected"]:
            for issue in report["issues_detected"]:
                st.error(issue)
        else:
            st.success("No inconsistencies found")

        st.subheader("🧾 Full Report")
        st.json(report)