# Diabetes Prediction API

This is a Flask-based web application and API that predicts whether a patient is diabetic based on various medical features. It uses a trained Logistic Regression model.

## Directory Structure
- `app.py`: The main Flask web server.
- `client.py`: A sample Python client to interact with the API programmatically.
- `models/logistic_reg_diabetic.pkl`: The trained machine learning model.
- `templates/`: HTML templates for the web interface.
- `diabetes.csv`: The dataset (optional).

## Requirements
Make sure you have Python installed. You can install the required packages using:
```bash
pip install -r requirements.txt
```

## How to Run

1. **Start the Flask Server**
   ```bash
   python app.py
   ```
   The server will start and provide a URL (usually `http://<your-ip>:5000` or `http://127.0.0.1:5000`).

2. **Access the Web Interface**
   Open your browser and navigate to the URL provided by the server to interact with the prediction form.

3. **Use the API Client**
   While the server is running, you can test the API endpoint programmatically:
   ```bash
   python client.py
   ```
