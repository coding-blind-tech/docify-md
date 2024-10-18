# Mark Down to PDF or Word Document

A program to convert markdown document to PDF or Word document.

## How to use?

This program is very simple to use. You first build the docker image and then run the docker run command with the arguments you choose. With this, you can take a markdown document and either create a pdf or word document depending on the arguments given.

docker build -t markdown-to-pdf .
docker run --rm -v $(pwd):/app markdown-to-pdf input.md output.docx docx

## How to Contribute?

To setup the development enviromnet, you will need to do the following:

1. Make sure that you have python installed and you have the python version 3.10 installed.
2. Run pipenv shell from the root of the directory.
3. Run pipenv install to install the needed dependencies.
4. To run the program run python main.py
5. Happy coding!
