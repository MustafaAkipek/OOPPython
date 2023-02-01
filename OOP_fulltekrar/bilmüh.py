class BilMüh:                                                                           #Sınıf
    ogrenci_sayisi:int = 0                                                              #Class variable
    
    def __init__(self, ad:str, soyad:str, no:int, ders:str = "OOP"):                    #Constructor
        self.ad = ad                                                                    #İnstance variable
        self.soyad = soyad                                                              #İnstance variable
        self.no = no                                                                    #İnstance variable
        self.__ders = ders                                                              #Encapsule edilmiş İnstance variable
        BilMüh.ogrenci_sayisi += 1                  
        
    def tum_bilgiler(self):                                                             #İnstance Method
        """ Kişinin bilgilerini döndürür """
        return f"Ogrenci Adi: {self.ad}\nOgrenci Soyadi: {self.soyad}\nOgrenci No: {self.no}\nOgrenci Ders: {self.__ders}"
    
    @property                                                                           #property getter
    def ders_yazdir(self):
        """ ders_yazdir.getter """
        return self.__ders
    
    @ders_yazdir.setter                                                                 #property setter
    def ders_yazdir(self, value:str):
        """ ders_yazdir.setter """
        self.__ders = value
    
    @ders_yazdir.deleter                                                                #property deletter
    def ders_yazdir(self):
        self.__ders = None
        
    
    @classmethod                                                                        #class method
    def ogrenci_sayi_yazdir(cls):
        """ Ogrenci sayısını öğrenmek için kullanırız """
        return f"Ogrenci Sayisi: {cls.ogrenci_sayisi}"
    
    @staticmethod
    def sehir_yazdir(sehir:str):
        """ Sehir ismini döndürür"""                                                    #static method
        return sehir
    
    def __add__(self, other):                                                           #dunder methods
        return  self.ad + other.ad
    
    def __repr__(self):                                                                 #dunder methods
        return f"Ad: {self.ad} Soyad: {self.soyad}"
    
    