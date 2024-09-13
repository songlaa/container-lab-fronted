# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install required packages
RUN pip install flask mysql-connector-python

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the default command to run the app with Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
