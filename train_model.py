import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("bike_data.csv")

# Encode categorical columns
cat_cols = ['bike_name', 'city', 'owner', 'brand']
encoder = LabelEncoder()
for col in cat_cols:
    data[col] = encoder.fit_transform(data[col])

# Features and Target
X = data[['bike_name', 'city', 'kms_driven', 'owner', 'age', 'power', 'brand']]
y = data['price']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the model and encoder
joblib.dump(model, "bike_price_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")

print("✅ Model training complete and saved!")