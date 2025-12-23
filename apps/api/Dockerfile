# apps/api/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY apps/api/requirements.txt ./apps/api/
RUN pip install --no-cache-dir -r ./apps/api/requirements.txt

# Copy source code and shared packages
COPY apps/api ./apps/api
COPY packages ./packages

# Set environment variables
ENV PYTHONPATH=/app
ENV ENV=prod

# Expose port and start API
EXPOSE 8080
CMD ["uvicorn", "apps.api.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
