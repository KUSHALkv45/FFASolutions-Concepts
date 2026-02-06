import streamlit as st
from utils.github_ops import list_dir, create_file
from utils.builders import build_full_solution

st.title("➕ Post New Solution")

# -------- Categories --------
cats = [d.name for d in list_dir("solutions") if d.type == "dir"]
category = st.selectbox("Category", cats + ["➕ Add new"])

if category == "➕ Add new":
    category = st.text_input("New category")

title = st.text_input("Solution Title")
slug = title.lower().replace(" ", "-")

idea = st.text_area("💡 Idea")
trace = st.text_area("🔍 Simple Algo Trace")
complexity = st.text_area("⏱️ Time & Space Complexity")
code = st.text_area("💻 Code")

if st.button("🚀 Post Solution"):
    base = f"solutions/{category}/{slug}"
    sections = {
        "idea": idea,
        "trace": trace,
        "complexity": complexity,
        "code": code,
    }

    for k, v in sections.items():
        if v.strip():
            create_file(f"{base}/{k}.md", v, f"Add {k}")

    full = build_full_solution(title, sections)
    create_file(f"{base}/full.md", full, "Add full solution")

    st.success("Solution posted successfully")
