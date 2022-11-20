import streamlit as st

st.title("Review Classifier Model")


with st.form(key='my_form'):
    st.text_area('Enter the review you wish to classify:')

    st.form_submit_button('Classify this Review')


output_from_model="some output"

st.write(f"{output_from_model}")