# 🛵 Used Bike Price Predictor

A Machine Learning project that predicts the resale price of a used bike based on features like bike name, city, kilometers driven, number of owners, age, power (cc), and brand. The model is deployed using a Streamlit web app.

---

## 🚀 Features

- Predicts the resale price of a used bike.
- Trained with a Random Forest Regressor.
- Interactive user interface using Streamlit.
- Uses label encoding for categorical values.
---

## 📁 Dataset

Used Bike dataset from Kaggle.  
Includes features like:

- `bike_name`
- `price`
- `city`
- `kms_driven`
- `owner`
- `age`
- `power`
- `brand`

---

<img width="711" height="726" alt="Streamlit (1)" src="https://github.com/user-attachments/assets/070df528-c247-4914-8679-27250623e4d8" />

## 🛠️ Installation

1. Clone the repository:
   
git clone https://github.com/your-username/BikePricePredictor.git
cd BikePricePredictor

2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate  # On Windows

3. Install dependencies:
pip install -r requirements.txt

🧠 Training the Model
To train the model, run:
python train_model.py

This will:
Load the dataset (used_bike_data.csv)
Encode categorical columns
Train a Random Forest Regressor
Save the model and label encoder as bike_price_model.pkl and label_encoder.pkl

🌐 Run the Streamlit App
streamlit run app.py
Then open the local URL in your browser to use the app.

📦 Project Structure
BikePricePredictor/
├── used_bike_data.csv
├── train_model.py
├── app.py
├── bike_price_model.pkl
├── label_encoder.pkl
├── requirements.txt
└── README.md

📸 Sample Prediction
💰 Estimated Price: ₹35,000.00

📌 Author
Developed by Vinoth Viveki
