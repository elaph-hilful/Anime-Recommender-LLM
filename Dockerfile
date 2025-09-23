# Builder
FROM python:3.11-slim as builder
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --user -e .

# Runtime
FROM python:3.11-slim
RUN groupadd --gid 1001 appuser && useradd --uid 1001 --gid 1001 --create-home appuser
WORKDIR /app
COPY --from=builder /root/.local /home/appuser/.local
COPY --from=builder /app /app
RUN chown -R appuser:appuser /app
ENV PATH=/home/appuser/.local/bin:$PATH
USER 1001
EXPOSE 8501
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
