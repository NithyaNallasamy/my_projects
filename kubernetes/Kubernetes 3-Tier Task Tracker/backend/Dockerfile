# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir flask pymongo

# Copy the rest of the code
COPY . .

# Expose the port our app runs on
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
