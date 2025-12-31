import os
import psycopg2
from flask import jsonify

def health_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "testdb"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "postgres")
        )
        conn.close()
        return jsonify({"status": "UP", "database": "CONNECTED"}), 200
    except Exception as e:
        return jsonify({"status": "DOWN", "error": str(e)}), 500
