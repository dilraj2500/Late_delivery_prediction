# Late Delivery Risk Prediction

A Machine Learning API to predict late delivery risk in supply chain using FastAPI, MySQL, and Scikit-learn.

## Tech Stack
- Python, FastAPI, Uvicorn
- Scikit-learn, Pandas, Joblib
- MySQL, SQLAlchemy
- HTML/CSS Frontend

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Configure .env file:
   DB_USER=root
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=late_delivery_db

3. Run server:
   uvicorn backend.app:app --reload

4. Open frontend:
   frontend/index.html

## API Endpoints
- GET  /       — Health check
- POST /predict — Predict late delivery risk