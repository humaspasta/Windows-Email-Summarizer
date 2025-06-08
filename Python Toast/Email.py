import imaplib , email



class Email:

    con = imaplib.IMAP4_SSL('imap.gmail.com')
    user_email_address = ''
    user_password = ''

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