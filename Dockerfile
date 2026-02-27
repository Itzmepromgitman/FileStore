# Use the slim version of Python 3.8 based on Debian Buster
FROM python:3.10-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Git and other necessary packages
RUN apt-get update && apt-get install -y git

# Copy and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variable for GitPython
ENV GIT_PYTHON_REFRESH=quiet

# Command to run the Python application
CMD ["bash", "start.sh"]
