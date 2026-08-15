# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 19:07:32 2025

@author: THYAGHARAJAN
"""

import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 20,
    "Insulin": 85,
    "BMI": 28.5,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 30
}

response = requests.post(url, json=data)
print(response.json())