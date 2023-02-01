from kimlikkarti import KimlikKarti

class OgrenciKarti(KimlikKarti):
    def __init__(self, ad, soyad, yas, tckno, ogrno, bolum):
        KimlikKarti.__init__(self, ad, soyad, yas, tckno)
        
        self.ogrno = ogrno
        self.bolum = bolum