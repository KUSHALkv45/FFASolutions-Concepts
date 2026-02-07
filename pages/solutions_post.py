"""Page for posting new solutions."""
import streamlit as st
import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.github_ops import list_dir, create_file
from utils.builders import build_full_solution

st.title("➕ Post New Solution")

# Category selection
st.subheader("Category")
cats = [d.name for d in list_dir("solutions") if d.type == "dir"]
category_options = cats + ["➕ Add new category"]
category = st.selectbox("Select Category", category_options)

if category == "➕ Add new category":
    category = st.text_input(
        "New Category Name",
        placeholder="e.g., dp, greedy, graphs",
        help="Use lowercase and hyphens for multi-word categories"
    )
    if category:
        category = category.lower().replace(" ", "-")

# Solution details
st.subheader("Solution Details")
title = st.text_input(
    "Solution Title",
    placeholder="e.g., Two Sum, Longest Palindromic Substring",
    help="Enter a descriptive title for the solution"
)

slug = title.lower().replace(" ", "-") if title else ""
if slug and category:
    st.caption(f"📁 Will be saved as: `solutions/{category}/{slug}/`")

# Section inputs
st.subheader("Solution Sections")

with st.expander("💡 Idea (Required)", expanded=True):
    idea = st.text_area(
        "Describe the core idea/approach",
        height=150,
        key="idea",
        label_visibility="collapsed"
    )

with st.expander("🔍 Simple Algorithm Trace (Optional)"):
    trace = st.text_area(
        "Walk through the algorithm with a simple example",
        height=150,
        key="trace",
        label_visibility="collapsed"
    )

with st.expander("⏱️ Time & Space Complexity (Optional)"):
    complexity = st.text_area(
        "Analyze time and space complexity",
        height=100,
        key="complexity",
        label_visibility="collapsed"
    )

with st.expander("💻 Code (Optional)"):
    code = st.text_area(
        "Paste the solution code (Python)",
        height=300,
        key="code",
        label_visibility="collapsed"
    )

# Submit button
st.markdown("---")

# Validation - only require title, category, and idea
has_required = title and category and idea

if st.button("🚀 Post Solution", type="primary", disabled=not has_required):
    if not title.strip():
        st.error("❌ Title is required")
    elif not category.strip():
        st.error("❌ Category is required")
    elif not idea.strip():
        st.error("❌ Idea section is required")
    else:
        try:
            base = f"solutions/{category}/{slug}"
            sections = {
                "idea": idea,
                "trace": trace,
                "complexity": complexity,
                "code": code,
            }
            
            # Create individual section files ONLY for non-empty sections
            files_created = []
            for key, content in sections.items():
                if content and content.strip():
                    create_file(f"{base}/.sections/{key}.md", content, f"Add {key} for {title}")
                    files_created.append(key)
            
            # Create full solution file with only the sections that have content
            # Pass empty string for missing sections to build_full_solution
            full = build_full_solution(title, sections)
            create_file(f"{base}/full.md", full, f"Add solution: {title}")
            
            st.success(f"✅ Solution '{title}' posted successfully!")
            st.info(f"📄 Created files: {', '.join(files_created + ['full'])}")
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ Error posting solution: {str(e)}")

# Help section
with st.expander("ℹ️ Help"):
    st.markdown("""
    **Required fields:**
    - Title
    - Category
    - Idea (at least this section must be filled)
    
    **Optional sections:**
    - Trace: Walk through with an example
    - Complexity: Big O analysis
    - Code: Implementation
    
    You can leave optional sections empty and fill them later using the Edit page.
    All sections will be combined into a `editorial.md` file automatically.
    """)
