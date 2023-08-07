import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import joblib
import datetime

# Load your dataset (replace 'dataset.csv' with your actual dataset file)
data = pd.read_csv('AAl.csv')

data['Date'] = pd.to_datetime(data['Date'])
data['DaysFromStart'] = (data['Date'] - data['Date'].min()).dt.days

# Assuming your dataset has columns 'Date', 'Low', 'Open', 'High', 'Close', 'Adjusted Close'
# 'Date' will be used as the target variable in this example
X = data[['Low', 'Open', 'High', 'Close', 'Adjusted Close']]  # Features
y = data['DaysFromStart']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a ColumnTransformer to process different types of features
# Here we're assuming all features are numeric, but you can adjust accordingly
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), X.columns)
    ])

# Create a pipeline with preprocessing, PCA, and a GradientBoostingRegressor
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('pca', PCA(n_components=3)),  # Principal Component Analysis
    ('regressor', GradientBoostingRegressor(n_estimators=100, random_state=42))  # Adjust parameters as needed
])

# Train the model
model.fit(X_train, y_train)

# Save the trained model as a .pkl file
model_filename = 'stock_price_prediction_model.pkl'
joblib.dump(model, model_filename)
print(f"Model saved as {model_filename}")