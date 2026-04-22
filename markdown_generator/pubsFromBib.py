#!/usr/bin/env python
# coding: utf-8
"""
Generate paper markdown files from BibTeX sources.
"""

import html
import re
from pathlib import Path
from time import strptime

from pybtex.database.input import bibtex

from utils import build_yaml_front_matter, ensure_dir, html_escape, optional_text, write_markdown

OUTPUT_DIR = Path("../_papers")

PUBLICATION_TYPES = {
    "proceeding": {
        "file": "proceedings.bib",
        "venue_key": "booktitle",
        "venue_prefix": "In the proceedings of ",
    },
    "journal": {
        "file": "pubs.bib",
        "venue_key": "journal",
        "venue_prefix": "",
    },
}


def parse_date(fields: dict) -> str:
    """Convert BibTeX date fields into YYYY-MM-DD format."""
    pub_year = fields.get("year", "1900")
    pub_month = "01"
    pub_day = "01"

    if "month" in fields:
        month_val = str(fields["month"])
        if len(month_val) < 3:
            pub_month = f"0{month_val}"[-2:]
        elif not month_val.isdigit():
            try:
                pub_month = f"{strptime(month_val[:3], '%b').tm_mon:02d}"
            except ValueError:
                pub_month = "01"
        else:
            pub_month = month_val.zfill(2)

    if "day" in fields:
        pub_day = str(fields["day"]).zfill(2)

    return f"{pub_year}-{pub_month}-{pub_day}"


def clean_bibtex_text(text: str) -> str:
    """Remove a few BibTeX formatting characters from plain text fields."""
    return text.replace("{", "").replace("}", "").replace("\\", "")


def generate_url_slug(title: str) -> str:
    """Build a filesystem-safe slug from a BibTeX title."""
    clean_title = clean_bibtex_text(title).replace(" ", "-")
    slug = re.sub(r"\[.*?\]|[^a-zA-Z0-9_-]", "", clean_title)
    return slug.replace("--", "-").strip("-").lower()


def build_citation(bib_id: str, bibdata, pubsource: str, pub_year: str) -> str:
    """Construct a readable citation string."""
    entry = bibdata.entries[bib_id]
    fields = entry.fields
    authors = []

    if "author" in entry.persons:
        for author in entry.persons["author"]:
            first_name = author.first_names[0] if author.first_names else ""
            last_name = author.last_names[0] if author.last_names else ""
            full_name = f"{first_name} {last_name}".strip()
            if full_name:
                authors.append(full_name)

    citation = ", ".join(authors)
    if citation:
        citation += ", "

    title = clean_bibtex_text(fields["title"])
    venue_key = PUBLICATION_TYPES[pubsource]["venue_key"]
    venue_prefix = PUBLICATION_TYPES[pubsource]["venue_prefix"]
    venue = venue_prefix + clean_bibtex_text(fields[venue_key])

    return f'{citation}"{html_escape(title)}." {html_escape(venue)}, {pub_year}.'


def generate_bib_markdown(bib_id: str, bibdata, pubsource: str) -> tuple[str, str]:
    """Generate a markdown file name and body for one BibTeX entry."""
    entry = bibdata.entries[bib_id]
    fields = entry.fields

    pub_date = parse_date(fields)
    pub_year = int(fields.get("year", "1900"))
    url_slug = generate_url_slug(fields["title"])
    md_filename = f"{pub_date}-{url_slug}.md"

    citation = build_citation(bib_id, bibdata, pubsource, str(pub_year))
    note = optional_text(fields.get("note"))
    url = optional_text(fields.get("url"))
    venue_key = PUBLICATION_TYPES[pubsource]["venue_key"]
    venue_prefix = PUBLICATION_TYPES[pubsource]["venue_prefix"]
    venue = venue_prefix + clean_bibtex_text(fields[venue_key])

    yaml_data = {
        "title": clean_bibtex_text(fields["title"]),
        "collection": "papers",
        "permalink": f"/papers/{url_slug}/",
        "date": pub_date,
        "year": pub_year,
        "venue": venue,
        "paperurl": url,
        "citation": citation,
        "excerpt": note,
    }

    content = [build_yaml_front_matter(yaml_data)]

    if note:
        content.append(html_escape(note))

    if url:
        content.append(f'[Access paper here]({url}){{:target="_blank"}}')
    else:
        search_title = clean_bibtex_text(fields["title"]).replace("-", "+")
        content.append(
            f'Use [Google Scholar](https://scholar.google.com/scholar?q={html.escape(search_title)}){{:target="_blank"}} for full citation'
        )

    return md_filename, "\n\n".join(content) + "\n"


def main() -> None:
    """Generate markdown files from all configured BibTeX sources."""
    output_dir = ensure_dir(OUTPUT_DIR)
    success_count = 0
    warning_count = 0

    for pubsource, config in PUBLICATION_TYPES.items():
        parser = bibtex.Parser()
        bibdata = parser.parse_file(config["file"])

        for bib_id in bibdata.entries:
            try:
                md_filename, md_content = generate_bib_markdown(bib_id, bibdata, pubsource)
                write_markdown(output_dir, md_filename, md_content)

                title = bibdata.entries[bib_id].fields["title"]
                display_title = title[:60] + "..." if len(title) > 60 else title
                print(f'SUCCESSFULLY PARSED {bib_id}: "{display_title}"')
                success_count += 1
            except KeyError as exc:
                title = bibdata.entries[bib_id].fields.get("title", "Unknown")
                display_title = title[:30] + "..." if len(title) > 30 else title
                print(f'WARNING Missing Expected Field {exc} from entry {bib_id}: "{display_title}"')
                warning_count += 1

    print(f"\nSummary: {success_count} successful, {warning_count} warnings")


if __name__ == "__main__":
    main()
