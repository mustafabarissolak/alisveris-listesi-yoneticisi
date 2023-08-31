# 1. Gereksinimlerin Belirlenmesi:
# Kullanıcının alışveriş listesine ürün ekleyebilmesi.
# Alışveriş listesindeki ürünleri görüntüleyebilmesi.
# Alışveriş listesinden ürün silebilmesi.
# Programı istediği zaman sonlandırabilmesi.

# 2. Program Akışının Tasarlanması:
# Kullanıcıya menü seçenekleri gösterilecek.
# Kullanıcının seçimine göre ilgili işlem yapılacak.
# Kullanıcı "çıkış" seçeneğini seçene kadar işlemler tekrar edecek.

# 3. Kodlama Adımları:
# Gerekli modülleri içe aktarın.
# Boş bir alışveriş listesi oluşturun.
# Bir döngü içinde kullanıcıdan sürekli olarak seçeneklerini alın ve ilgili işlemi gerçekleştirin.

import sys

alisveris_listesi = []

while True:
    print("Alışveriş Listesi Yöneticisi")
    print("1. Ürün Ekle")
    print("2. Listeyi Göster")
    print("3. Ürün Sil")
    print("4. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == "1":
        urun = input("Eklemek istediğiniz ürünü girin: ")
        alisveris_listesi.append(urun)
        print(f"{urun} alışveriş listesine eklendi.")

    elif secim == "2":
        print("Alışveriş Listesi:")
        for index, urun in enumerate(alisveris_listesi, start=1):
            print(f"{index}. {urun}")

    elif secim == "3":
        if not alisveris_listesi:
            print("Alışveriş listesi boş.")

        else:
            print("Alışveriş Listesi:")

            for index, urun in enumerate(alisveris_listesi, start=1):
                print(f"{index}. {urun}")
            sil_index = int(
                input("Silmek istediğiniz ürünün numarasını girin: ")) - 1

            if 0 <= sil_index < len(alisveris_listesi):
                silinen_urun = alisveris_listesi.pop(sil_index)
                print(f"{silinen_urun} alışveriş listesinden silindi.")

            else:
                print("Geçersiz bir numara girdiniz.")
    elif secim == "4":
        print("Program kapatılıyor...")
        sys.exit()
    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

