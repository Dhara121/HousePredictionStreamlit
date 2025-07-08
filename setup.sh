#!/bin/bash

echo "Setting up environment..."
python -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. To run the app:"
echo "streamlit run app/app.py"
