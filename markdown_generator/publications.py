#!/usr/bin/env python
# coding: utf-8
"""
Publications markdown generator for academicpages

Takes a TSV of publications with metadata and converts them for use with academicpages.github.io

Data format:
The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top.
- excerpt and paper_url can be blank, but the others must have values.
- pub_date must be formatted as YYYY-MM-DD.
- url_slug will be the descriptive part of the .md file and the permalink URL.
"""

import pandas as pd
from pathlib import Path
from utils import html_escape, ensure_dir, write_markdown


def generate_publication_markdown(row) -> str:
    """生成单篇 publication 的 Markdown 内容"""
    pub_date = str(row.pub_date)
    year = pub_date[:4]
    url_slug = row.url_slug
    
    # YAML Front Matter
    yaml_data = {
        'title': row.title,
        'collection': 'publications',
        'permalink': f'/publication/{pub_date}-{url_slug}',
        'date': pub_date,
        'venue': row.venue,
    }
    
    # 可选字段
    excerpt = str(row.excerpt) if pd.notna(row.excerpt) else ""
    if len(excerpt) > 5:
        yaml_data['excerpt'] = excerpt
    
    paper_url = str(row.paper_url) if pd.notna(row.paper_url) else ""
    if len(paper_url) > 5:
        yaml_data['paperurl'] = paper_url
    
    yaml_data['citation'] = row.citation
    
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
    if len(paper_url) > 5:
        md += f"\n\n<a href='{paper_url}'>Download paper here</a>\n"
    
    if len(excerpt) > 5:
        md += f"\n{html_escape(excerpt)}\n"
    
    md += f"\nRecommended citation: {row.citation}"
    
    return md


def main():
    # 读取 TSV
    publications = pd.read_csv("publications.tsv", sep="\t", header=0)
    
    # 确保输出目录存在
    output_dir = ensure_dir(Path("../_publications"))
    
    # 生成 Markdown 文件
    for _, item in publications.iterrows():
        md_filename = f"{item.pub_date}-{item.url_slug}.md"
        md_content = generate_publication_markdown(item)
        write_markdown(output_dir, md_filename, md_content)
    
    print(f"Successfully generated {len(publications)} publication files")


if __name__ == "__main__":
    main()
