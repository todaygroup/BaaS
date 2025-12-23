# apps/worker/Dockerfile
FROM python:3.11-slim

WORKDIR /worker

# Copy requirements and install dependencies
COPY apps/worker/requirements.txt ./apps/worker/
RUN pip install --no-cache-dir -r ./apps/worker/requirements.txt

# Copy source code and shared packages
COPY apps/worker ./apps/worker
COPY packages ./packages

# Set environment variables
ENV PYTHONPATH=/worker
ENV ENV=prod

# Run worker main module
CMD ["python", "-m", "apps.worker.worker.main"]
