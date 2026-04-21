#!/usr/bin/env python
# coding: utf-8
"""
Publications markdown generator from BibTeX for academicpages

Takes a set of bibtex files and converts them for use with academicpages.github.io
"""

from pybtex.database.input import bibtex
from time import strptime
import re
import html
from pathlib import Path
from utils import html_escape, ensure_dir, write_markdown


# Publication type configurations
PUBLICATION_TYPES = {
    "proceeding": {
        "file": "proceedings.bib",
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of ",
        "collection": {"name": "publications", "permalink": "/publication/"}
    },
    "journal": {
        "file": "pubs.bib",
        "venuekey": "journal",
        "venue-pretext": "",
        "collection": {"name": "publications", "permalink": "/publication/"}
    }
}


def parse_date(fields: dict) -> str:
    """解析日期字段，返回 YYYY-MM-DD 格式"""
    pub_year = fields.get("year", "1900")
    pub_month = "01"
    pub_day = "01"
    
    if "month" in fields:
        month_val = str(fields["month"])
        if len(month_val) < 3:
            pub_month = f"0{month_val}"[-2:]
        elif not month_val.isdigit():
            try:
                tmnth = strptime(month_val[:3], '%b').tm_mon
                pub_month = f"{tmnth:02d}"
            except ValueError:
                pub_month = "01"
        else:
            pub_month = month_val.zfill(2)
    
    if "day" in fields:
        pub_day = str(fields["day"]).zfill(2)
    
    return f"{pub_year}-{pub_month}-{pub_day}"


def clean_bibtex_text(text: str) -> str:
    """清理 BibTeX 文本中的特殊字符"""
    return text.replace("{", "").replace("}", "").replace("\\", "")


def generate_url_slug(title: str) -> str:
    """从标题生成 URL slug"""
    clean_title = clean_bibtex_text(title).replace(" ", "-")
    url_slug = re.sub(r"\[.*?\]|[^a-zA-Z0-9_-]", "", clean_title)
    return url_slug.replace("--", "-")


def build_citation(bib_id: str, bibdata, pubsource: str, pub_year: str) -> str:
    """构建引用文本"""
    entry = bibdata.entries[bib_id]
    fields = entry.fields
    
    # 作者
    authors = []
    if "author" in entry.persons:
        for author in entry.persons["author"]:
            first_name = author.first_names[0] if author.first_names else ""
            last_name = author.last_names[0] if author.last_names else ""
            authors.append(f"{first_name} {last_name}")
    
    citation = ", ".join(authors)
    if citation:
        citation += ", "
    
    # 标题
    title = clean_bibtex_text(fields["title"])
    citation += f'"{html_escape(title)}."'
    
    # 期刊/会议
    venue_key = PUBLICATION_TYPES[pubsource]["venuekey"]
    venue_pretext = PUBLICATION_TYPES[pubsource]["venue-pretext"]
    venue = venue_pretext + clean_bibtex_text(fields[venue_key])
    citation += f" {html_escape(venue)}, {pub_year}."
    
    return citation


def generate_bib_markdown(bib_id: str, bibdata, pubsource: str) -> tuple:
    """生成单篇 BibTeX 论文的 Markdown 内容，返回 (filename, content)"""
    entry = bibdata.entries[bib_id]
    fields = entry.fields
    
    # 解析日期
    pub_date = parse_date(fields)
    pub_year = fields.get("year", "1900")
    
    # 生成文件名
    url_slug = generate_url_slug(fields["title"])
    md_filename = f"{pub_date}-{url_slug}.md".replace("--", "-")
    html_filename = f"{pub_date}-{url_slug}".replace("--", "-")
    
    # 构建引用
    citation = build_citation(bib_id, bibdata, pubsource, pub_year)
    
    # 清理标题
    clean_title = html_escape(clean_bibtex_text(fields["title"]))
    
    # YAML Front Matter
    yaml_data = {
        'title': clean_title,
        'collection': PUBLICATION_TYPES[pubsource]["collection"]["name"],
        'permalink': PUBLICATION_TYPES[pubsource]["collection"]["permalink"] + html_filename,
        'date': pub_date,
    }
    
    # 可选字段
    note = ""
    if "note" in fields:
        note = str(fields["note"])
        if len(note) > 5:
            yaml_data['excerpt'] = note
    
    venue = PUBLICATION_TYPES[pubsource]["venue-pretext"] + clean_bibtex_text(fields[PUBLICATION_TYPES[pubsource]["venuekey"]])
    yaml_data['venue'] = venue
    
    url = ""
    if "url" in fields:
        url = str(fields["url"])
        if len(url) > 5:
            yaml_data['paperurl'] = url
    
    yaml_data['citation'] = citation
    
    # 构建 YAML
    md_lines = ["---"]
    for key, value in yaml_data.items():
        if isinstance(value, str):
            md_lines.append(f'{key}: "{html_escape(value)}"')
        else:
            md_lines.append(f'{key}: {value}')
    md_lines.append("---")
    
    md = "\n".join(md_lines)
    
    # Markdown 内容
    if note and len(note) > 5:
        md += f"\n{html_escape(note)}\n"
    
    if url and len(url) > 5:
        md += f'\n[Access paper here]({url}){{:target="_blank"}}\n'
    else:
        search_title = clean_bibtex_text(fields["title"]).replace("-", "+")
        md += f'\nUse [Google Scholar](https://scholar.google.com/scholar?q={html.escape(search_title)}){{:target="_blank"}} for full citation'
    
    return md_filename, md


def main():
    output_dir = ensure_dir(Path("../_publications"))
    success_count = 0
    warning_count = 0
    
    for pubsource in PUBLICATION_TYPES:
        parser = bibtex.Parser()
        bibdata = parser.parse_file(PUBLICATION_TYPES[pubsource]["file"])
        
        for bib_id in bibdata.entries:
            try:
                md_filename, md_content = generate_bib_markdown(bib_id, bibdata, pubsource)
                write_markdown(output_dir, md_filename, md_content)
                
                title = bibdata.entries[bib_id].fields["title"]
                display_title = title[:60] + "..." if len(title) > 60 else title
                print(f'SUCCESSFULLY PARSED {bib_id}: "{display_title}"')
                success_count += 1
                
            except KeyError as e:
                title = bibdata.entries[bib_id].fields.get("title", "Unknown")
                display_title = title[:30] + "..." if len(title) > 30 else title
                print(f'WARNING Missing Expected Field {e} from entry {bib_id}: "{display_title}"')
                warning_count += 1
                continue
    
    print(f"\nSummary: {success_count} successful, {warning_count} warnings")


if __name__ == "__main__":
    main()
