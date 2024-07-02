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

- Importing Libraries

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image
Imports necessary libraries for numerical operations, model loading, data handling, web app creation, and image processing.

Loading the Pre-trained Model
python
Copy code
try:
    with open("classifier.pkl", "rb") as pickle_in:
        classifier = pickle.load(pickle_in)
except FileNotFoundError:
    st.error("The model file 'classifier.pkl' was not found.")
    classifier = None
Attempts to load the pre-trained classifier model from a pickle file. Displays an error message if the file is not found.

Defining the Prediction Function
python
Copy code
def predict_note_authentication(variance, skewness, curtosis, entropy):
    if classifier:
        try:
            prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
            return prediction
        except Exception as e:
            st.error(f"Error in making prediction: {e}")
            return None
    else:
        st.error("Model not loaded.")
        return None
Defines a function to make predictions using the loaded model. Handles potential errors during prediction.

Main Function to Run the Streamlit App
python
Copy code
def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # User inputs for the features
    variance = st.text_input("Variance", "Type Here")
    skewness = st.text_input("Skewness", "Type Here")
    curtosis = st.text_input("Curtosis", "Type Here")
    entropy = st.text_input("Entropy", "Type Here")
    
    result = ""
    if st.button("Predict"):
        try:
            # Convert inputs to float for prediction
            variance = float(variance)
            skewness = float(skewness)
            curtosis = float(curtosis)
            entropy = float(entropy)
            result = predict_note_authentication(variance, skewness, curtosis, entropy)
            st.success('The output is {}'.format(result))
        except ValueError:
            st.error("Please enter valid numeric values.")
    
    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()

Title and Header: Sets the title and header of the app with custom HTML using st.markdown to embed HTML.
User Inputs: Creates text input fields for the user to input the four features using st.text_input.
Prediction Button: When clicked, converts inputs to float, calls the prediction function, and displays the result using st.button and st.success.
About Button: Displays additional information about the app using st.button and st.text.

Running the App
python
Copy code
if __name__ == '__main__':
    main()
Runs the main() function when the script is executed, starting the Streamlit app.