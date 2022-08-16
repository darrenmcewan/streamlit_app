from lxml import html 
import requests
import streamlit as st
from email.message import EmailMessage
import smtplib 

def send_email_gmail(subject, message, destination):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #This is where you would replace your password with the app password
    server.login('darrengmcewan@gmail.com', st.secrets["email_password"])

    msg = EmailMessage()

    message = f'{message}\n'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = 'darrengmcewan@gmail.com'
    msg['To'] = destination
    server.send_message(msg)

def check(products, email):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'} 
    fairlife_flavors = ['Chocolate','Vanilla','Salted Caramel','Strawberry']
    fairlife_links = ['https://www.samsclub.com/p/fairlife-nutrition-plan-chocolate-30-g-protein-shake-11-5-fl-oz-12-pk/prod24381709',
                      'https://www.samsclub.com/p/fairlife-nutrition-plan-vanilla-11-5-fl-oz-12pk/prod24522971?xid=plp_product_6',
                      'https://www.samsclub.com/p/fairlife-nutrition-plan-salted-caramel-30-g-protein-shake-11-5-fl-oz-12-pk/prod24964063',
                      'https://www.samsclub.com/p/premier-high-protein-shake-strawberry/prod24964333?xid=plp_product_3']
    
    items = dict(zip(fairlife_flavors, fairlife_links))
    
        
    body_of_email = ""
    email_subject = "Fairlife Availability"
    
        
    for i in products:
        page = requests.get(items[i], headers=headers) 
        doc = html.fromstring(page.content)
        # extract product name
        XPATH_NAME = doc.xpath('//html/head/title/text()')
        # checking availaility 
        XPATH_AVAILABILITY = doc.xpath('//meta[@content="InStock"]')

        if len(XPATH_AVAILABILITY) == 1:
            body_of_email += 'In Stock!\n\n' + XPATH_NAME[0] + '\n\n' + f'{items[i]}'
            st.write(f'✅ [In Stock!]({items[i]}) ' + XPATH_NAME[0])
           
        else:
            body_of_email += '❌ Out of Stock' + XPATH_NAME[0]
            st.write('\n\n❌ Out of Stock' + XPATH_NAME[0])
            continue
        
    st.success('Check finished!')
    if email != "":
            send_email_gmail(email_subject, body_of_email, email)
            st.success(f'Email sent to {email}')
           
    else:
        st.error("Error sending email")
    
        