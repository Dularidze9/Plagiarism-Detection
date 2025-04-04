# Use the official Python image as the base
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TRANSFORMERS_CACHE=/tmp/.cache/huggingface

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the cache folder with appropriate permissions
RUN mkdir -p $TRANSFORMERS_CACHE && chmod -R 777 $TRANSFORMERS_CACHE

# Copy the application code into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
