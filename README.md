# First Django Project

Bu proje, Django framework'ünü öğrenirken oluşturduğum, farklı uygulamaları ve temel web geliştirme kavramlarını içeren bir deneme projesidir. Kodlar ve yapı biraz karışık olabilir, çünkü öğrenme ve deneme amaçlı farklı örnekler bir arada kullanılmıştır.

## Proje Yapısı

- **firstdjango/**: Ana proje ayarları ve URL yönlendirmeleri.
- **pages/**: Ana sayfa, kurslar ve iletişim gibi temel sayfalar.
- **kurslar/**: Kurslarla ilgili örnek uygulama.
- **iletisim/**: İletişim sayfası ve ilgili fonksiyonlar.
- **templates/**: Ortak şablonlar ve sayfa görünümleri.
- **static/**: Statik dosyalar (CSS, JS, görseller).

## Kurulum

1. **Python ve Django Kurulumu**

   ```bash
   pip install django
   ```

2. **Projeyi Çalıştırma**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   Ardından tarayıcınızda `http://127.0.0.1:8000/` adresine giderek projeyi görebilirsiniz.

## Temel Özellikler

- **Ana Sayfa:** Basit bir karşılama sayfası.
- **Kurslar:** Kategorilere göre filtrelenebilen kurs listesi (örnek veri ile).
- **İletişim:** Basit iletişim sayfası ve örnek fonksiyonlar.
- **Admin Paneli:** Django'nun standart admin paneli ile yönetim.

## Örnek URL'ler

- `/` : Ana sayfa
- `/kurslar` : Kurslar sayfası
- `/iletisim` : İletişim sayfası
- `/admin/` : Yönetici paneli

## Notlar

- Projede veritabanı olarak varsayılan `sqlite3` kullanılmıştır.
- Bazı sayfalarda örnek veri ve fonksiyonlar yer almaktadır.
- Kodlar ve şablonlar öğrenme amaçlı olduğu için karmaşık ve düzensiz olabilir.

## Katkı ve Geliştirme

Bu proje tamamen öğrenme ve deneme amaçlıdır. Dilerseniz kendi denemelerinizi ekleyebilir veya yapıyı sadeleştirebilirsiniz.
