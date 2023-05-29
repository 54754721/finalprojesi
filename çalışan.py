"""Çalışan sınıfı için (Calisan.py) sektör (kullanıcının “teknoloji, muhasebe, inşaat, diğer” seçenekleri girmesi sağlanmalı ve doğru girdiği kontrol edilmelidir), tecrübe (ay değeri) ve maaş değişkenleri private olarak tanımlanmalıdır.
• Değişkenlere göre Initializer metot olmalıdır.
• Tüm gerekli değişkenler için get/set metotları tanımlanmalıdır.
• Çalışanın zam hakkını hesaplayan zam_hakki metodu yazılacaktır (2 sene öncesi tecrübesi olanın zam oranı önerisi 0’dır. 2-4 sene arası çalışan ise ve maaş 15000TL altıysa “maaş%tecrübe” sonucu zam oranı önerilecektir. 4 seneden fazla tecrübe varsa ve maaş 25000 altıysa “(maaş%tecrübe)/2” zam oranı önerilecektir). Yeni maaş, eski maaş ile aynıysa eski maaş, yeni maaşa atanmalıdır.
• İlgili yerlerde try/except kullanılmalıdır.
• __str__ metotunda ad, soyad, tecrübe ve yeni maaşı (public değişken ile yazdırılmamalı) yazılmalıdır."""
import insan #insan sınıfını import etme  

class Calisan(insan.Insan): #calisan sınıfı insan sınıfından kalıtım
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,sektor,tecrube,maas): #yapıcı metot
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk) #kalıtım aldığımız sınıfın yapıcı metotu
        self.__sektor=sektor #sektor private değişkeni
        self.__tecrube=tecrube #tecrube private değişkeni
        self.__maas=maas #maas private değişkeni
        self.__yeni_maas = self.__maas + self.zam_hakki() * self.__maas #yeni maas private değişkeni

    def get_sektor(self): #sektor almak için get metodu
        return self.__sektor
    def set_sektor(self,sektor): #sektor yapmak için set metodu
        self.__sektor=sektor

    def get_tecrube(self): #tecrube almak için get metodu
        return self.__tecrube
    def set_tecrube(self,tecrube): #tecrube yapmak için set metodu
        self.__tecrube=tecrube

    def get_maas(self): #maas almak için get metodu
        return self.__maas
    def set_maas(self,maas): #maas yapmak için set metodu
        self.__maas=maas

    def get_yeni_maas(self): #yeni maas almak için get metodu
        return self.__yeni_maas
    def set_yeni_maas(self,yeni_maas): #yeni maas yapmak için set metodu
        self.__yeni_maas=yeni_maas

    def zam_hakki(self): #zam hakki metodu
        zam=0 #zam değişkeni
        if self.__tecrube<24: #tecrube 24 den küçükse
            zam=0 #zam 0
        elif self.__tecrube>=24 and self.__tecrube<48 and self.__maas<15000: #tecrube 24 ile 48 arasında ve maas 15000 den küçükse
            zam=(self.__maas%self.__tecrube)/100 #zam maas*tecrube/100
        elif self.__tecrube>=48 and self.__maas>25000: #tecrube 48 den büyük ve maas 25000 den büyükse
            zam=((self.__maas%self.__tecrube)/100)/2 #zam (maas*tecrube/100)/2
        else: #eşitse
            zam=0 #zam 0
        return zam #yeni maas maas+zam

    def __str__(self): #str metodu ile calisan sınıfı için bilgileri yazdırma işlemi
        return f"ad: {self.get_ad()} soyad: {self.get_soyad()} tecrube: {self.__tecrube} yeni maas: {self.__yeni_maas}"
