# Bir öğrencinin Matematik notları (Veri Setimiz)
notlar = [75, 90, 50, 85, 100, 60]

print(f"Tüm Notlar: {notlar}")

# İndeksleme: Python'da saymaya 0'dan başlanır!
print(f"İlk Sınav: {notlar[0]}")  # 1. eleman
print(f"Son Sınav: {notlar[-1]}") # Sondan 1. eleman

print("\n--- Notlar Listeleniyor ---")

# 'notlar' listesindeki her bir 'puan' için dön:
for puan in notlar:
    print(f"İncelenen Not: {puan}")
    
print("Döngü bitti.")

print("\n--- Analiz Başlıyor ---")

toplam = 0  # Başlangıçta toplam 0'dır (Etkisiz eleman)

for puan in notlar:
    toplam = toplam + puan  # Her notu sepete ekle (Akümülasyon)
    # print(f"Ara toplam: {toplam}") # Bu satırı açarsan adım adım görürsün

eleman_sayisi = len(notlar) # n sayısı
ortalama = toplam / eleman_sayisi

print(f"Sınıf Mevcudu: {eleman_sayisi}")
print(f"Notların Toplamı: {toplam}")
print(f"Ortalama: {ortalama}")

###max kullanmadan max değer bulma
en_buyuk= 0
for puan in notlar:

    if  puan > en_buyuk:
        en_buyuk= puan
print(f"Sınıfın En Yüksek Notu: {en_buyuk}")

print("\n--- Dersten Geçenler Filtreleniyor ---")

gecenler = [] # 1. Adım: Boş küme (Sepet)

for puan in notlar:
    if puan >= 50:
        # 2. Adım: Şartı sağlayanları sepete at
        gecenler.append(puan) 

print(f"Geçen Notlar: {gecenler}")
print(f"Geçen Öğrenci Sayısı: {len(gecenler)}")

print("\n--- 10 Puan Bonus Ekleniyor ---")

yeni_notlar = [] # Dönüştürülmüş küme (Görüntü Kümesi)

for x in notlar:
    # Her elemana fonksiyonu uygula: f(x) = x + 10
    yeni_puan = x + 10
    
    # Not 100'ü geçemez kuralı (Min-Max Normalizasyonu)
    if yeni_puan > 100:
        yeni_puan = 100
        
    yeni_notlar.append(yeni_puan)

print(f"Eski Notlar: {notlar}")
print(f"Yeni Notlar: {yeni_notlar}")

print("\n--- Sınıf Defteri (Dictionary) ---")

# İsim (Key) -> Not (Value) eşleşmesi
sinif = {
    "Ali": 75,
    "Ayşe": 90,
    "Mehmet": 60,
    "Zeynep": 100
}

print(sinif)

# Ayşe'nin notu kaç? (f("Ayşe") = ?)
print(f"Ayşe'nin Notu: {sinif['Ayşe']}")

# Yeni öğrenci ekleme: f("Mert") = 45
sinif["Mert"] = 45
sinif["Miray"] = 100

# Not güncelleme: Ali itiraz etti, notu arttı.
sinif["Ali"] = 80

print(f"Güncel Sınıf: {sinif}")

print("\n--- Detaylı Sınıf Analizi ---")

# .items() komutu bize her turda iki bilgi verir: İsim ve Puan
for isim, puan in sinif.items():
    
    # Koşullu Durum (Piecewise Function)
    if puan >= 50:
        durum = "GEÇTİ ✅"
    else:
        durum = "KALDI ❌"
        
    print(f"{isim}: {puan} aldı -> Durumu: {durum}")