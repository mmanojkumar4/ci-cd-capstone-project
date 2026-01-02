from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="postgres_db",          
        port=5432,                   
        database="appdb",
        user="postgres",
        password="postgres",
        connect_timeout=5
    )


@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({
            "status": "UP",
            "database": "CONNECTED"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "DOWN",
            "error": str(e)
        }), 500

@app.route("/")
def home():
    return jsonify({"message": "Backend is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
