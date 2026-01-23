from flask import Flask, request, jsonify, render_template
from db import dbHandler

import logging, datetime

db = dbHandler()

def time():
    return datetime.datetime.now()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

info = []

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    info.append({"data": data, "timestamp": time()})
    logger.info("Received:", data)
    print(request)
    return jsonify({"status": "ok"})

@app.route("/")
def index():
    return render_template('index.html', data=info)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
