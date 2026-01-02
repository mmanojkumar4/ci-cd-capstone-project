# -------------------------
# Stage 1: base
# -------------------------
FROM python:3.11-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------
# Stage 2: test
# -------------------------
FROM base AS test
ENV TESTING=true
COPY app app
COPY tests tests
CMD ["pytest", "-v"]

# -------------------------
# Stage 3: runtime  
# -------------------------
FROM base AS runtime
COPY app app
EXPOSE 5000
CMD ["python", "app/main.py"]
