
# 🚀 Production MLOps Financial Prediction System

An end-to-end **Machine Learning Operations (MLOps) system** for predicting loan approval (credit risk) using a production-ready pipeline including data preprocessing, model training, API deployment, validation, logging, and Dockerization.

This project demonstrates **real-world ML system design**, focusing on **consistency between training and inference**, API reliability, and deployability.

---

# 📌 Features

## 🔹 Core ML Capabilities

* 📊 Loan approval prediction (binary classification)
* 🧠 Logistic Regression model for baseline prediction
* 📈 Model evaluation using accuracy and classification metrics
* 💾 Model persistence using Joblib

---

## 🔹 Data Engineering & Pipeline

* 📂 Data loading and preprocessing pipeline
* 🧹 Missing value handling (mode/median imputation)
* 🔢 Categorical feature encoding
* 🔄 Train-test split for model validation
* 🔁 Reusable preprocessing pipeline for training and inference

---

## 🔹 MLOps Capabilities

* ⚙️ Consistent preprocessing across training and inference
* 🔐 Input validation using Pydantic
* 📜 Logging for requests, predictions, and errors
* 📡 REST API for real-time predictions
* 🐳 Dockerized deployment

---

## 🔹 API Features

* 🚀 FastAPI-based inference service
* 📥 POST /predict endpoint
* 📊 Structured input validation
* 📌 JSON response with prediction and result
* 📄 Swagger UI for testing

---

# 🛠️ Technology Stack

## 🔹 Backend & ML

* FastAPI
* Scikit-learn
* Pandas
* Joblib

---

## 🔹 MLOps & Deployment

* Pydantic (input validation)
* Logging (Python logging module)
* Docker

---

## 🔹 Development Tools

* Python 3.10
* VS Code
* Git & GitHub
* Jupyter Notebook (EDA)

---

# 🏗️ Architecture

```id="mlopsarch"
Raw Input (API Request)
        │
        ▼
Pydantic Validation
        │
        ▼
Preprocessing Pipeline
        │
        ▼
Trained ML Model
        │
        ▼
Prediction Output
        │
        ▼
Logging (Request + Response)
```

---

# ⚙️ How to Run (Docker)

### 1️⃣ Clone Repository

```id="ml1"
git clone <your-repo-url>
cd mlops-financial-system
```

---

### 2️⃣ Build Docker Image

```id="ml2"
docker build -t mlops-financial-system .
```

---

### 3️⃣ Run Container

```id="ml3"
docker run -p 8000:8000 mlops-financial-system
```

---

### 4️⃣ Access API

* Swagger UI: http://localhost:8000/docs

---

# 🧪 API Usage

### POST `/predict`

#### Sample Input:

```json id="ml4"
{
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "0",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 0,
  "LoanAmount": 150,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area": "Urban"
}
```

---

#### Sample Response:

```json id="ml5"
{
  "prediction": 1,
  "result": "Approved"
}
```

---

# 🧠 Key Highlights

* Built a **production-ready ML system**, not just a model
* Ensured **training-inference consistency**, a critical MLOps requirement
* Implemented **input validation and logging for reliability**
* Designed **modular and reusable pipeline architecture**
* Delivered **deployable solution using Docker**

---

# 🔮 Future Enhancements

* Model versioning and registry (MLflow)
* CI/CD pipeline for automated deployment
* Monitoring (Prometheus / Grafana)
* Advanced models (XGBoost, LightGBM)
* Feature store integration

---

# 👨‍💻 Author

Developed as part of a **hands-on MLOps portfolio project** demonstrating real-world machine learning system design and deployment.

---


