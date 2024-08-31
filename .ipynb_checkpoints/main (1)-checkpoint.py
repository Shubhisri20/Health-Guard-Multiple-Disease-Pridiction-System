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



# Side bar for navigation
with st.sidebar:
          selected = option_menu('Multiple Disease Prediction System', ['Diabetes Prediction' , 'Heart Disease Prediction'] , menu_icon = 'hospital-fill' , icons = ['activity' , 'heart'] , default_index = 0) 


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


 

            
                        
                         











