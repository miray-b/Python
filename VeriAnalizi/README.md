# 📊 Öğrenci Not Analizi (Student Grade Analysis)

Bu proje, Python öğrenme sürecimde temel veri analizi yeteneklerini pekiştirmek için geliştirdiğim bir scripttir. Listeler, döngüler ve sözlükler (dictionaries) kullanılarak ham veriden anlamlı bilgiler çıkarma süreci simüle edilmiştir.

## 🎯 Projenin Amacı
Bir öğrenci grubuna ait notları analiz ederek sınıf ortalamasını hesaplamak, en başarılı öğrenciyi bulmak ve her öğrencinin geçme/kalma durumunu raporlamak.

## 🚀 Özellikler
* **Veri Toplulaştırma (Aggregation):** Sınıf ortalamasını ($\bar{x}$) hesaplar ve en yüksek notu bulur. (Eğitim amaçlı olarak hazır `max()` fonksiyonu yerine algoritma mantığı manuel olarak kurulmuştur).
* **Veri Filtreleme:** Dersi geçen öğrencileri (Not $\ge$ 50) filtreleyerek ayrı bir liste oluşturur.
* **Mantıksal Dönüşüm:** Her öğrenci için puana dayalı olarak "GEÇTİ" veya "KALDI" durumunu belirler.
* **Yapılandırılmış Veri:** Öğrenci isimleri ve notlarını eşleştirmek için Python **Sözlükleri (Dictionaries)** kullanılır.

## 🛠️ Kullanılan Teknolojiler
* **Dil:** Python 3
* **Veri Yapıları:** Listeler (`[]`), Sözlükler (`{}`)
* **Temel Kavramlar:** `for` Döngüleri, `if-else` Koşulları, Veri Eşleme (Mapping)

## 💻 Kodun İşleyişi
1.  **Liste Analizi:** Ham notlar üzerinde gezinerek istatistiksel verileri (toplam, ortalama) çıkarır.
2.  **Filtreleme:** Belirli bir koşulu sağlayan verileri ayıklar.
3.  **Sözlük Analizi:** `.items()` metodu ile isim-puan eşleşmelerini döngüye sokar ve detaylı bir durum raporu yazdırır.

## 🏃 Nasıl Çalıştırılır?
1.  Bilgisayarınızda Python 3'ün yüklü olduğundan emin olun.
2.  Proje klasörüne terminalden giriş yapın.
3.  Aşağıdaki komutu çalıştırın:

```bash
python veri_analizi.py
```
Developed by MBS