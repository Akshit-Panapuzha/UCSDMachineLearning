# Stock Price Prediction API for UCSD Machine Learning Bootcamp

Welcome to the Stock Price Prediction API repository. This project demonstrates a robust and sophisticated approach to predicting stock prices based on historical data. The API utilizes advanced machine learning techniques and a well-structured pipeline to provide accurate predictions of stock price trends.

## Overview

This project is the culmination of an extensive machine learning journey, combining skills honed during a comprehensive machine learning bootcamp with a master's-level understanding of predictive modeling. The API leverages the power of scikit-learn and Gradient Boosting Regression to create a robust predictive model for stock price movement.

## Features

- **Advanced Machine Learning Pipeline**: The heart of this API lies in its intricate machine learning pipeline. This pipeline encompasses preprocessing, dimensionality reduction, and Gradient Boosting Regression to create a high-performance predictive model.

- **Feature Engineering**: The model is trained on key features including 'Low', 'Open', 'High', 'Close', and 'Adjusted Close', capturing nuanced patterns in stock price data.

- **Efficient Preprocessing**: A custom preprocessing pipeline ensures that data is well-scaled and transformed, setting the stage for accurate predictions.

- **Dimensionality Reduction**: Principal Component Analysis (PCA) is employed to reduce feature dimensionality, optimizing model performance and mitigating overfitting.

- **Predictive Power**: The Gradient Boosting Regressor, known for its ability to capture complex relationships, forms the core of the predictive model, ensuring accurate and meaningful predictions.

- **Calculation of Predicted Date**: Rather than predicting exact stock prices, the API predicts the number of days from the start date. This unique approach adds practicality to predictions and enables informed decision-making.

## Getting Started

To use the Stock Price Prediction API, follow these steps:

1. Install the necessary packages: `pip install -r requirements.txt`

2. Prepare your historical stock data in CSV format, ensuring it includes columns 'Date', 'Low', 'Open', 'High', 'Close', and 'Adjusted Close'.

3. Train the predictive model by running the script `train_model.py`. This will generate the 'stock_price_prediction_model.pkl' file containing the trained model.

4. Run the API server by executing `server.py`. This will deploy the API, enabling you to send POST requests with input stock data.

5. Utilize the client script `client.py` to send input data to the API and receive predictions for the number of days from the start date.

## Advanced Usage

For advanced users seeking to enhance the API further, consider:

- Tuning hyperparameters of the Gradient Boosting Regressor for optimal performance.
- Exploring alternative regression techniques to compare and contrast predictive power.
- Modifying preprocessing steps or exploring additional feature engineering techniques.

---

By Akshit Panapuzha

