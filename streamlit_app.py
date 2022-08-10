import streamlit as st
import pandas as pd

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True



def main():
    fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
    fruit_list = fruit_list.set_index('Fruit')

    st.title("Darren's Fruit Shack")

    st.header("Create Your Own Smoothie")

    fruits_selected = st.multiselect("Pick some fruits:", list(fruit_list.index),['Avocado','Strawberries'])
    fruits_to_show = fruit_list.loc[fruits_selected]

    st.dataframe(fruits_to_show)
    

    
    
if check_password():
    st.button("Click me", on_click=main())
