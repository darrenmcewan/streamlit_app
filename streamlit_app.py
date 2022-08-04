import streamlit
import pandas as pd

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.header("List of Fruits")
streamlit.dataframe(fruit_list)

