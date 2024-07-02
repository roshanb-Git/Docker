# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:50:04 2024

@author: Roshan Bandara
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:50:04 2024

@author: Roshan Bandara
"""

#Importing libraries
import numpy as np
import pickle
import pandas as pd
import streamlit as st 

#potential image handling
from PIL import Image

# Load the pre-trained classifier model
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)



# Define the prediction function
def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction


# Define the main function to run the Streamlit app
def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    