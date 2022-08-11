import streamlit as st
import pandas as pd

def check_password():
    def password_entered():
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
    st.sidebar.caption('Wish to connect?')
    st.sidebar.write('📧: darren@mcewan.me')
    pdfFileObj = open('PDFs/Darren_McEwan_Resume-2022.pdf', 'rb')
    st.sidebar.download_button('Download Resume',pdfFileObj,file_name='Darren_McEwan_Resume-2022.pdf',mime='pdf')
    
    tab1, tab2, tab3 = st.tabs(["Projects", "Resume", "Hobbies"])
    
    with tab1:
        fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
        fruit_list = fruit_list.set_index('Fruit')

        st.title("Darren's Fruit Shack")

        st.header("Create Your Own Smoothie")

        fruits_selected = st.multiselect("Pick some fruits:", list(fruit_list.index),['Avocado','Strawberries'])
        fruits_to_show = fruit_list.loc[fruits_selected]

        st.dataframe(fruits_to_show)
    
    with tab2:
        pdf_file = 'PDFs/Darren_McEwan_Resume-2022.pdf'
        with open(pdf_file,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = F'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>’
        st.markdown(pdf_display, unsafe_allow_html=True)
    
if check_password():
    main()
