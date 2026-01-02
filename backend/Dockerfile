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

# Copy python packages
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11

# Copy app
COPY app app

USER appuser

EXPOSE 5000

# ✅ THIS MUST START FLASK SERVER (NOT TESTS)

CMD python app/init_db.py && python app/main.py
