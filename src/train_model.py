# src/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from preprocess import preprocess_data
import joblib
import os

# Load dataset
df = pd.read_csv("data/train.csv")
df = preprocess_data(df, is_train=True)

# Drop rows with missing SalePrice
df.dropna(subset=['SalePrice'], inplace=True)

# Use only selected features from the Streamlit app
features = [
    "OverallQual", "GrLivArea", "GarageCars",
    "TotalBsmtSF", "YearBuilt", "LotFrontage", "Neighborhood"
]
X = df[features]
y = df["SalePrice"]

# One-hot encode categorical features
X = pd.get_dummies(X, columns=["Neighborhood"], drop_first=True)

# Train-validation split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
val_preds = model.predict(X_val)
mse = mean_squared_error(y_val, val_preds)
rmse = mse ** 0.5
print(f"Validation RMSE: {rmse:.2f}")

# Save model and feature columns
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/house_price_model.pkl")
joblib.dump(list(X.columns), "models/feature_columns.pkl")
print("Model and feature list saved to 'models/'")
