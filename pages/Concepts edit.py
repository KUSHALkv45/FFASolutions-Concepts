"""Page for editing existing concepts."""

import streamlit as st
from utils.github_ops import list_dir, read_file, update_file
from utils.builders import build_concept

st.title("✏️ Edit Concept")

# Get list of concepts
concepts = [d.name for d in list_dir("concepts") if d.type == "dir"]

if not concepts:
    st.warning("⚠️ No concepts found. Create a concept first!")
    st.stop()

# Select concept
concept = st.selectbox("Select Concept", concepts, help="Choose a concept to edit")

if concept:
    try:
        # Read existing content
        text, sha = read_file(f"concepts/{concept}/content.md")
        
        # Parse content
        parts = text.split("## 🔗 Related Problems")
        desc = parts[0].replace(f"# {concept.replace('-', ' ').title()}", "").strip()
        
        urls = []
        if len(parts) > 1:
            urls = [
                u.strip("- ").strip()
                for u in parts[1].strip().splitlines()
                if u.strip() and u.strip() != ""
            ]
        
        # Initialize session state
        if "edit_urls" not in st.session_state or st.session_state.get("current_concept") != concept:
            st.session_state.edit_urls = urls.copy()
            st.session_state.current_concept = concept
        
        # Description editor
        st.subheader("Description")
        description = st.text_area(
            "Edit Description",
            value=desc,
            height=200,
            label_visibility="collapsed"
        )
        
        # URL management
        st.subheader("Related Problems")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            new_url = st.text_input("Add URL", placeholder="https://leetcode.com/problems/...")
        with col2:
            st.write("")  # Spacing
            st.write("")  # Spacing
            if st.button("➕ Add", disabled=not new_url.strip()):
                if new_url.strip() and new_url.strip() not in st.session_state.edit_urls:
                    st.session_state.edit_urls.append(new_url.strip())
                    st.rerun()
        
        # Display current URLs
        if st.session_state.edit_urls:
            st.write("**Current URLs:**")
            for i, u in enumerate(st.session_state.edit_urls):
                col_url, col_remove = st.columns([5, 1])
                with col_url:
                    st.text(f"• {u}")
                with col_remove:
                    if st.button("🗑️", key=f"remove_{i}"):
                        st.session_state.edit_urls.pop(i)
                        st.rerun()
        else:
            st.info("No URLs added yet")
        
        # Save button
        st.markdown("---")
        
        col_save, col_reset = st.columns([1, 1])
        
        with col_save:
            if st.button("💾 Save Changes", type="primary", disabled=not description.strip()):
                try:
                    content = build_concept(
                        concept.replace("-", " ").title(),
                        description,
                        st.session_state.edit_urls,
                    )
                    update_file(
                        f"concepts/{concept}/content.md",
                        content,
                        sha,
                        f"Update concept: {concept}",
                    )
                    st.success(f"✅ Concept '{concept}' updated successfully!")
                    # Reset state
                    del st.session_state.edit_urls
                    del st.session_state.current_concept
                except Exception as e:
                    st.error(f"❌ Error updating concept: {str(e)}")
        
        with col_reset:
            if st.button("🔄 Reset to Original"):
                st.session_state.edit_urls = urls.copy()
                st.rerun()
                
    except Exception as e:
        st.error(f"❌ Error loading concept: {str(e)}")
