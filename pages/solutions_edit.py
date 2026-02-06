import streamlit as st
from utils.github_ops import list_dir, read_file, update_file
from utils.builders import build_full_solution

st.title("✏️ Edit Solution")

cats = [d.name for d in list_dir("solutions") if d.type == "dir"]
category = st.selectbox("Category", cats)

solutions = [d.name for d in list_dir(f"solutions/{category}")]
solution = st.selectbox("Solution", solutions)

sections = ["idea", "trace", "complexity", "code"]
section = st.selectbox("Section to edit", sections)

path = f"solutions/{category}/{solution}/{section}.md"

content, sha = read_file(path) if path else ("", None)
text = st.text_area("Edit Section", value=content)

if st.button("💾 Save"):
    update_file(path, text, sha, "Update section")

    all_sections = {}
    for s in sections:
        try:
            t, _ = read_file(f"solutions/{category}/{solution}/{s}.md")
            all_sections[s] = t
        except:
            all_sections[s] = ""

    title = solution.replace("-", " ").title()
    full = build_full_solution(title, all_sections)

    full_path = f"solutions/{category}/{solution}/full.md"
    full_text, full_sha = read_file(full_path)
    update_file(full_path, full, full_sha, "Rebuild full solution")

    st.success("Section updated and full solution rebuilt")
