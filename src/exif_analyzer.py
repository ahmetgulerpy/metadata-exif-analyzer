"""
Metadata EXIF Analyzer

Professional implementation of an EXIF metadata analyzer.

This version uses command-line arguments and a cleaner project structure
while preserving the same logic demonstrated in the educational example.
"""

from pathlib import Path
import argparse

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def koordinatlari_ondaliga_cevir(deger, referans):
    """GPS koordinatlarını ondalık derece formatına dönüştürür."""
    derece = float(deger[0])
    dakika = float(deger[1])
    saniye = float(deger[2])

    ondalik = derece + (dakika / 60) + (saniye / 3600)

    if referans in ("S", "W"):
        ondalik *= -1

    return ondalik


def metadata_oku(dosya_yolu: Path) -> None:
    """Belirtilen görselin EXIF metadata bilgilerini analiz eder."""

    print(f"\n🔍 Analiz Edilen Dosya: {dosya_yolu.name}")

    try:
        with Image.open(dosya_yolu) as resim:
            exif_verisi = resim.getexif()

        if not exif_verisi:
            print("❌ EXIF metadata bulunamadı.")
            return

        metadata_havuzu = {}
        gps_verisi = {}

        for etiket_id, deger in exif_verisi.items():
            etiket_adi = TAGS.get(etiket_id, etiket_id)

            if etiket_adi == "GPSInfo":
                for gps_id, gps_deger in deger.items():
                    gps_etiket = GPSTAGS.get(gps_id, gps_id)
                    gps_verisi[gps_etiket] = gps_deger
            else:
                metadata_havuzu[etiket_adi] = deger

        cihaz_marka = metadata_havuzu.get("Make", "Unknown")
        cihaz_model = metadata_havuzu.get("Model", "Unknown")
        cekim_tarihi = metadata_havuzu.get("DateTime", "Unknown")

        print("=" * 50)
        print("📱 EXIF METADATA ANALYSIS")
        print("=" * 50)

        print(f"📸 Manufacturer : {cihaz_marka}")
        print(f"📱 Model        : {cihaz_model}")
        print(f"📅 Capture Date : {cekim_tarihi}")

        if gps_verisi:
            enlem = gps_verisi.get("GPSLatitude")
            enlem_ref = gps_verisi.get("GPSLatitudeRef")

            boylam = gps_verisi.get("GPSLongitude")
            boylam_ref = gps_verisi.get("GPSLongitudeRef")

            if enlem and boylam:
                latitude = koordinatlari_ondaliga_cevir(
                    enlem,
                    enlem_ref,
                )

                longitude = koordinatlari_ondaliga_cevir(
                    boylam,
                    boylam_ref,
                )

                print(f"\n📍 Latitude  : {latitude}")
                print(f"📍 Longitude : {longitude}")
                print(
                    f"🗺️ Google Maps : https://www.google.com/maps?q={latitude},{longitude}"
                )
        else:
            print("\n📍 GPS metadata bulunamadı.")

        print("=" * 50)

    except Exception as hata:
        print(f"❌ Hata: {hata}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract EXIF metadata from image files."
    )

    parser.add_argument(
        "image",
        help="Path to the image file",
    )

    args = parser.parse_args()

    dosya = Path(args.image)

    if not dosya.exists():
        print(f"❌ File not found: {dosya}")
        return

    metadata_oku(dosya)


if __name__ == "__main__":
    main()
