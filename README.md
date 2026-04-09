# 🎯 Student Score Predictor (ML API + Frontend)

## 🚀 Overview

This project is an end-to-end Machine Learning system that predicts a student's score based on:

* Hours studied
* Attendance percentage

It includes:

* A trained ML model
* A backend API built using FastAPI
* A frontend UI built using Streamlit

---

## 🧠 How It Works

1. User enters input (hours, attendance) in the frontend
2. Frontend sends request to backend API
3. Backend loads trained ML model
4. Model predicts score
5. API returns result to frontend
6. Frontend displays prediction

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* FastAPI
* Streamlit
* Requests

---

## 📁 Project Structure

```
ml-api-student-predictor/
│
├── app/
│   └── main.py          # FastAPI backend
│
├── frontend/
│   └── app.py           # Streamlit UI
│
├── model.pkl            # Trained ML model
├── train.py             # Model training script
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-link>
cd ml-api-student-predictor
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run backend (FastAPI)

```
uvicorn app.main:app --reload
```

### 4. Run frontend (Streamlit)

```
streamlit run frontend/app.py
```

---

## 🌐 API Endpoint

### POST `/predict`

#### Request:

```
{
  "hours": 5,
  "attendance": 80
}
```

#### Response:

```
{
  "predicted_score": 69.28
}
```

---

## 📌 Features

* End-to-end ML pipeline
* REST API integration
* Interactive frontend UI
* Real-time prediction

---

## 🚀 Future Improvements

* Add input validation (Pydantic)
* Deploy on cloud (Render/AWS)
* Improve UI design
* Use advanced ML models

---

## 🙌 Author

Aarya Yadav