from kimlikkarti import KimlikKarti
from ogrencikarti import OgrenciKarti

class KlupKarti(OgrenciKarti, KimlikKarti):
    def __init__(self, ad, soyad, yas, tckno, ogrno, bolum, klupadi):
        OgrenciKarti.__init__(self, ad, soyad, yas, tckno, ogrno, bolum)
        KimlikKarti.__init__(self, ad, soyad, yas, tckno)
        self.klupadi = klupadi
        
    def __str__(self):
        return self.soyad
        