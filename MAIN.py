import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu 


# Set page configuration
st.set_page_config(page_title="Health Gaurd", layout = "wide") 


# Setting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))                                          
 

# Loading the saved models 
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav ','rb'))
heart_model = pickle.load(open(f'{working_dir}/heart_model.sav','rb'))
parkison_model = pickle.load(open(f'{working_dir}/parkison_model.pkl','rb'))


# Side bar for navigation
with st.sidebar:
          selected = option_menu('Multiple Disease Prediction System', ['Diabetes Prediction' , 'Heart Disease Prediction','Parkison Prediction'] , menu_icon = 'hospital-fill' , icons = ['activity' , 'heart'] , default_index = 0) 


# Diabetes Prediction Page
if selected == 'Diabetes Prediction' : 
                 # Page Title 
                   st.title('Diabetes Prediction Using ML')
                 # Setting up the number of columns with the name
                   col1,col2,col3 = st.columns(3)
                   
                   with col1:
                             pregnancies = st.text_input("Number of Pregnancies")
                             

                   with col2:
                             glucose = st.text_input("Glucose Level") 

                   with col3:
                             bloodpressure = st.text_input("Blood Pressure Value")

                   with col1:
                             skinthickness = st.text_input("Skin Thickness")
                             

                   with col2:
                             insulin = st.text_input("Insulin Level")

                   with col3:
                             bmi = st.text_input("BMI Value")

                   with col1:
                             diabetespedigreefunction = st.text_input("Diabetes Pedigree Function")
                             

                   with col2:
                             age = st.text_input("Age of the Person")


                   # code for Prediction
                   diab_diagnosis = ''
               
                   # creation of button 
                   if st.button('Diabetes Test Result'):
                         user_input =[pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age]
                         
                         user_input = [float(x) for x in user_input]
 
                         diab_prediction = diabetes_model.predict([user_input])

                         if diab_prediction[0] == 1:
                                 diab_diagnosis = "The Person is Diabetic"
                         else:
                              diab_diagnosis = "The Person is not diabetic" 
                   st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    # Page Title
    st.title('Heart Disease Prediction')

    # Setting up the number of columns with the name
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Enter Age")
    with col2:
        sex = st.text_input("Gender")
    with col3:
        cp = st.text_input("CP")
    with col1:
        trestbps = st.text_input("Trestbps")
    with col2:
        chol = st.text_input("Cholesterol")
    with col3:
        fbs = st.text_input("FBS")
    with col1:
        restcg = st.text_input("RestCG")
    with col2:
        thalach = st.text_input("Thalach")
    with col3:
        exang = st.text_input("Exang")
    with col1:
        oldpeak = st.text_input("Oldpeak")
    with col2:
        slope = st.text_input("Slope")
    with col3:
        ca = st.text_input("CA")
    with col1:
        thal = st.text_input("Thal")

    # Code for Prediction
    heart_diagnosis = ''

    # Creation of button
    if st.button('Heart Test Result'):
        try:
            # Convert inputs to float and predict
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                          float(restcg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
            
            heart_prediction = heart_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = "The Person is having heart disease"
            else:
                heart_diagnosis = "The Person is not having heart disease"
        except ValueError:
            heart_diagnosis = "Please enter valid input values."

    st.success(heart_diagnosis)


if selected == 'Parkison Prediction':
    st.title("Parkison Disease Detection")

    col1, col2, col3 = st.columns(3)

    with col1:
        Fo_Hz = st.text_input("Enter MDVP:Fo(Hz)")
    with col2:
        Fhi_Hz = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        Flo_Hz = st.text_input("Enter MDVP:Flo(Hz)")
    with col1:
        Jitter_per = st.text_input("Enter Jitter(%)")
    with col2:
        Jitter_Abs = st.text_input("Enter Jitter_Abs")
    with col3:
        rap = st.text_input("Enter RAP")
    with col1:
        ppq = st.text_input("Enter PPQ")
    with col2:
        ddp = st.text_input("Enter DDP")
    with col3:
        shimmer = st.text_input("Enter shimmer ")
    with col1:
        shimmer_db = st.text_input("Enter Shimmer (Db)")
    with col2:
        apq3 = st.text_input("Enter Shimmer (APQ3)")
    with col3:
        apq5 = st.text_input("Enter Shimmer (APQ5)")
    with col1:
        apq = st.text_input("Enter APQ")
    with col2:
        dda = st.text_input("Enter Shimmer: DDA")
    with col3:
        nhr = st.text_input("Enter NHR")
    with col1:
        hnr  = st.text_input("Enter HNR")
    with col2:
        rpde = st.text_input("Enter RPDE")
    with col3:
        dfa = st.text_input("Enter DFA")
    with col1:
        spread1 = st.text_input("Enter Spread1")
    with col2:
        spread2 = st.text_input("Enter Spread 2")
    with col3:
        d2 = st.text_input("Enter D2")
    with col1: 
        ppe = st.text_input("Enter PPE")   
    
    park_diagnosis = ''
               
    # creation of button 
    if st.button('Diabetes Test Result'):
            user_input =[Fo_Hz,Fhi_Hz,Flo_Hz,Jitter_per,Jitter_Abs,
                         rap,ppq, ddp,shimmer,shimmer_db,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]
            
            user_input = [float(x) for x in user_input]

            park_prediction = parkison_model.predict([user_input])

            if park_prediction[0] == 1:
                    park_diagnosis = "The Person is Parkison Positive"
            else:
                park_diagnosis = "The Person is not Parkison Positive" 
    st.success(park_diagnosis)
