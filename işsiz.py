"""İşsiz sınıfı için (Issiz.py) statüsü (“mavi yaka, beyaz yaka, yönetici”) olan ve bu statülere ait geçmiş tecrübelerinin (yıl değeri) tutulduğu bir dictionary private değişkeni bulunmalıdır.
• Değişkene göre Initializer metot olmalıdır.
• Tüm gerekli değişkenler için get/set metotları tanımlanmalıdır.
• En uygun statünün bulunması için statu_bul metodu yazınız (Dictionaryde girilen değerlere göre; yıl değerinde mavi yakanın etkisi %20, beyaz yakanın etkisi %35, yöneticinin etkisi %45 olarak hesaplayınız ve en yüksek çıkan değere ait statüyü ilgili değişkeninize atayınız. Bu değişkene farklı bir class’tan erişim sağlanabilmelidir.)
• İlgili yerlerde try/except kullanılmalıdır.
• __str__ metotu içinde kullanıcının ad, soyadı ve dictionary ile hesaplanan kişiye en uygun statü (public değişken ile yazdırılmamalı) yazdırılmalıdır."""
import insan #insan sınıfını import ettik

class Issiz(insan.Insan): #issiz sınıfı insan sınıfından kalıtım
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,geçmiş_tecrübe): #yapıcı metot
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk) #kalıtım aldığımız sınıfın yapıcı metotu
        self.__gecmis_tecrube= geçmiş_tecrübe   #gecmis tecrube private değişkeni
        self.__statu=str() #statu private değişkeni
        self.statu_bul()

    def get_gecmis_tecrube(self): #gecmis tecrube almak için get metodu
        return self.__gecmis_tecrube
    def set_gecmis_tecrube(self,gecmis_tecrube): #gecmis tecrube yapmak için set metodu
        self.__gecmis_tecrube=gecmis_tecrube
    def statu_bul(self): #statu bulmak için metot
        mavi_yaka=self.__gecmis_tecrube[0]*0.2 #mavi yaka etkisi
        beyaz_yaka=self.__gecmis_tecrube[1]*0.35 #beyaz yaka etkisi
        yonetici=self.__gecmis_tecrube[2]*0.45 #yonetici etkisi
        if mavi_yaka>beyaz_yaka and mavi_yaka>yonetici: #mavi yaka en büyükse
            self.__statu="mavi yaka" #statu mavi yaka
        elif beyaz_yaka>mavi_yaka and beyaz_yaka>yonetici: #beyaz yaka en büyükse
            self.__statu="beyaz yaka" #statu beyaz yaka
        elif yonetici>mavi_yaka and yonetici>beyaz_yaka: #yonetici en büyükse
            self.__statu="yonetici" #statu yonetici
        else: #eşitse
            self.__statu="yönetici" #statu yönetici
    def __str__(self): #str metodu ile issiz sınıfı için bilgileri yazdırma işlemi
        return f"ad: {self.get_ad()} soyad: {self.get_soyad()} statu: {self.__statu}"
