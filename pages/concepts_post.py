import streamlit as st
from utils.github_ops import create_file
from utils.builders import build_concept

st.title("➕ Post New Concept")

title = st.text_input("Concept Title")
slug = title.lower().replace(" ", "-")
description = st.text_area("Concept Description")

if "urls" not in st.session_state:
    st.session_state.urls = []

url = st.text_input("Add URL")
if st.button("Add URL"):
    st.session_state.urls.append(url)

for u in st.session_state.urls:
    st.write("-", u)

if st.button("🚀 Post Concept"):
    content = build_concept(title, description, st.session_state.urls)
    create_file(f"concepts/{slug}/content.md", content, "Add concept")
    st.session_state.urls = []
    st.success("Concept posted")
