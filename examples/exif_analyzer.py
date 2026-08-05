"""
Metadata EXIF Analyzer (Educational Example)

This example demonstrates how to extract basic EXIF metadata
from an image using Python and Pillow.

This version is the same concept demonstrated in my Instagram tutorials
and is intentionally kept beginner-friendly.
"""

import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def koordinatlari_ondaliga_cevir(deger, referans):
    """GPS verilerini Google Maps'in anlayacağı koordinat formatına çevirir."""
    derece = float(deger[0])
    dakika = float(deger[1])
    saniye = float(deger[2])
    
    ondalik = derece + (dakika / 60.0) + (saniye / 3600.0)
    if referans in ['S', 'W']:
        ondalik = -ondalik
    return ondalik

def metadata_oku(dosya_yolu):
    print(f"\n🔍 {dosya_yolu} inceleniyor...")
    
    try:
        resim = Image.open(dosya_yolu)
        # Fotoğrafın EXIF (Metadata) verilerini alıyoruz
        exif_verisi = resim._getexif()
        
        if not exif_verisi:
            print("❌ Bu fotoğrafta gizli metadata izi bulunamadı (Temizlenmiş olabilir).")
            return

        metadata_havuzu = {}
        gps_verisi = {}

        # EXIF verilerini okunabilir etiketlere dönüştür
        for etiket_id, deger in exif_verisi.items():
            etiket_adi = TAGS.get(etiket_id, etiket_id)
            if etiket_adi == "GPSInfo":
                # GPS verilerini ayrı bir sözlükte toplayalım
                for gps_id in deger:
                    gps_etiket = GPSTAGS.get(gps_id, gps_id)
                    gps_verisi[gps_etiket] = deger[gps_id]
            else:
                metadata_havuzu[etiket_adi] = deger

        # --- TELEFON VE TARİH BİLGİLERİ ---
        cihaz_marka = metadata_havuzu.get("Make", "Bilinmiyor")
        cihaz_model = metadata_havuzu.get("Model", "Bilinmiyor")
        cekim_tarihi = metadata_havuzu.get("DateTime", "Bilinmiyor")

        print("=============================================")
        print("📱 DİJİTAL İZ ANALİZİ BAŞARILI!")
        print("=============================================")
        print(f"📸 Cihaz Markası: {cihaz_marka}")
        print(f"📱 Telefon Modeli: {cihaz_model}")
        print(f"📅 Çekim Tarihi/Saati: {cekim_tarihi}")

        # --- KONUM (GPS) BİLGİLERİ ---
        if gps_verisi:
            enlem_ref = gps_verisi.get("GPSLatitudeRef")
            enlem_verisi = gps_verisi.get("GPSLatitude")
            boylam_ref = gps_verisi.get("GPSLongitudeRef")
            boylam_verisi = gps_verisi.get("GPSLongitude")

            if enlem_verisi and boylam_verisi:
                enlem = koordinatlari_ondaliga_cevir(enlem_verisi, enlem_ref)
                boylam = koordinatlari_ondaliga_cevir(boylam_verisi, boylam_ref)
                
                print(f"📍 GPS Koordinatları: {enlem}, {boylam}")
                print(f"🔗 Google Maps Linki: https://www.google.com/maps?q={enlem},{boylam}")
        else:
            print("📍 GPS Konumu: Fotoğrafta konum izi bulunamadı (Konum servisleri kapalıyken çekilmiş).")
        print("=============================================")

    except Exception as e:
        print(f"❌ Hata: Dosya okunurken bir sorun oluştu: {e}")

# KODU TEST ETMEK İÇİN:
# Klasöründeki test fotoğrafının adını buraya yaz (Örn: "test.jpg")
resim_adi = "IMG_20260714_042120.jpg" 

if os.path.exists(resim_adi):
    metadata_oku(resim_adi)
else:
    print(f"⚠️ Test etmek için klasöre '{resim_adi}' adında bir fotoğraf ekleyin!")
