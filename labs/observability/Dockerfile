# Slim Python image for smaller footprint and faster builds
FROM python:3.11-slim

# Directory for the application code
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the application port
EXPOSE 8000

# Run the web server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]