# Use an official Python runtime as the base image
FROM python:3.9.16-alpine3.17

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variable for AWS credentials
ENV AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY

# Expose the port for the application
EXPOSE 5050

# Run the command to start the application
CMD ["python", "app.py"]
