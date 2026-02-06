"""Content builders for generating markdown files."""

SECTION_TITLES = {
    "idea": "💡 Idea",
    "trace": "🔍 Simple Algorithm Trace",
    "complexity": "⏱️ Time & Space Complexity",
    "code": "💻 Code",
}


def build_full_solution(title, sections):
    """
    Build a complete solution markdown file from sections.
    
    Args:
        title: Solution title
        sections: Dict mapping section keys to content
        
    Returns:
        Formatted markdown string
    """
    md = f"# {title}\n\n"
    
    for key, content in sections.items():
        if content and content.strip():
            md += f"## {SECTION_TITLES[key]}\n\n"
            
            if key == "code":
                md += f"```python\n{content.strip()}\n```\n\n"
            else:
                md += f"{content.strip()}\n\n"
    
    return md


def build_concept(title, description, urls):
    """
    Build a concept markdown file.
    
    Args:
        title: Concept title
        description: Concept description
        urls: List of related problem URLs
        
    Returns:
        Formatted markdown string
    """
    md = f"# {title}\n\n{description.strip()}\n\n"
    
    if urls:
        md += "## 🔗 Related Problems\n\n"
        for url in urls:
            if url.strip():
                md += f"- {url.strip()}\n"
    
    return md
