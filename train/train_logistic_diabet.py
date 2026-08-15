# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 16:45:06 2025

@author: THYAGHARAJAN
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Determine absolute paths relative to this script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
model_filename = os.path.join(script_dir, "..", "models", "logistic_reg_diabetic.pkl")
csv_path = os.path.join(script_dir, "..", "diabetes.csv")

df = pd.read_csv(csv_path)
print(df.head())



# Separate features (X) and target (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Features (X) shape:", X.shape)
print("Target (y) shape:", y.shape)
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)



# Create an instance of the LogisticRegression model
model = LogisticRegression(random_state=42, solver='liblinear')

# Fit the model to the training data
model.fit(X_train, y_train)

print("Logistic Regression model trained successfully.")

joblib.dump(model, model_filename)
print(f"Model saved to {os.path.normpath(model_filename)}")
