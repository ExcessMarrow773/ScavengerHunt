from flask import Flask, request, jsonify
import logging, datetime

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
    return jsonify({"status": "ok"})

@app.route("/")
def index():
    return jsonify({"data": info})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
