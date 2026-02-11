# ================================
# Base image
# ================================
FROM python:3.11-slim

# ================================
# Environment variables
# ================================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ================================
# System dependencies
# ================================
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# ================================
# Working directory
# ================================
WORKDIR /app

# ================================
# Install Python dependencies
# ================================
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ================================
# Copy project files
# ================================
COPY . .

# ================================
# Expose Cloud Run port
# ================================
EXPOSE 8080

# ================================
# Start production server
# ===============================

#CMD python manage.py migrate && gunicorn CNN.wsgi:application --bind 0.0.0.0:8080 --workers 1 --timeout 300
# CMD gunicorn CNN.wsgi:application --bind 0.0.0.0:$PORT --workers 1 --timeout 300
# CMD sh -c "python manage.py migrate && gunicorn CNN.wsgi:application --bind 0.0.0.0:8080 --workers 1 --timeout 300"
CMD sh -c "python manage.py migrate && gunicorn CNN.wsgi:application --bind 0.0.0.0:$PORT --workers 1 --timeout 300"



