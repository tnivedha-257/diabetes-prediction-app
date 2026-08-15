# -*- coding: utf-8 -*-
"""
Created on Sat Dec 1 13:46:05 2025
Updated GUI Client for Diabetes Prediction Flask API
Now supports entering server IP at runtime.
@author: THYAGHARAJAN
"""


import os
import json
import socket
from flask import Flask, request, jsonify, render_template
from joblib import load
import numpy as np

MODEL_FILE = 'models/logistic_reg_diabetic.pkl'   #see the directory structure

kkt_flask_server = Flask(__name__)
model = None


# ---------------- Helper: Get Local IP --------------------
def get_local_ip():
    """Returns active local IP if network available, else localhost."""
    try:
        # Try method 1: Ask OS the primary network IP
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        if not ip.startswith("127."):
            return ip
    except:
        pass

    try:
        # Try method 2: Use a UDP socket trick
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("192.168.1.1", 80))  # Router IP guess
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        pass

    try:
        # Try method 3: Google DNS (if internet exists)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        pass

    # Final fallback
    return "127.0.0.1"




# ---------------- Load Model --------------------
def load_model():
    global model
    try:
        model = load(MODEL_FILE)
        print(f"Model '{MODEL_FILE}' loaded successfully.")
    except Exception as e:
        print(f"Failed to load model: {e}")
        model = None


# ---------------- HTML GUI --------------------
@kkt_flask_server.route("/")
def home():
    ip = get_local_ip()
    return render_template(
    "index.html",
    server_ip=ip,
    predict_url=f"http://{ip}:5000/predict"
    )


# ---------------- PREDICTION API --------------------
@kkt_flask_server.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return jsonify({
            "status": "success",
            "message": "Diabetes Prediction API is running. Use POST method."
        })

    # If form submitted via browser
    if request.form:
        data = request.form
        features = [
            float(data["Pregnancies"]),
            float(data["Glucose"]),
            float(data["BloodPressure"]),
            float(data["SkinThickness"]),
            float(data["Insulin"]),
            float(data["BMI"]),
            float(data["DiabetesPedigreeFunction"]),
            float(data["Age"])
        ]

        X = np.array([features])
        prob = model.predict_proba(X)[0]
        prediction = int(model.predict(X)[0])

        return render_template(
            "result.html",
            label="Diabetic" if prediction == 1 else "Non-Diabetic",
            prob_diabetic=prob[1],
            prob_non_diabetic=prob[0]
        )

    # If JSON POST (from Python client)
    data = request.get_json()
    features = [
        data["Pregnancies"],
        data["Glucose"],
        data["BloodPressure"],
        data["SkinThickness"],
        data["Insulin"],
        data["BMI"],
        data["DiabetesPedigreeFunction"],
        data["Age"]
    ]

    X = np.array([features])
    prob = model.predict_proba(X)[0]
    prediction = int(model.predict(X)[0])

    return jsonify({
        "prediction": prediction,
        "prediction_label": "Diabetic" if prediction == 1 else "Non-Diabetic",
        "probability_diabetic": float(prob[1]),
        "probability_non_diabetic": float(prob[0])
    })



# ---------------- START SERVER --------------------
if __name__ == '__main__':
    load_model()

    ip = get_local_ip()
    print("========================================")
    print(f"Flask server running on: http://{ip}:5000")
    print("========================================")

    kkt_flask_server.run(host="0.0.0.0", port=5000, debug=True)
