This code is for a Streamlit app with two functions: check_password() and main().
Function: check_password()

This function creates a password-protected login screen for the Streamlit app. If the user enters the correct password (which is stored in Streamlit secrets), they will gain access to the main part of the app.
Function: main()

This function is the main part of the app. It consists of three tabs: Projects, Resume, and Hobbies.
Tab 1: Projects

This tab contains a Fairlife checker which checks the Sam's Club website for the selected flavor of Fairlife nutrition shakes and sends an email to the user (if requested) when the product is available. It also allows the user to sign up for automatic notifications for available Fairlife products.
Tab 2: Resume

This tab contains a downloadable PDF resume and the email address of the app creator.
External modules used

This code uses the following external modules:

    streamlit
    pandas
    base64
    requests
    lxml.html
    fairlife (custom module)
    datetime
    email.message
    smtplib

Note

In order to use the email functionality, the user will need to replace the email and password in send_email_gmail() with their own Gmail address and an app password (which can be generated in the Google account settings).
