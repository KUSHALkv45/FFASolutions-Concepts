"""Page for posting new concepts."""

import streamlit as st
from utils.github_ops import create_file
from utils.builders import build_concept

st.title("➕ Post New Concept")

# Input fields
title = st.text_input("Concept Title", help="Enter a descriptive title for the concept")
slug = title.lower().replace(" ", "-") if title else ""

if slug:
    st.caption(f"📁 Will be saved as: `concepts/{slug}/content.md`")

description = st.text_area(
    "Concept Description",
    height=200,
    help="Explain the concept in detail"
)

# URL management
st.subheader("Related Problems")

if "urls" not in st.session_state:
    st.session_state.urls = []

col1, col2 = st.columns([3, 1])
with col1:
    url = st.text_input("Add URL", placeholder="https://leetcode.com/problems/...")
with col2:
    st.write("")  # Spacing
    st.write("")  # Spacing
    if st.button("➕ Add", disabled=not url.strip()):
        if url.strip() and url.strip() not in st.session_state.urls:
            st.session_state.urls.append(url.strip())
            st.rerun()

# Display current URLs
if st.session_state.urls:
    st.write("**Current URLs:**")
    for i, u in enumerate(st.session_state.urls):
        col_url, col_remove = st.columns([5, 1])
        with col_url:
            st.text(f"• {u}")
        with col_remove:
            if st.button("🗑️", key=f"remove_{i}"):
                st.session_state.urls.pop(i)
                st.rerun()
else:
    st.info("No URLs added yet")

# Submit button
st.markdown("---")

if st.button("🚀 Post Concept", type="primary", disabled=not (title and description)):
    if not title.strip():
        st.error("❌ Title is required")
    elif not description.strip():
        st.error("❌ Description is required")
    else:
        try:
            content = build_concept(title, description, st.session_state.urls)
            create_file(f"concepts/{slug}/content.md", content, f"Add concept: {title}")
            st.session_state.urls = []
            st.success(f"✅ Concept '{title}' posted successfully!")
            st.balloons()
        except Exception as e:
            st.error(f"❌ Error posting concept: {str(e)}")
