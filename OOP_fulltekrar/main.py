from bilmüh import BilMüh
from kimlikkarti import KimlikKarti
from ogrencikarti import OgrenciKarti
from klupkarti import KlupKarti

ogrenci1 = BilMüh("Mustafa", "Akipek", 20217170000, "OOP")
ogrenci2 = BilMüh("Yaren", "Akpinar", 20217170001, "OOP")


ogrenci1.ders_yazdir = "Mat"
print(ogrenci1.ders_yazdir)


print(ogrenci1.tum_bilgiler())

print(BilMüh.ogrenci_sayi_yazdir())

print(ogrenci1.tum_bilgiler())


print(ogrenci1 + ogrenci2)

print(ogrenci1)


kimlikkarti1 = KimlikKarti("Mustafa", "Akipek", 19, 39139139391)

ogrenciKarti1 = OgrenciKarti("Mustafa", "Akipek", 19, 39139139391, 20217170000, "BilMüh")

klupkarti1 = KlupKarti("Mustafa", "Akipek", 19, 39139139391, 20217170000, "Bilmüh", "versebyte")

print(klupkarti1)

del ogrenci1.ders_yazdir

print(ogrenci1.ders_yazdir)