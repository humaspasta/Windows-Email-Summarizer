import os
import json
import time
import imaplib
from email.policy import default
import email
import google.auth
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import win11toast
import google.generativeai as gemini

# Path to the JSON file you downloaded

file_name = 'secret file here'
full_path = os.path.abspath(file_name)
print("file path full")
print(full_path)
print()
CLIENT_SECRETS_FILE = full_path
split_path = CLIENT_SECRETS_FILE.split('\\')
print("Split file {}".format(split_path))

actual_path = ""

for item in split_path:
    actual_path += item + "\\"

actual_path = actual_path[:-1]






# Scopes required for accessing Gmail
SCOPES = ['https://mail.google.com/']

# Authenticate and obtain credentials
flow = InstalledAppFlow.from_client_secrets_file(r'secret file', SCOPES)
creds = flow.run_local_server(port=0)

# Save the credentials for future use
with open('token.json', 'w') as token:
    token.write(creds.to_json())

# Load the credentials from the saved file
creds = Credentials.from_authorized_user_file('token.json', SCOPES)

# Create the OAuth2 authentication string


#print("Authenticated String: {}".format(auth_string))

user = '#username here'
password = '#password here'


if creds.expired and creds.refresh_token:
    creds.refresh(google.auth.transport.requests.Request())
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

def get_Auth(x):
    auth_string = 'user=%s\1auth=Bearer %s\1\1' % (user, creds.token)
    return auth_string

mail = imaplib.IMAP4_SSL(host='imap.gmail.com')

mail.authenticate('XOAUTH2' , get_Auth)
print()
print("your in")
print()
mail.select("INBOX")
type , data = mail.search(None , 'ALL')

Heading = ''
body = ''
heading_body_dictionary = {}

for item in data[0].split():
    res , data = mail.fetch(item , '(RFC822)')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email , policy=default)
    date = "date: {}".format(msg['date']) 
    sender = "{}".format(msg['From'])
    
    print(sender)


    if msg.is_multipart():
            for part in msg.iter_parts():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8')
   
   
          
    try:
        if(sender.index("TLDR") > -1):
            heading_body_dictionary[sender] = body
    except:
        pass


keys = list(heading_body_dictionary.keys())
print(heading_body_dictionary.get(keys[0]))
#gemini.set= 'AIzaSyBNHow-SfB2qsC1uAEeODAB4Crvi5scBCw'
gemini.configure(api_key='AIzaSyBNHow-SfB2qsC1uAEeODAB4Crvi5scBCw')

model = gemini.GenerativeModel(model_name="models/gemini-1.5-flash")

  
prompt= "Please sumerize the following in one word answers" + heading_body_dictionary.get(keys[0])

summery = model.generate_content(prompt)


win11toast.notify(title= "New TLDR Update" , body= summery.text)
print(f"Output token count: {summery.usage_metadata.prompt_token_count}")


mail.logout()

    







    

    






        
 
    
    
    
    
    









#506384305115-uab9qrenqoh0geavnor5qacfm7ff9ref.apps.googleusercontent.com # client id






























'''
def __init__(self, user_email_address_1 , user_password_1) -> None:
    user_email_address = user_email_address_1
    user_password = user_password_1

def get_body(self , msg):
    if msg.is_multiplier():
        return msg.get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None , True)
        
def search(self, key , val):
    result , data = self.con.search(None , key , '"{}"'.format(val))
    return data
        

def get_emails(self, result_bytes):
     msgs = []
     for num in result_bytes[0].split():
        type , data = self.con.fetch(num , '(RFC822)')

def log_in(self):
    self.con.login(self.user_email_address , self.user_password)
    
def check_for_email(catagory , self):
    self.con.select(catagory)

con.login(user , password)



'''
