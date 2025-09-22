## Parent docker image
FROM python:3.10-slim

## Esential environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1



## Set work directory
WORKDIR /app

## Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Comping all the contents from repo to app
COPY . .


## Run setup.py
RUN pip install --no-cache-dir -e .

## Expose the port 8501
EXPOSE 8501


CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
