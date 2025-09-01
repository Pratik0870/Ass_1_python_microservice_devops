from flask import Flask, jsonify
import os
import psycopg2
import time
import json

app = Flask(__name__)

DB_HOST = os.getenv("POSTGRES_HOST", "postgres")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "mydb")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/data")
def get_data():
    try:
        conn = psycopg2.connect(
            host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
            user=DB_USER, password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO heartbeats(details) VALUES (%s) RETURNING id;",
            (json.dumps({"message": "Hello from Backend", "timestamp": int(time.time())}),)
        )
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Hello from Backend", "db": "inserted"}), 200
    except Exception as e:
        return jsonify({"db_error": str(e), "message": "Hello from Backend"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
