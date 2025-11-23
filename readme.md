# 🏥 Health Guard – Multiple Disease Prediction System
### AI-powered health prediction app built with Machine Learning & Streamlit

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Models-green)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📄 Overview
**Health Guard** is an AI-powered medical diagnosis assistance system that enables users to input medical attributes and predict the likelihood of **multiple diseases**, including **Diabetes, Heart Disease, and Parkinson’s Disease**.  
The application integrates **trained machine learning models** into an intuitive **Streamlit** user interface and supports **PDF medical summary report generation**.

---

## 🚀 Features
- ✔ Predict **Diabetes, Heart Disease & Parkinson’s Disease**
- ✔ **Clean & interactive** Streamlit UI
- ✔ **Machine Learning model integration** (Logistic Regression / SVM)
- ✔ **PDF report generation**
- ✔ **Modular & scalable** architecture
- ✔ **Responsive and user-friendly** experience

---

## 🖥 Tech Stack

| Category        | Technology |
|----------------|------------|
| Frontend UI    | Streamlit |
| Backend        | Python |
| Libraries      | NumPy, Pandas, Scikit-learn, Pickle |
| PDF Generator  | ReportLab |
| ML Models Used | Logistic Regression, Support Vector Machine (SVC) |
| IDE            | VS Code / PyCharm / Jupyter |
| Deployment     | Localhost / Streamlit Cloud |

---

## 📂 Project Structure

- **Health-Guard/**
  - `diabetes_model.sav` — Trained Diabetes prediction model
  - `heart_model.sav` — Trained Heart Disease prediction model
  - `parkinsons_model.sav` — Trained Parkinson’s Disease model
  - `main.py` — Main Streamlit web application
  - `report_generator.py` — PDF report creation module
  - `requirements.txt` — Python dependencies list
  - `README.md` — Project documentation

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Shubhisri20/Health-Guard-Multiple-Disease-Pridiction-System.git
cd Health-Guard


python -m venv health_guard
health_guard\Scripts\activate        # Windows
source health_guard/bin/activate     # Mac/Linux

pip install -r requirements.txt
streamlit run main.py

```

