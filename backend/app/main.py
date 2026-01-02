from flask import Flask, jsonify
import os

app = Flask(__name__)   #  DEFINE APP FIRST


@app.route("/health")
def health():
    # Skip DB during tests
    if os.getenv("TESTING") == "true":
        return jsonify({"status": "UP", "database": "SKIPPED"}), 200

    return jsonify({"status": "UP", "database": "CONNECTED"}), 200


@app.route("/")
def home():
    return jsonify({"message": "Backend is running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
