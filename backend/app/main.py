from flask import Flask, jsonify
from flask_cors import CORS
from app.db import get_db_connection

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running"})

@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "UP", "database": "CONNECTED"})
    except Exception as e:
        return jsonify({"status": "DOWN", "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
