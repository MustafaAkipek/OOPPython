class KimlikKarti:
    
    def __init__(self, ad, soyad, yas, tckno):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.tckno = tckno
        
    def __str__(self):
        return f"Ad: {self.ad}"
    
    def yazdir(self):
        return f"{self.ad}"