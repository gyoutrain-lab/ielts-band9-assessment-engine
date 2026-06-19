import streamlit as st
import json

# Setup
st.set_page_config(page_title="Pro-English Engine", page_icon="🌐", layout="wide")

# Sidebar - Professional Control Panel
st.sidebar.title("Configuration")
domain = st.sidebar.selectbox("Industry Domain", ["Nursing", "Hospitality"])
with open("curriculum_data.json", "r") as f:
    data = json.load(f)

# Main Dashboard
st.title(f"🌐 {domain} Professional Proficiency Engine")
st.markdown("---")

for category, content in data[domain].items():
    with st.expander(f"Review: {category.replace('_', ' ')}"):
        st.write(f"**Baseline Prompt:** {content['baseline']}")
        user_input = st.text_area(f"Your Transformation for {category}:", key=category)
        
        if st.button("Evaluate", key=f"btn_{category}"):
            st.success(f"Professional Standard: {content['target']}")
            st.warning("Note: Analyze your response for Nominalization and Thematic Fronting.")
