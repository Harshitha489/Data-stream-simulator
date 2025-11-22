import warnings
warnings.filterwarnings("ignore",category=UserWarning, message="This is a Development server")
from flask import Flask, jsonify, render_template
import random
import time

app = Flask(__name__)

def generate_data():
    return {
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 90.0), 2),
        "pressure": round(random.uniform(900.0, 1100.0), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(generate_data())

if __name__ == "__main__":
    app.run(debug=True)