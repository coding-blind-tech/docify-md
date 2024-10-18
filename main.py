"""This script converts a markdown file to a specified output format
(PDF or DOCX) using pypandoc.

Functions:
    normalize_text(md_file_path):
        Reads a markdown file, normalizes its content
        to remove special  characters, and returns the normalized content.

    convert_md(md_file_path, output_file_path, output_format):
        Converts a markdown file
        to the specified output format
        (PDF or DOCX) after normalizing its content.
        Parameters:
            md_file_path (str): Path to the input markdown file.
            output_file_path (str): Path to the output file.
            output_format (str): Desired output format ('pdf' or 'docx').

Usage:
    Run the script from the command line with the following arguments:
        python main.py <input_md_file> <output_file> <output_format>
    Example:
        python main.py example.md example.pdf pdf
"""

import sys
import pypandoc
import unicodedata


def normalize_text(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Normalize the content to remove special characters
    normalized_content = unicodedata.normalize('NFKC', content)
    return normalized_content


def convert_md(md_file_path, output_file_path, output_format):
    extra_args = []

    if output_format == 'pdf':
        extra_args = [
            # Change to 'pdflatex' or 'lualatex' if needed
            '--pdf-engine=xelatex',
            '--variable', 'geometry:margin=1in',
        ]

    try:
        # Normalize the markdown content before conversion
        normalized_content = normalize_text(md_file_path)

        # Convert the normalized content
        output = pypandoc.convert_text(
            normalized_content,
            output_format,
            format='md',
            outputfile=output_file_path,
            extra_args=extra_args
        )
        return output
    except RuntimeError as e:
        print(f"An error occurred during conversion: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: python main.py <input_md_file> <output_file> "
            "<output_format>"
            )
        sys.exit(1)

    md_file_path = sys.argv[1]
    output_file_path = f"output/{sys.argv[2]}"
    output_format = sys.argv[3]  # 'pdf' or 'docx'

    convert_md(md_file_path, output_file_path, output_format)
