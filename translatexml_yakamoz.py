import os
import requests
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
from forex_python.converter import CurrencyRates
import math
import copy

# === File paths ===
translated_file = "translated_yalin.xml"
original_file = "original_yalin.xml"
source_url = "https://modayakamoz.com/xml/yalin1"

# === Download XML ===
response = requests.get(source_url)
with open(original_file, "wb") as f:
    f.write(response.content)
print("Downloaded XML from source.")

# === Parse XML ===
tree = ET.parse(original_file)
root = tree.getroot()
new_products = root.find("Urunler").findall("Urun")
print(f"Parsed {len(new_products)} products from XML.")

# === Load previous translations ===
if os.path.exists(translated_file) and os.path.getsize(translated_file) > 0:
    try:
        old_tree = ET.parse(translated_file)
        old_root = old_tree.getroot()
        old_products = {p.find("UrunKartiID").text: p for p in old_root.find("Urunler").findall("Urun")}
        print(f"Loaded {len(old_products)} previously translated products.")
    except ET.ParseError:
        print("Warning: Failed to parse old file.")
        old_products = {}
else:
    old_products = {}

# === Set up translation and currency ===
translator = GoogleTranslator(source='auto', target='en')
currency = CurrencyRates()
try:
    rate = currency.get_rate('TRY', 'USD')
except:
    rate = 0.031
print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# === Helpers ===
def total_stock(urun):
    total = 0
    for secenek in urun.findall(".//Secenek"):
        stok = secenek.find("StokAdedi")
        if stok is not None and stok.text.isdigit():
            total += int(stok.text)
    return total

def translate_field(el):
    if el is not None and el.text:
        try:
            el.text = translator.translate(el.text)
        except Exception as e:
            print(f"Translation failed: {e}")

def convert_price(el):
    if el is not None and el.text:
        try:
            price = float(el.text.replace(",", "."))
            el.text = f"{math.ceil(price * rate * 100) / 100:.2f}"
        except Exception as e:
            print(f"Price conversion failed: {e}")

# === Process products ===
final_products = {}

for urun in new_products:
    pid_el = urun.find("UrunKartiID")
    if pid_el is None or not pid_el.text:
        continue
    pid = pid_el.text.strip()

    stock = total_stock(urun)
    if stock == 0:
        continue

    if pid in old_products:
        final_products[pid] = old_products[pid]
        continue

    print(f"Translating product ID: {pid}")
    translated = copy.deepcopy(urun)

    # Translate top-level product info
    for tag in ["UrunAdi", "OnYazi", "Aciklama", "Marka", "Cinsiyet", "Üretici",
                "YıkamaTalimatı", "MateryalBileseni", "Kategori", "KategoriTree",
                "SeoSayfaBaslik", "SeoAnahtarKelime", "SeoAciklama"]:
        translate_field(translated.find(tag))

    # Translate variants
    for secenek in translated.findall(".//Secenek"):
        convert_price(secenek.find("SatisFiyati"))
        convert_price(secenek.find("IndirimliFiyat"))
        for ozellik in secenek.findall(".//Ozellik"):
            translate_field(ozellik)
            if "Deger" in ozellik.attrib:
                try:
                    ozellik.attrib["Deger"] = translator.translate(ozellik.attrib["Deger"])
                except:
                    pass

    final_products[pid] = translated

# === Write output XML ===
if final_products:
    out_root = ET.Element("Root")
    urunler = ET.SubElement(out_root, "Urunler")
    for p in final_products.values():
        urunler.append(p)

    ET.ElementTree(out_root).write(translated_file, encoding="utf-8", xml_declaration=True, short_empty_elements=True)
    print(f"Saved {len(final_products)} products to {translated_file}.")
else:
    print("No products to save.")
