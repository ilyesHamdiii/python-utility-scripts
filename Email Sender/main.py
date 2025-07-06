# thats a protoytype of how sending an email via python (CLI)




from email.message import EmailMessage
from dotenv import load_dotenv
import ssl
import smtplib
email_sender=" "
load_dotenv()
class Mail():
    def __init__(self,name,password):
        self.name=name
        self.password=password
    def getinfo(self):
        print(f"the name is {self.name}")
        print(f"the password is {self.password}")


def email_sender(object_sender,object_receiver):
    subjet=input("provide the email subject ")
    body=input("provide the email body ")
    em=EmailMessage()
    em['Form']=object_sender.name
    em['to']=object_receiver.name
    em['subject']=subjet
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(object_sender.name,object_sender.password)
        smtp.sendmail(object_sender.name,object_receiver.name,em.as_string())