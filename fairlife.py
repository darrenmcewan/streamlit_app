from lxml import html 
import requests
import streamlit as st

def check(products):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'} 
    fairlife_flavors = ['Chocolate','Vanilla','Salted Caramel','Strawberry']
    fairlife_links = ['https://www.samsclub.com/p/fairlife-nutrition-plan-chocolate-30-g-protein-shake-11-5-fl-oz-12-pk/prod24381709',
                      'https://www.samsclub.com/p/fairlife-nutrition-plan-vanilla-11-5-fl-oz-12pk/prod24522971?xid=plp_product_6',
                      'https://www.samsclub.com/p/fairlife-nutrition-plan-salted-caramel-30-g-protein-shake-11-5-fl-oz-12-pk/prod24964063',
                      'https://www.samsclub.com/p/premier-high-protein-shake-strawberry/prod24964333?xid=plp_product_3']
    
    items = dict(zip(fairlife_flavors, fairlife_links))
    
    for i in products:
        page = requests.get(items[i], headers=headers) 
        doc = html.fromstring(page.content)
        # extract product name
        XPATH_NAME = doc.xpath('//html/head/title/text()')
        # checking availaility 
        XPATH_AVAILABILITY = doc.xpath('//meta[@content="InStock"]')

        if len(XPATH_AVAILABILITY) == 1:
            body_of_email = 'In Stock!\n\n' + XPATH_NAME[0] + '\n\n' + f'{i}'
            email_subject = 'In Stock! ' + XPATH_NAME[0]
            st.text('In Stock! ' + XPATH_NAME[0])
            #send_email_gmail(email_subject, body_of_email, "darren@mcewan.me")
            #print('Email sent!')
            #print()
        else:
            st.text('Out of Stock' + XPATH_NAME[0])
            #print(XPATH_NAME[0])
    
            continue