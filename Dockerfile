FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-full \
        pandoc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install pipenv
RUN pip install pipenv

RUN apt-get install -y fonts-lmodern

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Install Python dependencies
RUN pipenv install --deploy --ignore-pipfile


# This Dockerfile sets the entrypoint for the container.
# Set the entrypoint
ENTRYPOINT ["pipenv", "run", "python", "main.py"]