#!/usr/bin/env python
# coding: utf-8
"""
Talks markdown generator for academicpages

Takes a TSV of talks with metadata and converts them for use with academicpages.github.io

Data format:
The TSV needs to have the following columns: title, type, url_slug, venue, date, location, talk_url, description, with a header at the top.
- Fields that cannot be blank: title, url_slug, date. All else can be blank. type defaults to "Talk"
- date must be formatted as YYYY-MM-DD.
- url_slug will be the descriptive part of the .md file and the permalink URL.
"""

import pandas as pd
from pathlib import Path
from utils import html_escape, ensure_dir, write_markdown


def generate_talk_markdown(row) -> str:
    """生成单个 talk 的 Markdown 内容"""
    talk_date = str(row.date)
    url_slug = row.url_slug
    
    # YAML Front Matter
    yaml_data = {
        'title': row.title,
        'collection': 'talks',
        'type': row.type if pd.notna(row.type) and len(str(row.type)) > 3 else 'Talk',
        'permalink': f'/talks/{talk_date}-{url_slug}',
    }
    
    # 可选字段
    venue = str(row.venue) if pd.notna(row.venue) else ""
    if len(venue) > 3:
        yaml_data['venue'] = venue
    
    location = str(row.location) if pd.notna(row.location) else ""
    if len(location) > 3:
        yaml_data['date'] = talk_date
        yaml_data['location'] = location
    
    # 构建 YAML
    md_lines = ["---"]
    for key, value in yaml_data.items():
        if isinstance(value, str):
            md_lines.append(f'{key}: "{html_escape(value)}"')
        else:
            md_lines.append(f'{key}: {value}')
    md_lines.append("---")
    
    md = "\n".join(md_lines) + "\n"
    
    # Markdown 内容
    talk_url = str(row.talk_url) if pd.notna(row.talk_url) else ""
    if len(talk_url) > 3:
        md += f"\n[More information here]({talk_url})\n"
    
    description = str(row.description) if pd.notna(row.description) else ""
    if len(description) > 3:
        md += f"\n{html_escape(description)}\n"
    
    return md


def main():
    # 读取 TSV
    talks = pd.read_csv("talks.tsv", sep="\t", header=0)
    
    # 确保输出目录存在
    output_dir = ensure_dir(Path("../_talks"))
    
    # 生成 Markdown 文件
    for _, item in talks.iterrows():
        md_filename = f"{item.date}-{item.url_slug}.md"
        md_content = generate_talk_markdown(item)
        write_markdown(output_dir, md_filename, md_content)
    
    print(f"Successfully generated {len(talks)} talk files")


if __name__ == "__main__":
    main()
