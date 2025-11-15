# Use slim Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy server script
COPY server.py .

# Expose port (Fly.io ignores this, but good practice)
EXPOSE 6000

# Set environment variable for Python unbuffered output (good for logs)
ENV PYTHONUNBUFFERED=1

# Run server
CMD ["python", "server.py"]
