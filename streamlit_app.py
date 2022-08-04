import streamlit
import pandas as pd

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')

streamlit.title("Darren's Fruit Shack")

streamlit.header("Create Your Own Smoothie")

streamlit.multiselect("Pick some fruits:", list(fruit_list.index))
streamlit.dataframe(fruit_list)

