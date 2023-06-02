"""Mavi yaka sınıfı için (MaviYaka.py) yıpranma payı (float: 0.2, 0.5 gibi değer almalıdır) değişkeni private olarak bulunmalıdır.
• Değişkenlere göre Initializer metot olmalıdır.
• Tüm gerekli değişkenler için get/set metotları tanımlanmalıdır.
• Çalışanın zam hakkını hesaplayan zam_hakki metodu yazılacaktır (2 sene öncesi tecrübesi olanın zam oranı önerisi “yıpranma_payi*10” olacaktır. 2-4 sene arası çalışan ise ve maaş 15000TL altıysa “(maaş%tecrübe)/2 + (yıpranma_payi*10)” sonucu zam oranı önerilecektir. 4 seneden fazla tecrübe varsa ve maaş 25000 altıysa “(maaş%tecrübe)/3+ (yıpranma_payi*10)” zam oranı önerilecektir). Yeni maaş, eski maaş ile aynıysa eski maaş, yeni maaşa atanmalıdır.
• İlgili yerlerde try/except kullanılmalıdır.
• __str__ metotunda ad, soyad, tecrübe ve yeni maaşı (public değişken ile yazdırılmamalı) yazılmalıdır."""
import çalışan #çalışan sınıfını import etme

class MaviYaka(çalışan.Calisan): #mavi yaka sınıfı calisan sınıfından kalıtım
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,sektor,tecrube,maas,yipranma_payi): #yapıcı metot
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk,sektor,tecrube,maas) #kalıtım aldığımız sınıfın yapıcı metotu
        self.__yipranma_payi=yipranma_payi #yipranma payi private değişkeni

    def get_yipranma_payi(self): #yipranma payi almak için get metodu
        return self.__yipranma_payi
    def set_yipranma_payi(self,yipranma_payi): #yipranma payi yapmak için set metodu
        self.__yipranma_payi=yipranma_payi

    def zam_hakki(self): #zam hakki metodu
        zam=0 #zam değişkeni
        if self.get_tecrube()<24: #tecrube 24 den küçükse
            zam=self.__yipranma_payi*10 #zam yipranma payi*10
        elif self.get_tecrube()>=24 and self.get_tecrube()<48 and self.get_maas()<15000: #tecrube 24 ile 48 arasında ve maas 15000 den küçükse
            zam=(self.get_maas()*self.__tecrube/100)/2 + (self.__yipranma_payi*10) #zam (maas*tecrube/100)/2 + (yipranma payi*10)
        elif self.get_tecrube()>=48 and self.get_maas()>25000: #tecrube 48 den büyük ve maas 25000 den büyükse
            zam=(self.get_maas()*self.get_tecrube()/100)/3 + (self.__yipranma_payi*10) #zam (maas*tecrube/100)/3 + (yipranma payi*10)
        else: #eş
            zam=0 #zam 0
        return zam #yeni maas maas+zam
