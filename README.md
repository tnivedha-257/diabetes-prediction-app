# Diabetes Prediction API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-app-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

This is a Flask-based web application and API that predicts whether a patient is diabetic based on various medical features. It uses a trained Logistic Regression model from scikit-learn.

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
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME
```
*(Note: Replace `YOUR-USERNAME/YOUR-REPOSITORY-NAME` with your actual GitHub link once created).*

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

**2. Access the Web Interface**
Open your browser and navigate to the URL provided by the server to interact with the prediction form.

**3. Use the API Client**
While the server is running, you can test the API endpoint programmatically by opening a second terminal window and running:
```bash
python client.py
```
