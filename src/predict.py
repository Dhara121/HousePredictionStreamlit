import pandas as pd
import joblib
from preprocess import preprocess_data

# 1. Load test data
test_df = pd.read_csv("data/test.csv")

# 2. Preprocess test data 
test_df_processed = preprocess_data(test_df, is_train=False)

# 3. Load the trained model
model = joblib.load("models/house_price_model.pkl")

# 4. Make predictions
predictions = model.predict(test_df_processed)

# 5. Create submission DataFrame
submission = pd.DataFrame({
    "Id": test_df["Id"],
    "SalePrice": predictions
})

# 6. Save to CSV
submission.to_csv("data/processed_data.csv", index=False)

