import streamlit as st
from keras.models import load_model
import os

#helper imports to preprocess text for model
import re 
from gensim.parsing.preprocessing import remove_stopwords #to remove common words
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
remove_chars=re.compile('/[!@#$%^&*]/g')
def clean_text(text: str) -> str:
    """
        text: a string
        
        return: modified initial string with non ascii characters, other special characters and stop words removed.
        Words are also converted to lower case and lemmatized.
    """
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
    text=remove_chars.sub(" ", text)
    text = remove_stopwords(text)
    return text
    

def remove_non_ascii(string: str) -> str:
    return ''.join(char for char in string if ord(char) < 128)
#model=load_model("saved_model/model1")#load saved model


#######################################################
#ui code begins here

st.title("Review Classifier Model")

st.info("""Welcome to the broadband review classifier! Please enter the review you wish to classify.
        The model will give it a rating out of 4  where 1 is bad and 4 is good.""")
with st.form(key='my_form'):
    text= st.text_area('Enter the review you wish to classify:')
    button=st.form_submit_button('Classify this Review')
    
    if text and button:
        text=clean_text(text)
        text=remove_non_ascii(text)
        output_from_model="some output"
        st.write(f"{text}")

prediction_lables={"Bad": 1, "Mediocre":2 ,"Satisfactory":3, "Good":4}


