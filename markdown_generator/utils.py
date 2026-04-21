#!/usr/bin/env python
# coding: utf-8
"""
公共工具模块，提供 HTML 转义和 Markdown 生成功能
"""

from pathlib import Path
from typing import Optional, Dict, Any

HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}


def html_escape(text: Optional[str]) -> str:
    """转义 HTML 特殊字符"""
    if not text:
        return ""
    return "".join(HTML_ESCAPE_TABLE.get(c, c) for c in text)


def ensure_dir(path: Path) -> Path:
    """确保目录存在，如果不存在则创建"""
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_markdown(output_dir: Path, filename: str, content: str) -> None:
    """写入 Markdown 文件"""
    filepath = output_dir / filename
    filepath.write_text(content, encoding='utf-8')


def build_yaml_front_matter(data: Dict[str, Any]) -> str:
    """构建 YAML Front Matter"""
    lines = ["---"]
    for key, value in data.items():
        if value is not None and value != "":
            if isinstance(value, str):
                lines.append(f'{key}: "{html_escape(value)}"')
            else:
                lines.append(f'{key}: {value}')
    lines.append("---")
    return "\n".join(lines)
