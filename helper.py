import re 
from gensim.parsing.preprocessing import remove_stopwords #to remove common words
from nltk.stem import WordNetLemmatizer
import numpy as np

lemmatizer = WordNetLemmatizer()


REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
remove_chars=re.compile('/[!@#$%^&*]/g')
lables={"Bad": 1, "Mediocre":2 ,"Satisfactory":3, "Good":4}
class_names = list(lables.keys())


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


def decode_output(model_output: list[int]) -> str:
    
    """Decodes the output of the model and converts it back to text."""

    results= {"Probability: ": np.max(model_output[0]), "Classified: ":  class_names[np.argmax(model_output[0])], "Probability Array": model_output[0]}

    return results