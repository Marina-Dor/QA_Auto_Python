FROM python:3.12-slim

# Setting working directory
WORKDIR /app

# Copying the app code
COPY . /app

ENV PYTHONPATH="/app:/app/tests"

# Install system dependencies required for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Installing Python dependencies
RUN python -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
RUN python --version

CMD ["pytest", "tests/"]