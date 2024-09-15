# Use the official Python image from DockerHub as the base image
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install required system dependencies for ODBC Driver
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc-dev

# Install the Microsoft ODBC Driver for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Install pyodbc
RUN pip install pyodbc
# Set environment variables to avoid writing .pyc files and enable unbuffered output

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container (update the path)
COPY ./requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY ./PUCarona-1 /app/

# Expose the port that the Flask app runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
