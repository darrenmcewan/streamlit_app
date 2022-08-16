import streamlit as st
import pandas as pd
import base64

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
    
    tab1, tab2, tab3 = st.tabs(["Projects", "Resume", "Hobbies"])
    
    with tab1:
        
        st.title("Darren's Fairlife Checker")

        st.header("Which item should we check?")
        fairlife_flavors = ['Chocolate','Vanilla','Salted Caramel','Strawberry']
        fairlife_images = ['imgs\chocolate.png', 'imgs\vanilla.png','imgs\salted_caramel.png','imgs\strawberry.png']
        #fairlife_selected = st.multiselect("Select Flavor:", fairlife_flavors,['Chocolate'])
        
        images = dict(zip(fairlife_flavors, fairlife_images))

        user_option = st.multiselect("Choose an item", fairlife_flavors,['Chocolate'])
        
        st.image([images[x] for x in user_option])
    
    with tab2:
        st.header('Education & Work')
        pdfFileObj = open('PDFs/Darren_McEwan_Resume-2022.pdf', 'rb')
        st.download_button('Download Resume',pdfFileObj,file_name='Darren_McEwan_Resume-2022.pdf',mime='pdf')
        
        pdf_file = 'PDFs/Darren_McEwan_Resume-2022.pdf'
        with open(pdf_file,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
        st.write('📧: darren@mcewan.me')
        
        
if check_password():
    main()
