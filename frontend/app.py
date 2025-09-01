import os
import requests
from flask import Flask, render_template_string

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:5000/api/data")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Frontend Service</title>
</head>
<body>
    <h1>Frontend - Connected to Backend</h1>
    <h3>Data from backend:</h3>
    <pre>{{ backend_data }}</pre>
</body>
</html>
"""

@app.route("/")
def index():
    try:
        response = requests.get(BACKEND_URL, timeout=15)  # keep 15
        data = response.json()
    except Exception as e:
        data = {"error": str(e)}
    return render_template_string(HTML_TEMPLATE, backend_data=data)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
