"""Page for editing existing solutions."""

import streamlit as st
from utils.github_ops import list_dir, read_file, update_file
from utils.builders import build_full_solution

st.title("✏️ Edit Solution")

# Category selection
cats = [d.name for d in list_dir("solutions") if d.type == "dir"]

if not cats:
    st.warning("⚠️ No solution categories found. Create a solution first!")
    st.stop()

category = st.selectbox("Category", cats, help="Select a category")

# Solution selection
if category:
    solutions = [d.name for d in list_dir(f"solutions/{category}") if d.type == "dir"]
    
    if not solutions:
        st.warning(f"⚠️ No solutions found in category '{category}'")
        st.stop()
    
    solution = st.selectbox("Solution", solutions, help="Select a solution to edit")
    
    if solution:
        st.caption(f"📁 Editing: `solutions/{category}/{solution}/`")
        
        # Section selection
        sections = ["idea", "trace", "complexity", "code"]
        section = st.selectbox(
            "Section to Edit",
            sections,
            format_func=lambda x: {
                "idea": "💡 Idea",
                "trace": "🔍 Simple Algorithm Trace",
                "complexity": "⏱️ Time & Space Complexity",
                "code": "💻 Code"
            }[x]
        )
        
        # Read section content
        path = f"solutions/{category}/{solution}/.sections/{section}.md"
        
        try:
            content, sha = read_file(path)
        except Exception:
            content = ""
            sha = None
            st.info(f"ℹ️ Section '{section}' doesn't exist yet. You can create it below.")
        
        # Editor
        st.subheader(f"Edit {section.title()} Section")
        
        # Adjust height based on section type
        height = 300 if section == "code" else 200
        
        text = st.text_area(
            "Content",
            value=content,
            height=height,
            label_visibility="collapsed",
            help="Edit the section content"
        )
        
        # Save button
        st.markdown("---")
        
        col_save, col_preview = st.columns([1, 1])
        
        with col_save:
            if st.button("💾 Save Section", type="primary", disabled=not text.strip()):
                try:
                    if sha:
                        # Update existing file
                        update_file(path, text, sha, f"Update {section} for {solution}")
                    else:
                        # Create new file
                        from utils.github_ops import create_file
                        create_file(path, text, f"Add {section} for {solution}")
                    
                    # Rebuild full solution
                    all_sections = {}
                    for s in sections:
                        try:
                            section_content, _ = read_file(f"solutions/{category}/{solution}/.sections/{s}.md")
                            all_sections[s] = section_content
                        except Exception:
                            all_sections[s] = ""
                    
                    # Update the current section with new content
                    all_sections[section] = text
                    
                    title = solution.replace("-", " ").title()
                    full = build_full_solution(title, all_sections)
                    
                    # Update editorial.md
                    full_path = f"solutions/{category}/{solution}/editorial.md"
                    try:
                        _, full_sha = read_file(full_path)
                        update_file(full_path, full, full_sha, f"Rebuild full solution for {solution}")
                    except Exception:
                        # full.md doesn't exist, create it
                        from utils.github_ops import create_file
                        create_file(full_path, full, f"Create full solution for {solution}")
                    
                    st.success(f"✅ Section '{section}' saved and full solution rebuilt!")
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error saving section: {str(e)}")
        
        with col_preview:
            if st.button("👁️ Preview Full Solution"):
                st.session_state.show_preview = not st.session_state.get("show_preview", False)
                st.rerun()
        
        # Preview
        if st.session_state.get("show_preview", False):
            st.markdown("---")
            st.subheader("Full Solution Preview")
            
            try:
                all_sections = {}
                for s in sections:
                    try:
                        section_content, _ = read_file(f"solutions/{category}/{solution}/{s}.md")
                        all_sections[s] = section_content
                    except Exception:
                        all_sections[s] = ""
                
                # Include current edits
                all_sections[section] = text
                
                title = solution.replace("-", " ").title()
                full = build_full_solution(title, all_sections)
                
                st.markdown(full)
                
            except Exception as e:
                st.error(f"❌ Error generating preview: {str(e)}")
