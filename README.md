# Diabetes Prediction API

![Python](https://img.shields.io/badge/Python-306998?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

This is a Flask-based web application and API that predicts whether a patient is diabetic based on various medical features (Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, and Age). It uses a Logistic Regression model trained with the PIMA INDIAN Dataset using scikit-learn.

## Directory Structure
- `app.py`: The main Flask web server.
- `client.py`: A sample Python client to interact with the API programmatically.
- `models/logistic_reg_diabetic.pkl`: The trained machine learning model.
- `templates/`: HTML templates for the web interface.
- `diabetes.csv`: The dataset used for training (optional).

## Setup & Installation

To run this project on your local machine, you must first clone the repository and then install the required Python packages.

**1. Clone the repository**
```bash
git clone https://github.com/tnivedha-257/diabetes-prediction-app.git
cd diabetes-prediction-app
```

**2. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Mac/Linux
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

## How to Run

**1. Start the Flask Server**
```bash
python app.py
```
The server will start and provide a URL (usually `http://127.0.0.1:5000`).
It will also provide your current network address, (like Running on http://10.17.86.42:5000). 
You can give this address to others who have connected to the same network and they can use your app.

**2. Access the Web Interface**
Open your browser and navigate to the URL provided by the server to interact with the prediction form.

**3. Use the API Client**
While the server is running, you can test the API endpoint programmatically by opening a second terminal window and running:
```bash
python client.py
```
