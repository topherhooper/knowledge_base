# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install bash, bsdmainutils (for colrm), and any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y bash bsdmainutils \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements.txt file to leverage Docker cache
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run chatgpt_document_assistant.py when the container launches
CMD ["python", "py/chatgpt_document_assistant.py"]