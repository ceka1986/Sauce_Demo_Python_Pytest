# Use an official lightweight Python runtime as a parent image
FROM python:3.10-slim

# Install system dependencies required for Selenium and Chrome
RUN apt-get update && apt-get install -y \
    curl \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Default command to run tests when the container starts
CMD ["pytest"]