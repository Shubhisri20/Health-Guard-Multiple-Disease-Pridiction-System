📌 Health Guard – Multiple Disease Prediction System
AI-powered health prediction app built with Machine Learning & Streamlit

The Health Guard application allows users to input medical attributes and predicts the likelihood of multiple diseases including Diabetes, Heart Disease, and Parkinson’s Disease.
It uses trained machine learning models and provides an intuitive UI built in Streamlit. The project also features PDF report generation for prediction summaries.

🚀 Features

✔ Predict Diabetes, Heart Disease, and Parkinson’s Disease
✔ Streamlit-based clean and interactive UI
✔ Machine Learning model integration (Logistic Regression / SVM)
✔ Medical report summary generated as PDF
✔ Modular & scalable code structure
✔ User-friendly responsive interface

🖥 Tech Stack
Category	Technology
Frontend UI	Streamlit
Backend	Python
Libraries	NumPy, Pandas, Scikit-learn, Pickle
PDF Generator	ReportLab
Models Used	Logistic Regression, Support Vector Machine (SVC)
IDE	VS Code / PyCharm / Jupyter
Deployment	Localhost / Streamlit Cloud
📂 Project Structure
Health-Guard/
│
├── diabetes_model.sav
├── heart_model.sav
├── parkinsons_model.sav
│
├── main.py               # Main Streamlit App
├── report_generator.py   # PDF export module
│
├── requirements.txt
└── README.md

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Shubhisri20/Health-Guard-Multiple-Disease-Pridiction-System.git
cd Health-Guard

2️⃣ Create a Virtual Environment
python -m venv health_guard
health_guard\Scripts\activate      # For Windows
source health_guard/bin/activate   # For Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run main.py

📊 Machine Learning Models
Disease	Algorithm	Accuracy
Diabetes	Logistic Regression	~85%
Heart Disease	Logistic Regression	~88%
Parkinson’s Disease	Support Vector Machine (SVC)	~93%

Models were trained on publicly available datasets from Kaggle.