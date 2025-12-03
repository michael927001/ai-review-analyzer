# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose FastAPI port
EXPOSE 8080

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
