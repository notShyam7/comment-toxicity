# -*- coding: utf-8 -*-
"""toxicity.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X6DivARVo-u0r4csDr8CBfhSb4w-QeQS
"""

import streamlit as st
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('/content/gdrive/MyDrive/Comment Toxicity/toxicity.h5')

# Function to preprocess the input text using Embedding layer
embedding_layer = model.layers[0]  # Assuming Embedding layer is the first layer

def preprocess_text(text):
    text = [text]  # Convert to a list
    # Convert input text to integer sequences using the embedding layer
    vectorized_text = embedding_layer(tf.constant(text))
    return vectorized_text

# Function to predict toxicity
def predict_toxicity(text):
    vectorized_text = preprocess_text(text)
    prediction = model.predict(vectorized_text)
    return prediction[0]

# Streamlit app
st.title("Comment Toxicity Predictor")

# Input text box for user input
user_input = st.text_area("Enter your comment:", "")

if st.button("Predict"):
    if user_input:
        prediction = predict_toxicity(user_input)
        if prediction >= 0.5:
            st.write("This comment is toxic.")
        else:
            st.write("This comment is not toxic.")
    else:
        st.write("Please enter a comment.")

