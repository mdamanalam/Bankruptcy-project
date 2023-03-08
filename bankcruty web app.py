# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:05:09 2023

@author: 91808
"""

import numpy as np
import pickle
import streamlit as st

st.title('Bankruptcy Prediction Web App')
st.sidebar.header('User Input Parameters')

# loding the saved model
loaded_model = pickle.load(open('C:/Users/91808/OneDrive/Desktop/trained_model.sav','rb'))

input_data = (0,0,0.5,0.5,0.5,0)


# creating a function for prediction

def bankruptcy_prediction(input_data):
    
    

    #changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for  one instance
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0] == 0):
      return'The company is going to bankrupt'
    else:
      return'The company is non-bankrupt'
      
      
def main():

   # giving a title 
   st.title('User Input Parameters')
   
   #getting the input data from the user
   
      
   industrial_risk = st.text_input('Parameter for industrial_risk')
   management_risk = st.text_input('Parameter for management_risk')
   financial_flexibility = st.text_input('Parameter for financial_flexibility')
   credibility = st.text_input('Parameter for credibility')
   competitiveness = st.text_input('Parameter for competitiveness')
   operating_risk = st.text_input('Parameter for operating_risk')
   
   # code for prediction
   bankruptcy = ''
   
   # creating a button for prediction
   
   if st.button('Bankruptcy Result'):
       bankruptcy = bankruptcy_prediction([industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk])
       
   st.success(bankruptcy)


if __name__ == '__main__':
    main()