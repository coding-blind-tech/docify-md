# Docify MD

A program to convert markdown documents into either PDF or Word document formats. This project simplifies the process of transforming a markdown file into a professional-looking document using a Docker container, making it lightweight and easy to use across various platforms.

## Features
- Convert Markdown files (`.md`) to **PDF** or **Word** (`.docx`) documents.
- Easy setup using **Docker**, ensuring compatibility across different systems.
- Support for custom styling via LaTeX for PDFs.

## How to Use

This program is simple to use. You first need to build the Docker image, and then run the container with the necessary arguments to convert your Markdown file into either a PDF or Word document. 

### Step-by-Step Instructions:
1. **Build the Docker Image**:
    ```bash
    docker build -t markdown-to-pdf .
    ```

2. **Run the Docker Container**:
    - For **Word document** (`.docx`) output:
      ```bash
      docker run --rm -v $(pwd):/app markdown-to-pdf input.md output.docx docx
      ```
    - For **PDF** output:
      ```bash
      docker run --rm -v $(pwd):/app markdown-to-pdf input.md output.pdf pdf
      ```

### Arguments:
- `input.md`: The path to the markdown file you want to convert.
- `output.docx` or `output.pdf`: The path and name of the resulting Word or PDF document.
- `docx` or `pdf`: The output format you wish to create.

## How to Contribute

We welcome contributions to improve this project. Here’s how you can set up your development environment and start contributing.

### Development Setup:

1. **Install Python 3.10**: Ensure that Python 3.10 or higher is installed on your system.
   
2. **Install Pipenv**: This project uses `pipenv` for managing dependencies and virtual environments. You can install `pipenv` by running:
    ```bash
    pip install pipenv
    ```

3. **Set up the Virtual Environment**:
    - Navigate to the root of the project directory.
    - Activate the virtual environment:
      ```bash
      pipenv shell
      ```

4. **Install Dependencies**:
    ```bash
    pipenv install
    ```

5. **Run the Program**:
    - You can test the program locally by running:
      ```bash
      python main.py
      ```

### Contribution Guidelines:

- Please **open an issue** to discuss any significant changes before submitting a pull request.
- For minor issues or improvements, feel free to submit pull requests directly.
- Ensure that the code is well-documented and adheres to Python’s PEP 8 guidelines.

## Reporting Issues

If you find a bug or have any problems using the project, please **open an issue** on the GitHub repository. Include any relevant details, including:
- Operating system and version
- Steps to reproduce the issue
- Logs or error messages, if applicable

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors of open-source libraries and tools used in this project, including **pandoc**, **XeLaTeX**, and others.
- Inspired by the need for simple markdown conversion for technical documentation.

Happy coding!
