import spacy
import streamlit as st
from collections import defaultdict


def get_data(name):
    
    nlp = None
    if name == "Small":
        nlp = spacy.load("en_core_web_sm")
    elif name == "Medium":
        nlp = spacy.load("en_core_web_md")
    else:
        return None

    return nlp

# sidebar
st.sidebar.title("Select data size")
model_size = st.sidebar.selectbox(
    'Options', 
    ('Small', 'Medium')
    )


# Mainbar

st.title("Named Entity Recognition using Spacy and Streamlit")

nlp = get_data(model_size)

st.write("Spacy can predict all possible entities such Person, Companies, Countries and more")

input_text = st.text_input("Enter a input text")

result = nlp(input_text)


entities = defaultdict(list)
for entity in result.ents:
    entities[entity.label_].append(entity.text)


st.write(entities)