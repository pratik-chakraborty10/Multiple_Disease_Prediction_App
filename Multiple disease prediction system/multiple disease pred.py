#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:13:30 2024

@author: pratikchakraborty
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np


#loading saved models
diabetes_model=pickle.load(open('/Users/pratikchakraborty/Desktop/Multiple disease prediction system/saved models/trained_model.sav','rb'))

heart_disease_model=pickle.load(open('/Users/pratikchakraborty/Desktop/Multiple disease prediction system/saved models/heart_disease_model.sav','rb'))


#sidebar navigation

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System Using ML', ['Diabetes Prediction','Heart Disease Prediction'],icons=['bandaid','activity'],default_index=0)
    
    
#Diabetes prediction page

if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    #columns for the input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose=st.text_input('Glucose Level')
    
    with col3:
        BloodPressure=st.text_input('Blood Pressure Level')
        
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin=st.text_input('Insulin Value')
        
    with col3:
        BMI=st.text_input('BMI Level')
        
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabtes Pedigree Function Value')
        
    with col2:
        
        Age=st.text_input('Age of the person')
        
    
    
    
    
   
   
    
    
    
    
    
    #code for prediction
    diab_diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if(diab_prediction[0]==1):
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is non diabetic'
            
    st.success(diab_diagnosis)
    

# Heart disease prediction
    
if(selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    
    
    
    
    # Convert input values to numeric types
    
    
   
    
    
    
    
    
    
   
   
    
    
    col1,col2,col3=st.columns(3)
        
    with col1:
           
            age=st.text_input('Age')
            
            
    with col2:
            sex=st.text_input('sex')
            
            
    with col3:
            cp=st.text_input('Chest Pain Types')
            
            
    with col1:
            trestbps=st.text_input('Resting Blood Pressure')
            
            
    with col2:
            chol=st.text_input('serum Cholestral in mg/dl')
            
            
    with col3:
            fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl')
            
            
    with col1:
            restecg=st.text_input('Resting ElectroCardioGraphic Result')
            
            
    with col2:
            thalach=st.text_input('Maximum Heart rate acheived')
            
            
    with col3:
            exang=st.text_input('Exercise Induced Angina')
            
            
    with col1:
            oldpeak=st.text_input('ST depression induced by exercise')
            
            
    with col2:
            slope=st.text_input('slope of the peak exercise ST segment')
            
            
    with col3:
            ca=st.text_input('Major vessels colored by flourosopy')
            
            
    with col1:
            thal=st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
            
            
            
        # code for prediction
        
    heart_diagonosis=''
        
        #creating a button for prediction
        
    if st.button('Heart Disease Test Result'):
            #heart_prediction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
            # Convert input values to floats
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]
            
            heart_prediction = heart_disease_model.predict([user_input])
            
            if(heart_prediction[0] == 1):
                heart_diagonosis='The person is having heart disease'
            else:
                heart_diagonosis='The person does not have any heart disease'
                
    st.success(heart_diagonosis)
        
    
        
