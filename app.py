import streamlit as st
import json

# Load data
with open("curriculum_data.json", "r") as f:
    data = json.load(f)

st.set_page_config(page_title="Pro-English Engine", layout="centered")
st.title("🎓 Professional Proficiency Engine")

domain = st.sidebar.selectbox("Select Domain", ["Nursing", "Hospitality"])
question = st.sidebar.radio("Select Test Item", range(len(data[domain])))

item = data[domain][question]

st.subheader(f"{domain} Assessment")
st.write(f"**Baseline:** {item['baseline']}")

user_answer = st.text_input("Your Band 9 Transformation:")

if st.button("Submit & Analyze"):
    # Simple logic: compare against target keywords
    st.success(f"Target Structure: {item['target']}")
    st.info("Your response is being evaluated for nominalization and thematic fronting.")
