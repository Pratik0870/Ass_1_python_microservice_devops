import os
import json
import time
from flask import Flask, jsonify
import psycopg2
import requests

app = Flask(__name__)

DB_HOST = os.getenv("POSTGRES_HOST", "postgres")
DB_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
DB_NAME = os.getenv("POSTGRES_DB", "appdb")
DB_USER = os.getenv("POSTGRES_USER", "appuser")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "apppass")

LOGGER_URL = os.getenv("LOGGER_URL", "http://logger:9000/log")

def get_db_conn():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        connect_timeout=5
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/data")
def api_data():
    ts = int(time.time())
    message = {"message": "Hello from Backend", "timestamp": ts}

    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO heartbeats(details) VALUES (%s)", (json.dumps(message),))
        conn.commit()
        cur.close()
        conn.close()
        message["db"] = "inserted"
    except Exception as e:
        message["db_error"] = str(e)

    try:
        requests.post(LOGGER_URL, json={"event": "api_hit", "payload": message}, timeout=2)
        message["logger"] = "notified"
    except Exception as e:
        message["logger_error"] = str(e)

    return jsonify(message), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
