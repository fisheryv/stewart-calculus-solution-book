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

DOC_DIR = "docs"
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


def _write_directory_structure(root_dir, output_file, level: int = 0, index: int = 0):
    """Recursively writes the directory structure to a text file.
    :param root_dir: The root directory to traverse
    :param output_file: The output file object
    :param level: Current nesting level
    :param index: Parent directory index
    """
    # List the contents of the current directory (ignore access errors)
    try:
        entries = os.listdir(root_dir)
    except PermissionError:
        print(f"Permission denied: {root_dir}")
        return
    except FileNotFoundError:
        print(f"Directory not found: {root_dir}")
        return

    # Sort by length and alphabetical order, directories first
    entries.sort(
        key=lambda e: (
            not os.path.isdir(os.path.join(root_dir, e)),
            (len(e), e.lower()),
        )
    )

    indent = "\t" * level  # Indent strings
    for i, entry in enumerate(entries, start=1):
        full_path = os.path.join(root_dir, entry)

        if os.path.isdir(full_path):
            if level == 0:
                item = f"Ch {i}. {CHAPTER_TITLES[i - 1]}"
            else:
                item = f"Section {index}.{i}"
            # Write directory entry
            output_file.write(f"{indent}- {item}\n")
            # Process subdirectories recursively with increased indentation
            _write_directory_structure(full_path, output_file, level + 1, i)
        else:
            # Write file entry
            item = full_path[full_path.find(DOC_DIR) :]  # Get the relative path portion
            item = item.replace("\\", "/")  # Replace backslashes with slashes
            output_file.write(f"{indent}- [Problem {i}](/{item})\n")


def generate_toc():
    """Generate the table of contents and write it to the output file."""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("- [Home](/README.md)\n")
        # Get the absolute path of the current script
        root_path = Path(__file__).resolve().parent
        docs_path = os.path.join(root_path, DOC_DIR)
        # Start recursive traversal
        _write_directory_structure(docs_path, f)


if __name__ == "__main__":
    generate_toc()
