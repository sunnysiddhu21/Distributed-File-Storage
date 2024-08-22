# Use a base image with Python installed
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY app app

# Set the command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
