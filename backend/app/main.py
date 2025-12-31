from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running"})

@app.route("/health")
def health():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        conn.close()
        return jsonify({"status": "UP", "database": "CONNECTED"})
    except Exception as e:
        return jsonify({"status": "DOWN", "error": str(e)})

# 🔴 THIS WAS MISSING
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
