"""Main entry point for Problem Solving CMS."""

import streamlit as st

# Configure page
st.set_page_config(
    page_title="Problem Solving CMS",
    page_icon="📚",
    layout="centered"
)

# Main title
st.title("📚 Problem Solving Knowledge Base")

st.markdown("---")

# Navigation
st.subheader("Solutions")
col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/solutions_post.py", label="➕ Post New Solution")
with col2:
    st.page_link("pages/solutions_edit.py", label="✏️ Edit Solution")

st.markdown("---")

st.subheader("Concepts")
col3, col4 = st.columns(2)
with col3:
    st.page_link("pages/concepts_post.py", label="➕ Post New Concept")
with col4:
    st.page_link("pages/concepts_edit.py", label="✏️ Edit Concept")
