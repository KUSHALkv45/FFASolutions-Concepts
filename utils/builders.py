SECTION_TITLES = {
    "idea": "💡 Idea",
    "trace": "🔍 Simple Algorithm Trace",
    "complexity": "⏱️ Time & Space Complexity",
    "code": "💻 Code",
}


def build_full_solution(title, sections):
    md = f"# {title}\n\n"

    for key, content in sections.items():
        if content.strip():
            md += f"## {SECTION_TITLES[key]}\n"
            if key == "code":
                md += f"```python\n{content}\n```\n\n"
            else:
                md += f"{content}\n\n"

    return md


def build_concept(title, description, urls):
    md = f"# {title}\n\n{description}\n\n"

    if urls:
        md += "## 🔗 Related Problems\n"
        for u in urls:
            md += f"- {u}\n"

    return md
