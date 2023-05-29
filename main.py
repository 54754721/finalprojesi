    """Main.py için;
• İlgili yerlerde try/except kullanılmalıdır.
• Sadece insan sınıfı için 2 nesne üretilmelidir ve bilgiler __str__ metotu aracılığıyla yazdırılmalıdır.
• İşsiz sınıfı için 3 nesne üretilmelidir ve __str__ metotu ile ilgili bilgiler ekrana yazdırılmalıdır.
• Çalışan sınıfı için 3 nesne üretilmelidir ve __str__ metotu ile ilgili bilgiler ekrana yazdırılmalıdır.
• Mavi yaka sınıfı için 3 nesne üretilmelidir ve __str__ metotu ile ilgili bilgiler ekrana yazdırılmalıdır.
• Beyaz yaka sınıfı için 3 nesne üretilmelidir ve __str__ metotu ile ilgili bilgiler ekrana yazdırılmalıdır.
• Çalışan, mavi yaka ve beyaz yaka nesnelerinin tüm değerlerinden (“çalışan, mavi yaka, beyaz yaka” nesne değeri ,tc_no, ad, soyad, yas, cinsiyet, uyruk, sektör, tecrübe (kaydederken yıla çeviriniz), maaş, yıpranma payı, teşvik primi, yeni maaş) bir pandas DataFrame oluşturunuz (excel, csv veya dictionary ile). Oluşturduğunuz DataFrame ile şu işlemleri gerçekleştiriniz:
a) Bazı değişken değerleri diğer nesneler için boş olabilir, DataFrame için bu değerleri 0 atayınız.
b) Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş ortalamalarını her grup için hesaplayınız ve yazdırınız.
c) Maaşı 15000TL üzerinde olanların toplam sayısını bulunuz.
d) Yeni maaşa göre DataFrame’i küçükten büyüğe sıralayınız ve yazdırınız.
e) Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulunuz ve yazdırınız.
f) Yeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanları, tc_no ve yeni_maaş sütunlarını seçerek gösteriniz ve yazdırınız.
g) Var olan DataFrame’den ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame elde ediniz ve yazdırınız."""
import insan, işsiz, çalışan, maviyakalı, beyazyakalı #sınıflar
import pandas as pd #pandas kütüphanesi
def main():
    insan1=insan.Insan(11111111111,"ali","veli",20,"erkek","tr") #insan sınıfı için 1. nesne
    insan2=insan.Insan(22222222222,"ayse","fatma",30,"kadin","tr") #insan sınıfı için 2. nesne
    print(insan1) #insan1 nesnesi için __str__ metodu
    print(insan2) #insan2 nesnesi için __str__ metodu
    print("-"*50) #50 tane -
    issiz1=işsiz.Issiz(33333333333,"mehmet","ali",25,"erkek","tr",[2,5,5]) #issiz sınıfı için 1. nesne
    issiz2=işsiz.Issiz(44444444444,"ali","veli",30,"erkek","tr",[10,12,0]) #issiz sınıfı için 2. nesne
    issiz3=işsiz.Issiz(55555555555,"ayse","fatma",35,"kadin","tr",[5,10,2]) #issiz sınıfı için 3. nesne
    print(issiz1) #issiz1 nesnesi için __str__ metodu
    print(issiz2) #issiz2 nesnesi için __str__ metodu
    print(issiz3) #issiz3 nesnesi için __str__ metodu
    print("-"*50) #50 tane -
    calisan1=çalışan.Calisan(66666666666,"mehmet","ali",40,"erkek","tr","yazilim",20,10000) #calisan sınıfı için 1. nesne
    calisan2=çalışan.Calisan(77777777777,"ali","veli",45,"erkek","tr","yazilim",25,12000) #calisan sınıfı için 2. nesne
    calisan3=çalışan.Calisan(88888888888,"ayse","fatma",50,"kadin","tr","yazilim",30,14000) #calisan sınıfı için 3. nesne
    print(calisan1) #calisan1 nesnesi için __str__ metodu
    print(calisan2) #calisan2 nesnesi için __str__ metodu
    print(calisan3) #calisan3 nesnesi için __str__ metodu
    print("-"*50) #50 tane -
    maviyaka1=maviyakalı.MaviYaka(99999999999,"mehmet","ali",55,"erkek","tr","yazilim",35,26000,0.2) #maviyaka sınıfı için 1. nesne
    maviyaka2=maviyakalı.MaviYaka(10101010101,"ali","veli",60,"erkek","tr","yazilim",40,30000,0.25) #maviyaka sınıfı için 2. nesne
    maviyaka3=maviyakalı.MaviYaka(12121212121,"ayse","fatma",65,"kadin","tr","yazilim",45,35000,0.5) #maviyaka sınıfı için 3. nesne
    print(maviyaka1) #maviyaka1 nesnesi için __str__ metodu
    print(maviyaka2) #maviyaka2 nesnesi için __str__ metodu
    print(maviyaka3) #maviyaka3 nesnesi için __str__ metodu
    print("-"*50) #50 tane -
    beyazyaka1=beyazyakalı.BeyazYaka(13131313131,"mehmet","ali",70,"erkek","tr","yazilim",50,24000,250) #beyazyaka sınıfı için 1. nesne
    beyazyaka2=beyazyakalı.BeyazYaka(14141414141,"ali","veli",75,"erkek","tr","yazilim",55,26000,500) #beyazyaka sınıfı için 2. nesne
    beyazyaka3=beyazyakalı.BeyazYaka(15151515151,"ayse","fatma",80,"kadin","tr","yazilim",60,35000,2500) #beyazyaka sınıfı için 3. nesne
    print(beyazyaka1) #beyazyaka1 nesnesi için __str__ metodu
    print(beyazyaka2) #beyazyaka2 nesnesi için __str__ metodu
    print(beyazyaka3) #beyazyaka3 nesnesi için __str__ metodu
    print("-"*50) #50 tane -
    neseneler = ["Çalışan", "Çalışan", "Çalışan", "MaviYaka", "MaviYaka", "MaviYaka", "BeyazYaka", "BeyazYaka", "BeyazYaka"]
    tcler = [calisan1.get_tc_no(),calisan2.get_tc_no(),calisan3.get_tc_no(),maviyaka1.get_tc_no(),maviyaka2.get_tc_no(),maviyaka3.get_tc_no(),beyazyaka1.get_tc_no(),beyazyaka2.get_tc_no(),beyazyaka3.get_tc_no()]
    adlar = [calisan1.get_ad(),calisan2.get_ad(),calisan3.get_ad(),maviyaka1.get_ad(),maviyaka2.get_ad(),maviyaka3.get_ad(),beyazyaka1.get_ad(),beyazyaka2.get_ad(),beyazyaka3.get_ad()]
    soyadlar = [calisan1.get_soyad(),calisan2.get_soyad(),calisan3.get_soyad(),maviyaka1.get_soyad(),maviyaka2.get_soyad(),maviyaka3.get_soyad(),beyazyaka1.get_soyad(),beyazyaka2.get_soyad(),beyazyaka3.get_soyad()]
    yaslar = [calisan1.get_yas(),calisan2.get_yas(),calisan3.get_yas(),maviyaka1.get_yas(),maviyaka2.get_yas(),maviyaka3.get_yas(),beyazyaka1.get_yas(),beyazyaka2.get_yas(),beyazyaka3.get_yas()]
    cinsiyetler = [calisan1.get_cinsiyet(),calisan2.get_cinsiyet(),calisan3.get_cinsiyet(),maviyaka1.get_cinsiyet(),maviyaka2.get_cinsiyet(),maviyaka3.get_cinsiyet(),beyazyaka1.get_cinsiyet(),beyazyaka2.get_cinsiyet(),beyazyaka3.get_cinsiyet()]
    uyruklar = [calisan1.get_uyruk(),calisan2.get_uyruk(),calisan3.get_uyruk(),maviyaka1.get_uyruk(),maviyaka2.get_uyruk(),maviyaka3.get_uyruk(),beyazyaka1.get_uyruk(),beyazyaka2.get_uyruk(),beyazyaka3.get_uyruk()]
    sektorler = [calisan1.get_sektor(),calisan2.get_sektor(),calisan3.get_sektor(),maviyaka1.get_sektor(),maviyaka2.get_sektor(),maviyaka3.get_sektor(),beyazyaka1.get_sektor(),beyazyaka2.get_sektor(),beyazyaka3.get_sektor()]
    tecrubeler = [calisan1.get_tecrube(),calisan2.get_tecrube(),calisan3.get_tecrube(),maviyaka1.get_tecrube(),maviyaka2.get_tecrube(),maviyaka3.get_tecrube(),beyazyaka1.get_tecrube(),beyazyaka2.get_tecrube(),beyazyaka3.get_tecrube()]
    maaslar = [calisan1.get_maas(),calisan2.get_maas(),calisan3.get_maas(),maviyaka1.get_maas(),maviyaka2.get_maas(),maviyaka3.get_maas(),beyazyaka1.get_maas(),beyazyaka2.get_maas(),beyazyaka3.get_maas()]
    yıpranmalar = [0, 0, 0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(), maviyaka3.get_yipranma_payi(), 0, 0, 0]
    primler = [0, 0, 0, 0, 0, 0, beyazyaka1.get_prim(), beyazyaka2.get_prim(), beyazyaka3.get_prim()]
    yenimaaslar = [calisan1.get_yeni_maas(),calisan2.get_yeni_maas(),calisan3.get_yeni_maas(),maviyaka1.get_yeni_maas(),maviyaka2.get_yeni_maas(),maviyaka3.get_yeni_maas(),beyazyaka1.get_yeni_maas(),beyazyaka2.get_yeni_maas(),beyazyaka3.get_yeni_maas()]
    
    tablo = {"neseler":neseneler,"tcler":tcler,"adlar":adlar,"soyadlar":soyadlar,"yaslar":yaslar,"cinsiyetler":cinsiyetler,"uyruklar":uyruklar,"sektorler":sektorler,"tecrubeler":tecrubeler,"maaslar":maaslar,"yıpranmalar":yıpranmalar,"primler":primler,"yenimaaslar":yenimaaslar}
    df = pd.DataFrame(tablo) #tabloyu dataframe e çevirme
    print(df) #dataframe i yazdırma
    print("-"*50) #50 tane -
    """Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş ortalamalarını her grup için hesaplayınız ve yazdırınız."""
    print("Çalışanlar için tecrübe ortalaması: ",df[df["neseler"]=="Çalışan"]["tecrubeler"].mean())
    print("Çalışanlar için yeni maaş ortalaması: ",df[df["neseler"]=="Çalışan"]["yenimaaslar"].mean())
    print("Mavi yaka için tecrübe ortalaması: ",df[df["neseler"]=="MaviYaka"]["tecrubeler"].mean())
    print("Mavi yaka için yeni maaş ortalaması: ",df[df["neseler"]=="MaviYaka"]["yenimaaslar"].mean())
    print("Beyaz yaka için tecrübe ortalaması: ",df[df["neseler"]=="BeyazYaka"]["tecrubeler"].mean())
    print("Beyaz yaka için yeni maaş ortalaması: ",df[df["neseler"]=="BeyazYaka"]["yenimaaslar"].mean())
    print("-"*50) #50 tane -
    #Maaşı 15000TL üzerinde olanların toplam sayısını bulunuz.
    print("Maaşı 15000TL üzerinde olanların toplam sayısı: ",len(df[df["maaslar"]>15000]))
    print("-"*50) #50 tane -
    #Yeni maaşa göre DataFrame’i küçükten büyüğe sıralayınız ve yazdırınız.
    print(df.sort_values(by="yenimaaslar"))
    print("-"*50) #50 tane -
    #Yeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanları, tc_no ve yeni_maaş sütunlarını seçerek gösteriniz ve yazdırınız.
    print(df[df["yenimaaslar"]>10000][2:5][["tcler","yenimaaslar"]])
    print("-"*50) #50 tane -
    #Var olan DataFrame’den ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame elde ediniz ve yazdırınız.
    print(df[["adlar","soyadlar","sektorler","yenimaaslar"]])
    print("-"*50) #50 tane -

if __name__ == "__main__":
    main()

    