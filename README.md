##  House Price Prediction App

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Status](https://img.shields.io/badge/Status-Deployed-success)

A Machine Learning web application built with **Streamlit**, which predicts housing prices based on key features like area, year built, basement size, neighborhood, etc.

📍 **Live App**:  [Visit Here](https://houseprediction-n053.onrender.com)

---

###  Features

*  Real-time prediction of house prices
*  Pre-trained RandomForestRegressor model
*  Intuitive UI with Streamlit
*  One-hot encoding of neighborhoods
*  Cleaned and production-ready deployment via Render

---

###  Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **Modeling**: scikit-learn
* **Data Handling**: Pandas
* **Deployment**: Render

---

### 🗂️ Project Structure

```
House-price-predictor/
│
├── app/
│   └── app.py                  # Streamlit application
├── models/
│   ├── house_price_model.pkl   # Trained model
│   └── feature_columns.pkl     # Expected input columns
├── src/
│   ├── preprocess.py           # Data preprocessing
│   ├── predict.py              # (optional) prediction logic
├── requirements.txt
├── render.yaml
├── Dockerfile (optional)
├── setup.sh (optional)
└── README.md
```

---

###  How to Run Locally

```bash
# Clone repo
git clone https://github.com/Dhara121/HousePredictionStreamlit.git
cd HousePredictionStreamlit

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app/app.py
```
