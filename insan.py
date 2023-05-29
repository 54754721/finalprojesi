"""Çalışanların performans ölçümü ve zam almasına, çalışmayanların uygun statüye önerilmesine dayalı bir proje geliştirilecektir. Projede insan, çalışan, işsiz, mavi yaka, beyaz yaka sınıfları oluşturulacaktır. Sınıflar arasında kalıtım olmasına dikkat edilmelidir.
• Çalışan ve İşsiz sınıfları İnsan sınıfından kalıtım yoluyla üretilmelidir.
• Mavi yaka, beyaz yaka sınıfları Çalışan sınıfından kalıtım yoluyla üretilmelidir."""
"""İnsan sınıfında (Insan.py); tc_no, ad, soyad, yaş, cinsiyet, uyruk bilgileri private değişkenleri olarak bulunmalıdır.
• Değişkenlere göre Initializer metot olmalıdır.
• Tüm değişkenler için get/set metotları tanımlanmalıdır.
• __str__ metotu ile kullanıcı bilgileri yazdırılmalıdır."""

class Insan: #insan sınıfı
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk): #yapıcı metot
        self.__tc_no=tc_no #tc no private değişkeni
        self.__ad=ad #ad private değişkeni
        self.__soyad=soyad #soyad private değişkeni
        self.__yas=yas #yas private değişkeni
        self.__cinsiyet=cinsiyet #cinsiyet private değişkeni
        self.__uyruk=uyruk  #uyruk private değişkeni

    def get_tc_no(self): #tc no almak için get metodu
        return self.__tc_no
    def set_tc_no(self,tc_no): #tc no yapmak için set metodu
        self.__tc_no=tc_no

    def get_ad(self): #ad almak için get metodu
        return self.__ad
    def set_ad(self,ad): #ad yapmak için set metodu
        self.__ad=ad

    def get_soyad(self): #soyad almak için get metodu
        return self.__soyad
    def set_soyad(self,soyad): #soyad yapmak için set metodu
        self.__soyad=soyad

    def get_yas(self): #yas almak için get metodu
        return self.__yas
    def set_yas(self,yas): #yas yapmak için set metodu
        self.__yas=yas

    def get_cinsiyet(self): #cinsiyet almak için get metodu
        return self.__cinsiyet
    def set_cinsiyet(self,cinsiyet): #cinsiyet yapmak için set metodu
        self.__cinsiyet=cinsiyet

    def get_uyruk(self): #uyruk almak için get metodu
        return self.__uyruk
    def set_uyruk(self,uyruk): #uyruk yapmak için set metodu
        self.__uyruk=uyruk

    def __str__(self): #str metodu ile insan sınıfı için bilgileri yazdırma işlemi
        return f"tc: {self.__tc_no} ad:{self.__ad} soyad:{self.__soyad} yas:{self.__yas} cinsiyet:{self.__cinsiyet} uyruk:{self.__uyruk}"
