# Dolu klasör silmek için
# !rm -rf folder_name/

# Gerekli paketleri yükle
!pip install -q gdown

import zipfile
import os
import shutil

user_input = input("Dosyaları temizlemek istiyorsanız 1 giriniz: ")

if user_input == "1":
    content_dir = '/content'

    for item in os.listdir(content_dir):
        item_path = os.path.join(content_dir, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            print(f"Hata oluştu: {item_path} silinemedi. Sebep: {e}")

    print("✅ /content dizini temizlendi.")
else:
    print("❌ Temizleme işlemi yapılmadan devam ediliyor.")

# Eğer /content/Data yoksa, zip indir ve çıkar
if not os.path.exists('/content/Data'):
    print("Data klasörü bulunamadı. ZIP dosyası indiriliyor ve çıkarılıyor...")

    # Google Drive'dan zip indir
    !gdown 1xaW6YmmTY98pYraSI1VIVYz0Oa4AxBHn --output file.zip

    # ZIP çıkar
    with zipfile.ZipFile('file.zip', 'r') as zip_ref:
        zip_ref.extractall('/content')

    print("ZIP dosyası başarıyla çıkarıldı.")
    os.remove('file.zip')
else:
    print("Data klasörü zaten mevcut. ZIP indirme işlemi atlandı.")

# GitHub reposunu klonla
!git clone https://github.com/Ahmet-MahirDEMIRELLI/bitirme_ml.git

# bitirme_ml içeriğini /content altına taşı
src_path = '/content/bitirme_ml'
dst_path = '/content'

# Her dosya ve klasörü taşı
for item in os.listdir(src_path):
    s = os.path.join(src_path, item)
    d = os.path.join(dst_path, item)
    if os.path.isdir(s):
        shutil.move(s, d)
    else:
        shutil.move(s, d)

# Eski klasörü sil
shutil.rmtree(src_path)
print("bitirme_ml içeriği /content altına taşındı ve klasör silindi.")

print("✅ İşlemler tamamlandı.")
