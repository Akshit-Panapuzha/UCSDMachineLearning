# Stock Price Prediction API

Welcome to the Stock Price Prediction API repository. This project showcases a sophisticated approach to predicting stock prices based on historical data, leveraging advanced machine learning techniques and a well-structured pipeline to provide accurate predictions of stock price trends.

## Overview

This project represents the culmination of a comprehensive machine learning journey, combining skills honed during a rigorous machine learning bootcamp with a master's-level understanding of predictive modeling. The API harnesses the capabilities of scikit-learn and Gradient Boosting Regression to craft a robust predictive model for stock price movement.

## Features

- **Advanced Machine Learning Pipeline**: At the core of this API lies a complex machine learning pipeline. This pipeline encompasses preprocessing, dimensionality reduction, and Gradient Boosting Regression to craft a high-performance predictive model.

- **Feature Engineering**: The model is trained on pivotal features including 'Low', 'Open', 'High', 'Close', and 'Adjusted Close', enabling the capture of nuanced patterns in stock price data.

- **Efficient Preprocessing**: A meticulously designed preprocessing pipeline ensures meticulous data scaling and transformation, setting the foundation for accurate predictions.

- **Dimensionality Reduction**: The integration of Principal Component Analysis (PCA) facilitates feature dimensionality reduction, optimizing model performance and curbing overfitting.

- **Predictive Power**: The central predictive model utilizes Gradient Boosting Regressor, recognized for its aptitude in capturing intricate relationships, ensuring precise and meaningful predictions.

- **Calculation of Predicted Date**: Differing from conventional approaches, the API predicts the number of days from the start date. This innovative strategy enhances practicality and empowers well-informed decision-making.

## Getting Started

To experience the Stock Price Prediction API, proceed through these steps:

1. Begin by installing the requisite packages: `pip install -r requirements.txt`

2. Ready your historical stock data in CSV format, making sure to include essential columns such as 'Date', 'Low', 'Open', 'High', 'Close', and 'Adjusted Close'.

3. Train the predictive model by executing the `trainModel.py` script. This process will generate the 'stock_price_prediction_model.pkl' file, encapsulating the trained model.

4. Activate the API server by running the `server.py` script. This deployment allows you to issue POST requests with input stock data.

5. Engage the client script `client.py` to transmit input data to the API and obtain predictions for the number of days from the start date.

## Advanced Usage

For advanced users keen on further enhancing the API's capabilities, consider:

- Fine-tuning hyperparameters of the Gradient Boosting Regressor for optimal performance.
- Exploring alternate regression techniques to compare and contrast predictive prowess.
- Customizing preprocessing steps or exploring additional avenues for feature engineering.

--------
By Akshit Panapuzha

---

**Note**: Be sure to execute the `trainModel.py` script to generate the 'stock_price_prediction_model.pkl' file before utilizing the API for predictions.
