from flask import Flask, request
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from main import scrape
app = Flask(__name__)
@app.route("/scrape", methods=["POST"])
def scrape_data():
    data = request.json
    location = data.get("location")
    if not location:
        return {"error": "No location provided"}, 400
    result_path = scrape(location)
    if result_path and os.path.exists(result_path):
        return {"status": "success", "csv_path": result_path}
    else:
        return {"status": "fail", "message": "No data collected"}, 200
if __name__ == "__main__":
    app.run(debug=True)
