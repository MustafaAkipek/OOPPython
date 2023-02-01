from abc import ABCMeta, abstractmethod


class Sms(metaclass=ABCMeta):
 #kesinlikle eklememiz gereken methodlara abstract dekoratörünü ekliyoruz
    @abstractmethod
    def create_token(self): pass
    
    @abstractmethod
    def phone(self): pass
    
    @abstractmethod
    def message(self): pass
    
    @abstractmethod
    def send(self): pass
    
    