import streamlit as st
from utils.github_ops import list_dir, read_file, update_file
from utils.builders import build_concept

st.title("✏️ Edit Concept")

concepts = [d.name for d in list_dir("concepts")]
concept = st.selectbox("Concept", concepts)

text, sha = read_file(f"concepts/{concept}/content.md")

parts = text.split("## 🔗 Related Problems")
desc = parts[0]
urls = []

if len(parts) > 1:
    urls = [u.strip("- ").strip() for u in parts[1].splitlines() if u.strip()]

description = st.text_area("Description", value=desc)

if "edit_urls" not in st.session_state:
    st.session_state.edit_urls = urls

new_url = st.text_input("Add URL")
if st.button("Add URL"):
    st.session_state.edit_urls.append(new_url)

for u in st.session_state.edit_urls:
    st.write("-", u)

if st.button("💾 Save Concept"):
    content = build_concept(
        concept.replace("-", " ").title(),
        description,
        st.session_state.edit_urls,
    )
    update_file(
        f"concepts/{concept}/content.md",
        content,
        sha,
        "Update concept",
    )
    st.success("Concept updated")
