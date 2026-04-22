#!/usr/bin/env python
# coding: utf-8
"""
Shared helpers for markdown generation scripts.
"""

from pathlib import Path
from typing import Any, Dict, Optional

HTML_ESCAPE_TABLE = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
}


def html_escape(text: Optional[str]) -> str:
    """Escape the small subset of characters we emit into YAML/HTML."""
    if not text:
        return ""
    return "".join(HTML_ESCAPE_TABLE.get(char, char) for char in text)


def ensure_dir(path: Path) -> Path:
    """Create a directory if it does not already exist."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_markdown(output_dir: Path, filename: str, content: str) -> None:
    """Write a UTF-8 markdown file into the target directory."""
    filepath = output_dir / filename
    filepath.write_text(content, encoding="utf-8")


def build_yaml_front_matter(data: Dict[str, Any]) -> str:
    """Build YAML front matter while skipping empty values."""
    lines = ["---"]
    for key, value in data.items():
        if value is None or value == "":
            continue
        if isinstance(value, str):
            lines.append(f'{key}: "{html_escape(value)}"')
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def optional_text(value: Any) -> str:
    """Return a normalized optional string value."""
    if value is None:
        return ""

    text = str(value).strip()
    if text.lower() == "nan":
        return ""
    return text
