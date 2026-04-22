#!/usr/bin/env python
# coding: utf-8
"""
Generate paper markdown files from a TSV file.

Expected columns:
- pub_date (YYYY-MM-DD)
- title
- venue
- excerpt
- citation
- url_slug
- paper_url
"""

from pathlib import Path

import pandas as pd

from utils import build_yaml_front_matter, ensure_dir, html_escape, optional_text, write_markdown

OUTPUT_DIR = Path("../_papers")
COLLECTION = "papers"
PERMALINK_PREFIX = "/papers/"


def generate_publication_markdown(row) -> str:
    """Generate one markdown document for a paper entry."""
    pub_date = str(row.pub_date)
    year = int(pub_date[:4])
    url_slug = row.url_slug

    excerpt = optional_text(row.excerpt)
    paper_url = optional_text(row.paper_url)
    citation = optional_text(row.citation)

    yaml_data = {
        "title": row.title,
        "collection": COLLECTION,
        "permalink": f"{PERMALINK_PREFIX}{url_slug}/",
        "date": pub_date,
        "year": year,
        "venue": row.venue,
        "paperurl": paper_url,
        "citation": citation,
        "excerpt": excerpt,
    }

    content = [build_yaml_front_matter(yaml_data)]

    if paper_url:
        content.append(f"<a href='{paper_url}'>Download paper here</a>")

    if excerpt:
        content.append(html_escape(excerpt))

    if citation:
        content.append(f"Recommended citation: {html_escape(citation)}")

    return "\n\n".join(content) + "\n"


def main() -> None:
    """Read the TSV file and generate paper markdown files."""
    publications = pd.read_csv("publications.tsv", sep="\t", header=0)
    output_dir = ensure_dir(OUTPUT_DIR)

    for _, item in publications.iterrows():
        md_filename = f"{item.pub_date}-{item.url_slug}.md"
        md_content = generate_publication_markdown(item)
        write_markdown(output_dir, md_filename, md_content)

    print(f"Successfully generated {len(publications)} paper files in {output_dir}")


if __name__ == "__main__":
    main()
