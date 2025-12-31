# ---------- Stage 1: Builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# ---------- Stage 2: Runtime ----------
FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy installed python packages from builder
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11

# Copy application code
COPY app app

USER appuser

EXPOSE 5000

CMD ["python", "app/main.py"]
