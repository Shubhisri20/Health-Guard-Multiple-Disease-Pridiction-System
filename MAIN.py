import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu 


# ---------------------- PAGE CONFIGURATION ----------------------
st.set_page_config(
    page_title="Health Guard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for modern UI
st.markdown("""
    <style>
        .main {background-color: #ffffff;}
        .stButton>button {
            background-color: #0d6efd;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 18px;
        }
        .stButton>button:hover {
            background-color: #084298;
            color: #fff;
        }
        .css-1d391kg, .css-12oz5g7, .css-1v3fvcr {
            background-color: #f0f7ff !important;
        }
        .css-10trblm, .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1px solid #0d6efd;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- WORKING DIRECTORY ----------------------
working_dir = os.path.dirname(os.path.abspath(__file__))

# ---------------------- MODEL LOADING ----------------------
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open(f'{working_dir}/heart_model.sav', 'rb'))
parkison_model = pickle.load(open(f'{working_dir}/parkison_model.pkl', 'rb'))

# ---------------------- SIDEBAR NAVIGATION ----------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=130)
    selected = option_menu(
        menu_title="Multi Disease Predictor",
        options=['Diabetes Prediction', 'Heart Disease Prediction', 'Parkison Prediction'],
        icons=['activity', 'heart-pulse', 'person'],
        menu_icon="hospital-fill",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#e6f0ff"},
            "icon": {"color": "#0d6efd", "font-size": "20px"},
            "nav-link": {"font-size": "18px", "color": "#000000", "text-align": "left"},
            "nav-link-selected": {"background-color": "#0d6efd", "color": "white"},
        }
    )

# ---------------------- DIABETES PREDICTION SECTION ----------------------
if selected == 'Diabetes Prediction':
    st.markdown("<h1 style='text-align:center; color:#0d6efd;'>🩺 Diabetes Prediction Using Machine Learning</h1>", unsafe_allow_html=True)
    st.write("### Enter Patient Details")

    col1, col2, col3 = st.columns(3)
    with col1: pregnancies = st.text_input("Number of Pregnancies")
    with col2: glucose = st.text_input("Glucose Level")
    with col3: bloodpressure = st.text_input("Blood Pressure Value")
    with col1: skinthickness = st.text_input("Skin Thickness")
    with col2: insulin = st.text_input("Insulin Level")
    with col3: bmi = st.text_input("BMI Value")
    with col1: diabetespedigreefunction = st.text_input("Diabetes Pedigree Function")
    with col2: age = st.text_input("Age")

    diab_diagnosis = ""
    if st.button("Predict Diabetes"):
        user_input = [float(x) for x in [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]]
        diab_prediction = diabetes_model.predict([user_input])

        diab_diagnosis = "🟥 The Person is Diabetic" if diab_prediction[0] == 1 else "🟩 The Person is Not Diabetic"
    st.success(diab_diagnosis)

# ---------------------- HEART DISEASE PREDICTION SECTION ----------------------
if selected == 'Heart Disease Prediction':
    st.markdown("<h1 style='text-align:center; color:#0d6efd;'>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1: age = st.text_input("Age")
    with col2: sex = st.text_input("Gender (1=Male, 0=Female)")
    with col3: cp = st.text_input("Chest Pain Type")
    with col1: trestbps = st.text_input("Resting BP")
    with col2: chol = st.text_input("Cholesterol")
    with col3: fbs = st.text_input("Fasting Blood Sugar")
    with col1: restcg = st.text_input("Resting ECG")
    with col2: thalach = st.text_input("Max Heart Rate")
    with col3: exang = st.text_input("Exercise Angina")
    with col1: oldpeak = st.text_input("Oldpeak")
    with col2: slope = st.text_input("Slope")
    with col3: ca = st.text_input("CA")
    with col1: thal = st.text_input("Thal")

    heart_diagnosis = ""
    if st.button("Predict Heart Condition"):
        try:
            user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal]]
            heart_prediction = heart_model.predict([user_input])
            heart_diagnosis = "🟥 The Person Has Heart Disease" if heart_prediction[0] == 1 else "🟩 The Person is Healthy"
        except:
            heart_diagnosis = "❌ Please enter valid numeric values"

    st.success(heart_diagnosis)

# ---------------------- PARKINSON PREDICTION SECTION ---------------------

# ---------------------- PARKINSON PREDICTION SECTION ----------------------
if selected == 'Parkison Prediction':
    st.markdown("<h1 style='text-align:center; color:#0d6efd;'>🧠 Parkinson Disease Detection</h1>", unsafe_allow_html=True)

    inputs = []
    col1, col2, col3 = st.columns(3)
    features = ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "Jitter(%)", "Jitter_Abs", "RAP", "PPQ", "DDP",
                "Shimmer", "Shimmer (dB)", "APQ3", "APQ5", "APQ", "DDA", "NHR", "HNR", "RPDE", "DFA",
                "Spread1", "Spread2", "D2", "PPE"]

    for i, f in enumerate(features):
        if i % 3 == 0:
            inputs.append(col1.text_input(f))
        elif i % 3 == 1:
            inputs.append(col2.text_input(f))
        else:
            inputs.append(col3.text_input(f))

    park_diagnosis = ""
    values = []

    if st.button("Predict Parkinson"):
        values = [float(x) for x in inputs]
        prediction = parkison_model.predict([values])
        park_diagnosis = "🟥 Parkinson Positive" if prediction[0] == 1 else "🟩 Parkinson Negative"

    st.success(park_diagnosis)