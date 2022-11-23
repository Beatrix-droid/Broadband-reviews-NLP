import re 
from gensim.parsing.preprocessing import remove_stopwords #to remove common words
from nltk.stem import WordNetLemmatizer
import numpy as np
import tensorflow as tf


lemmatizer = WordNetLemmatizer()


REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
remove_chars=re.compile('/[!@#$%^&*]/g')
lables={"Bad": 1.0, "Mediocre":2.0 ,"Satisfactory":3.0, "Good":3.5}
class_names = list(lables.keys())

#max words to be used.
MAX_WORDS=5000 
#max no of words per complaint:
MAX_SEQUENCE=250
#fixed
EMBEDDING_DIM=250


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

    """Removes non ascii characters"""

    return ''.join(char for char in string if ord(char) < 128)


def encode_text(text: str):
   
    """Make prediction based on user input"""


    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=MAX_WORDS)
    tokenizer.fit_on_texts(text)

    model_input = tokenizer.texts_to_sequences(text) 
    model_input = tf.keras.utils.pad_sequences(model_input, maxlen=MAX_SEQUENCE)
    return model_input


def decode_output(model_output: list[int]) -> str:
    
    """Decodes the output of the model and converts it back to text."""

    results= {"Probability": np.max(model_output[0]), "Classified":  class_names[np.argmax(model_output[0])], "Probability Array": model_output[0]}

    return results
