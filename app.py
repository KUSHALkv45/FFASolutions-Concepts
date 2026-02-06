import streamlit as st

st.set_page_config(page_title="Problem Solving CMS")

st.title("📚 Problem Solving Knowledge Base")

st.page_link("pages/solutions_post.py", label="➕ Post New Solution")
st.page_link("pages/solutions_edit.py", label="✏️ Edit Solution")
st.page_link("pages/concepts_post.py", label="➕ Post New Concept")
st.page_link("pages/concepts_edit.py", label="✏️ Edit Concept")
