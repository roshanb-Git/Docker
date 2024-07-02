# Streamlit Banknote Authenticator Documentation

## Overview
- This application is a Streamlit-based web app that uses a pre-trained machine learning model to predict the authenticity of banknotes based on four features: variance, skewness, curtosis, and entropy.

### File Structure
- classifier.pkl: The pre-trained machine learning model saved in a pickle file.
- app_streamlit.py: The main Python script for running the Streamlit app.

### Libraries Used
- numpy: For numerical operations.
- pickle: For loading the pre-trained model.
- pandas: For data manipulation (not used in the current version, but commonly included for data handling).
- streamlit: For creating the web app.
- PIL (Python Imaging Library): For potential image handling.

### Streamlit Key Points
1) Easy to Use: Streamlit allows you to turn Python scripts into interactive web applications with minimal code.
2) Widgets: Streamlit provides a variety of widgets like text input, buttons, sliders, and more to capture user input.
3) Real-time Updates: Automatically updates the app in real-time when changes are made to the script or user input.
4) Markdown Support: Allows embedding of HTML and Markdown for formatting text and adding styles.
5) Deployment: Easy to deploy on various platforms, including Streamlit Cloud.


## Script Breakdown

1) Importing Libraries
Imports necessary libraries for numerical operations, model loading, data handling, web app creation, and image processing.
    - import numpy as np
    - import pickle
    - import pandas as pd
    - import streamlit as st 
    - from PIL import Image


2) Loading the Pre-trained Model
Attempts to load the pre-trained classifier model from a pickle file.
    - pickle_in = open("classifier.pkl","rb")
    - classifier=pickle.load(pickle_in)
 

3) Defining the Prediction Function
Defines a function to make predictions using the loaded model.
    - def predict_note_authentication(variance,skewness,curtosis,entropy):
       - prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
       - print(prediction)
       - return prediction

#### Main Function to Run the Streamlit App

- Title and Header: Sets the title and header of the app with custom HTML using st.markdown to embed HTML.
- User Inputs: Creates text input fields for the user to input the four features using st.text_input.
- Prediction Button: When clicked, converts inputs to float, calls the prediction function, and displays the result using st.button and st.success.
- About Button: Displays additional information about the app using st.button and st.text.

  
        def main():
            st.title("Bank Authenticator")
            html_temp = """
            <div style="background-color:tomato;padding:10px">
            <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
            </div>
        """

        # User inputs for the features
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



#### Running the App
Runs the main() function when the script is executed, starting the Streamlit app.
    if __name__ == '__main__':
        main()

