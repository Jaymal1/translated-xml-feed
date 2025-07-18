


import requests
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
import os
import time

# Constants
XML_URL = "https://gecelikmagazasi.com/TicimaxXml/CB0C2D2195694477A0657C567D29C8AF"
RAW_XML_PATH = "debug_raw_icgiyim.xml"
OUTPUT_XML_PATH = "translatedsample_icgiyim.xml"
TRANSLATOR = GoogleTranslator(source='tr', target='en')

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_exchange_rate():
    try:
        response = requests.get("https://api.exchangerate.host/latest?base=TRY&symbols=USD")
        data = response.json()
        return float(data["rates"]["USD"])
    except Exception as e:
        print("Exchange rate fetch failed:", e)
        return 0.032  # fallback

def translate_text(text):
    try:
        return TRANSLATOR.translate(text.strip())
    except Exception:
        return text

def save_raw_xml():
    response = requests.get(XML_URL, headers=HEADERS)
    response.encoding = 'utf-8'

    if not response.ok:
        raise Exception(f"Failed to fetch XML. Status code: {response.status_code}")

    # Save raw for debugging
    with open(RAW_XML_PATH, "w", encoding="utf-8") as f:
        f.write(response.text)

    # Clean BOM and validate XML
    content = response.text.lstrip('\ufeff').strip()
    if not content.startswith("<?xml"):
        preview = content[:300]
        raise Exception(f"Response does not appear to be valid XML. Preview:\n{preview}")

    try:
        return ET.ElementTree(ET.fromstring(content))
    except ET.ParseError as e:
        with open("error_log_icgiyim.txt", "w", encoding="utf-8") as err_file:
            err_file.write(content)
        raise Exception(f"Failed to parse XML: {e}")

def load_existing_output():
    if not os.path.exists(OUTPUT_XML_PATH):
        root = ET.Element("Root")
        return ET.ElementTree(root)
    return ET.parse(OUTPUT_XML_PATH)

def get_existing_barcodes(tree):
    return {opt.find("Barkod").text for opt in tree.findall(".//Secenek") if opt.find("Barkod") is not None and opt.find("Barkod").text}

def process_products(raw_tree, output_tree, rate):
    root_out = output_tree.getroot()
    barcodes_out = get_existing_barcodes(output_tree)

    for urun in raw_tree.findall(".//Urun"):
        urun_kopya = ET.Element("Urun")
        barkod = None  # initialize outside loop

        # Translate product name
        name = urun.findtext("UrunAdi", "")
        ET.SubElement(urun_kopya, "UrunAdi").text = translate_text(name)

        # Copy and translate Aciklama
        aciklama_tag = urun.find("Aciklama")
        if aciklama_tag is not None:
            translated = translate_text(aciklama_tag.text or "")
            ET.SubElement(urun_kopya, "Aciklama").text = translated

        # Copy basic fields
        fields_to_copy = ["UrunKartiID", "Marka", "Kategori", "KategoriTree", "UrunUrl"]
        for field in fields_to_copy:
            ET.SubElement(urun_kopya, field).text = urun.findtext(field, "")

        # Copy and add images
        images = urun.find("Resimler")
        if images is not None:
            for resim in images.findall("Resim"):
                pic = ET.SubElement(urun_kopya, "pictureUrl")
                pic.text = resim.text

        # Process variations
        urunsecenek_tag = urun.find("UrunSecenek")
        if urunsecenek_tag is not None:
            secenek_group = ET.SubElement(urun_kopya, "UrunSecenek")

            for secenek in urunsecenek_tag.findall("Secenek"):
                barkod = secenek.findtext("Barkod", "").strip()
                stok_adedi = secenek.findtext("StokAdedi", "0")
                satis_fiyati = secenek.findtext("SatisFiyati", "0").replace(",", ".")

                is_new = barkod and barkod not in barcodes_out

                if is_new or True:
                    secenek_out = ET.SubElement(secenek_group, "Secenek")
                    for child in ["VaryasyonID", "StokKodu", "Barkod"]:
                        ET.SubElement(secenek_out, child).text = secenek.findtext(child, "")

                    ET.SubElement(secenek_out, "StokAdedi").text = stok_adedi
                    try:
                        price_usd = round(float(satis_fiyati) * rate, 2)
                    except:
                        price_usd = 0.0
                    ET.SubElement(secenek_out, "PriceUSD").text = str(price_usd)

                    # Translate EkSecenekOzellik > Ozellik
                    ek = secenek.find("EkSecenekOzellik")
                    if ek is not None:
                        translated_ek = ET.SubElement(secenek_out, "EkSecenekOzellik")
                        for ozellik in ek.findall("Ozellik"):
                            new_ozellik = ET.SubElement(translated_ek, "Ozellik")
                            for k, v in ozellik.attrib.items():
                                new_ozellik.set(k, translate_text(v))
                            new_ozellik.text = translate_text(ozellik.text or "")

        if barkod and barkod not in barcodes_out:
            root_out.append(urun_kopya)
        else:
            for existing_sec in root_out.findall(".//Secenek"):
                if existing_sec.findtext("Barkod", "") == barkod:
                    existing_sec.find("StokAdedi").text = stok_adedi
                    existing_sec.find("PriceUSD").text = str(price_usd)

def main():
    print("Starting script for icgiyim...")
    raw_tree = save_raw_xml()
    output_tree = load_existing_output()
    rate = fetch_exchange_rate()
    process_products(raw_tree, output_tree, rate)
    output_tree.write(OUTPUT_XML_PATH, encoding="utf-8", xml_declaration=True)
    print("Translation and sync complete. Output saved to:", OUTPUT_XML_PATH)

if __name__ == "__main__":
    main()





