# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:55:35 2023

@author: 16172
"""
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

def Predict_current_charges(df):
    # Select the predictor variables
    X = df[['Consumption_(HCF)', 'Other_Charges','TDS','Water&Sewer_Charges']]

    # Select the target variable
    y = df['Current_Charges']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a random forest regression model
    rf_model = RandomForestRegressor()

    # Train the model using the training data
    rf_model.fit(X_train, y_train)

    # Use the trained model to make predictions on the test data and accuracy
    return pd.DataFrame({'predicted_Current_charges': rf_model.predict(X_test)}),{'Accuracy' :rf_model.score(X_test, y_test)}
    

def Predict_revenue(df):
    # Encode the Rate_Class variable
    le = LabelEncoder()
    df['Rate_Class_Encoded'] = le.fit_transform(df['Rate_Class'])

    # Select the predictor variables
    X = df[['Consumption_(HCF)', 'Other_Charges', 'Rate_Class_Encoded', 'TDS', 'Service_Start_Date', 'Service_End_Date']]

    # Select the target variable
    y = df['Current_Charges']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Gradient Boosting regression model
    gb_model = GradientBoostingRegressor()

    # Train the model using the training data
    gb_model.fit(X_train, y_train)

    # Use the trained model to make predictions on the test data and accuracy
    return pd.DataFrame({'predicted_Revenue': gb_model.predict(X_test)}), {'Accuracy': gb_model.score(X_test, y_test)}
