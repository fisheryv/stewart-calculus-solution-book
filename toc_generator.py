"""Automatically generate the table of contents (_sidebar.md).

This script scans the project directory for markdown files and
generates a hierarchical table of contents in the _sidebar.md file.

The directory structure is as follows:
docs/
  ├── ch*/
      ├── section*/
          ├── Problem*.md
"""

import os
from pathlib import Path

OUTPUT_FILE = "_sidebar1.md"
CHAPTER_TITLES = [
    "Functions and Models",
    "Limits and Derivatives",
    "Differentiation Rules",
    "Applications of Differentiation",
    "Integrals",
    "Applications of Integration",
    "Techniques of Integration",
    "Further Applications of Integration",
    "Differential Equations",
    "Parametric Equations and Polar Coordinates",
    "Infinite Sequences and Series",
]


def _write_directory_structure(root_dir: str, output_file, indent: str = ""):
    """
    递归写入目录结构到文本文件
    :param root_dir: 要遍历的根目录
    :param output_file: 输出的文件对象
    :param indent: 当前层级的缩进字符串
    """
    # 列出当前目录内容（忽略访问错误）
    try:
        entries = os.listdir(root_dir)
    except PermissionError:
        print(f"Permission denied: {root_dir}")
        return
    except FileNotFoundError:
        print(f"Directory not found: {root_dir}")
        return

    # 按长度和字母顺序排序，目录优先
    entries.sort(
        key=lambda e: (
            not os.path.isdir(os.path.join(root_dir, e)),
            (len(e), e.lower()),
        )
    )

    for i, entry in enumerate(entries):
        full_path = os.path.join(root_dir, entry)
        # is_last = i == len(entries) - 1

        if os.path.isdir(full_path):
            # 写入目录项
            output_file.write(f"{indent}- {entry}\n")
            # 递归处理子目录，增加缩进
            next_indent = indent + ("\t")
            _write_directory_structure(full_path, output_file, next_indent)
        else:
            # 写入文件项
            output_file.write(f"{indent}- [{entry}]({full_path})\n")


def generate_toc():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("- [Home](/README.md)\n")
        # 获取当前脚本的绝对路径
        root_path = Path(__file__).resolve().parent
        docs_path = os.path.join(root_path, "docs")
        # 开始递归遍历
        _write_directory_structure(docs_path, f)


if __name__ == "__main__":
    generate_toc()
