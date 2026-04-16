from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/load")
def load():
    return jsonify(load_data())

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    save_data(data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)