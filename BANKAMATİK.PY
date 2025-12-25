hesaplar = [
    {"ad": "batuhan ayazlı", "HesapNo": "123456", "bakiye": 20000, "ekhesap": 500, "usarname": "batuhanayaz", "şifre": "1234"},
    {"ad": "semra çelik", "HesapNo": "789147", "bakiye": 20000, "ekhesap": 250, "usarname": "semracız", "şifre": "456789"}
]

def bakiyesorgula(hesap):
    print("\n Hesap Özeti ")
    print(f"Güncel Bakiye: {hesap['bakiye']} TL")
    print(f"Ek Hesap Limiti: {hesap['ekhesap']} TL")

def paraçekme(hesap):
    miktar = float(input("Çekmek istediğiniz miktar: "))
    
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print(f"Paranızı alabilirsiniz. Yeni bakiyeniz: {hesap['bakiye']} TL")
    else:
        toplam = hesap["bakiye"] + hesap["ekhesap"] 
        if toplam >= miktar:
            ekhesap_onay = input(f"Bakiyeniz yetersiz. Ek hesap kullanılsın mı? (e/h): ")
            if ekhesap_onay.lower() == "e":
                ek_kullanilacak = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekhesap"] -= ek_kullanilacak
                print("Paranızı ek hesap kullanarak aldınız.")
            else:
                print("İşlem reddedildi.")
        else:
            print("Üzgünüz,limitiniz  yetersiz.")

def parayatırma(hesap):
    miktar = float(input("Yatırmak istediğiniz miktar: "))
    hesap["bakiye"] += miktar
    print(f"Yeni bakiyeniz: {hesap['bakiye']} TL")

def menu(hesap):
    while True: 
        print(f"\nHoş Geldiniz, Sayın {hesap['ad'].upper()}")
        print("1- Bakiye Sorgula\n2- Para Çek\n3- Para Yatır\n4- Çıkış")
        islem = input("Seçiminiz: ")
        
        if islem == "1": bakiyesorgula(hesap)
        elif islem == "2": paraçekme(hesap)
        elif islem == "3": parayatırma(hesap)
        elif islem == "4": 
            print("Ana menüye dönülüyor....")
            break
        else: 
            print("seçimin hatalı!")

def login():
    print("\n-- Giriş Yap --")
    u_name = input("Username: ")
    u_pass = input("Parola: ")
    
    for hesap in hesaplar:
        if hesap["usarname"] == u_name and hesap["şifre"] == u_pass:
            menu(hesap)
            return 
    
    print("Hatalı kullanıcı adı veya şifre!")

def kayit_ol():
    print("\n--- Yeni Hesap Oluştur ---")
    ad = input("Adınız Soyadınız: ")
    hesap_no = input("Hesap Numarası: ")
    username = input("Kullanıcı Adı belirleyin: ")
    sifre = input("Şifre belirleyin: ")
    

    yeni_hesap = {
        "ad": ad,
        "HesapNo": hesap_no,
        "bakiye": 0,
        "ekhesap": 500, 
        "usarname": username,
        "şifre": sifre
    }
    
    hesaplar.append(yeni_hesap)
    print("Hesabınız başarıyla oluşturuldu! Şimdi giriş yapabilirsiniz.")


def ana_ekran():
    while True:
        print("\n BANKAMIZA HOŞ GELDİNİZ ")
        print("1- Giriş Yap")
        print("2- kayıt ol")
        print("3- uygulamadan çık ")
        secim = input("Seçimin: ")

        if secim == "1":
            login()
        elif secim == "2":
            kayit_ol()
        elif secim == "3":
            print("İyi günler")
            break
        else:
            print("Geçersiz işlem.")


ana_ekran()
