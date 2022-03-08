# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:30:04 2022

@author: 91863
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def insurance_premium_prediction(age,sex,bmi,children,smoker,region):
    
    """Let's predict the insurance premiums 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: age
        in: query
        type: number
        required: true
      - name: sex
        in: query
        type: number
        required: true
      - name: bmi
        in: query
        type: number
        required: true
      - name: children
        in: query
        type: number
        required: true
      - name: smoker
          in: query
          type: number
          required: true
      - name: region
            in: query
            type: number
            required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=model.predict([[age,sex,bmi,children,smoker,region]])
    print(prediction)
    return prediction



def main():
    st.title("Insurance Premium Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Insurance Premium Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","Type Here")
    sex = st.text_input("sex","Type Here")
    bmi = st.text_input("bmi","Type Here")
    children = st.text_input("children","Type Here")
    smoker = st.text_input("smoker","Type Here")
    region = st.text_input("region","Type Here")
    result=""
    if st.button("Predict"):
        result=insurance_premium_prediction(age,sex,bmi,children,smoker,region)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()