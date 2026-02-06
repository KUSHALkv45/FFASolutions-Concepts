SECTIONS = ["idea", "trace", "complexity", "code"]

def build_full(title, section_map):
    md = f"# {title}\n\n"

    for sec, text in section_map.items():
        if text.strip():
            md += f"## {sec.title()}\n{text}\n\n"

    return md
