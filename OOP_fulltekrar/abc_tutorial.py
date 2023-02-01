from abc_tutorial_base import Sms

class XCompany(Sms):
    def phone(self):
        print("Telefon girildi")
        
    def message(self):
        print("Mesaj girildi")
        
    def send(self):
        print("Sns gönderildi")
    
    def create_token(self):
        print("crate token gönderildi")
        
x = XCompany()