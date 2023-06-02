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
