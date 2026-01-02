# ---------- Stage 1: Builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.11-slim AS runtime

RUN useradd -m appuser
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY app app

USER appuser
EXPOSE 5000
CMD ["python", "app/main.py"]

# ---------- Stage 3: Test ----------
FROM python:3.11-slim AS test

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app app
COPY tests tests

CMD ["pytest"]
