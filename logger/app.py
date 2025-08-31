import os
from flask import Flask, request, jsonify

app = Flask(__name__)
LOG_DIR = os.getenv("LOG_DIR", "/logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/log", methods=["POST"])
def log():
    payload = request.get_json(silent=True) or {}
    line = str(payload).replace("\n", " ")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    return jsonify({"written": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
