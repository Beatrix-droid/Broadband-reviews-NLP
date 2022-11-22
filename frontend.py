import streamlit as st
from keras.models import load_model
from helper import *


#helper imports to preprocess text for model

@st.cache  #to increase performance
def load_model():
    model=load_model("saved_model/model1")#load saved model
    return model

#######################################################
#ui code begins here

st.title("Review Classifier Model")

st.info("""Welcome to the broadband review classifier! Please enter the review you wish to classify.
        The model will give it a rating out of 4  where 1 is bad and 4 is good.""")
with st.form(key='my_form'):
    text= st.text_area('Enter the review you wish to classify:')
    button=st.form_submit_button('Classify this Review')
    
    if text and button:
        #process text
        text=clean_text(text)
        text=remove_non_ascii(text)
     
        #feed into model
        model_output= model.predict(text)

        #decode results and display them on page
        results= decode_output(model_output)
        st.write(f"{results}")






