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



@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    data["timestamp"] = str(time())
    logger.info(f"Received:{data}")
    print(time())
    db.new_request(data["message"], data["device"], time(), raw=data)
    print(request)
    return jsonify({"status": "ok"})

@app.route("/")
def index():

    requests = db.get_requests()

    return render_template('index.html', requests=requests)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
