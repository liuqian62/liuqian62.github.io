#!/usr/bin/env python
# coding: utf-8
"""
Generate talk markdown files from a TSV file.
"""

from pathlib import Path

import pandas as pd

from utils import build_yaml_front_matter, ensure_dir, html_escape, optional_text, write_markdown

OUTPUT_DIR = Path("../_talks")


def generate_talk_markdown(row) -> str:
    """Generate one markdown document for a talk entry."""
    talk_date = str(row.date)
    url_slug = row.url_slug
    venue = optional_text(row.venue)
    location = optional_text(row.location)
    talk_url = optional_text(row.talk_url)
    description = optional_text(row.description)

    yaml_data = {
        "title": row.title,
        "collection": "talks",
        "type": row.type if pd.notna(row.type) and len(str(row.type)) > 3 else "Talk",
        "permalink": f"/talks/{talk_date}-{url_slug}",
        "date": talk_date,
        "venue": venue,
        "location": location,
    }

    content = [build_yaml_front_matter(yaml_data)]

    if talk_url:
        content.append(f"[More information here]({talk_url})")

    if description:
        content.append(html_escape(description))

    return "\n\n".join(content) + "\n"


def main() -> None:
    """Read the TSV file and generate talk markdown files."""
    talks = pd.read_csv("talks.tsv", sep="\t", header=0)
    output_dir = ensure_dir(OUTPUT_DIR)

    for _, item in talks.iterrows():
        md_filename = f"{item.date}-{item.url_slug}.md"
        md_content = generate_talk_markdown(item)
        write_markdown(output_dir, md_filename, md_content)

    print(f"Successfully generated {len(talks)} talk files in {output_dir}")


if __name__ == "__main__":
    main()
