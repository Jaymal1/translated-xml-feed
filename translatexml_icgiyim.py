

# import os
# import requests
# import xml.etree.ElementTree as ET
# from deep_translator import GoogleTranslator
# from forex_python.converter import CurrencyRates
# import math

# # Display current directory
# print(f"Current working directory: {os.getcwd()}")

# # Step 1: Download XML
# url = "https://gecelikmagazasi.com/TicimaxXml/CB0C2D2195694477A0657C567D29C8AF"
# response = requests.get(url)
# print("XML downloaded successfully.")

# with open("original.xml", "wb") as f:
#     f.write(response.content)

# tree = ET.parse("original.xml")
# root = tree.getroot()
# print("XML parsed successfully.")

# # Step 2: Set up translator and exchange rate
# translator = GoogleTranslator(source='auto', target='en')
# currency = CurrencyRates()
# try:
#     rate = currency.get_rate('TRY', 'USD')
# except Exception as e:
#     print(f"Currency API failed. Using fallback rate. Error: {e}")
#     rate = 0.031  # fallback rate
# print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# # Step 3: Process first 20 products only
# translated_root = ET.Element(root.tag)
# products = root.findall(".//Urun")
# print(f"Found {len(products)} products. Translating first 20...")

# for i, product in enumerate(products[:10], start=1):
#     print(f"Translating product {i}...")

#     # Translate name
#     name = product.find("UrunAdi")
#     if name is not None and name.text:
#         name.text = translator.translate(name.text)

#     # Translate description
#     description = product.find("Aciklama")
#     if description is not None and description.text:
#         description.text = translator.translate(description.text)

#     # Translate EksecenekOzellik (if present at product level)
#     secenek = product.find("EksecenekOzellik")
#     if secenek is not None and secenek.text:
#         secenek.text = translator.translate(secenek.text)

#     # Convert product price
#     price = product.find("Fiyat")
#     if price is not None and price.text:
#         try:
#             lira_value = float(price.text.replace(",", "."))
#             usd_value = math.ceil(lira_value * rate * 100) / 100.0
#             price.text = f"{usd_value:.2f}"
#         except Exception as e:
#             print(f"Could not convert price: {price.text}, error: {e}")

#     # Process variants
#     urun_secenek = product.find("UrunSecenek")
#     if urun_secenek is not None:
#         for variant in urun_secenek.findall("Secenek"):
#             # Translate EkSecenekOzellik
#             eksecenek = variant.find("EkSecenekOzellik")
#             if eksecenek is not None:
#                 for attr in eksecenek.findall("Ozellik"):
#                     if attr.text:
#                         try:
#                             translated = translator.translate(attr.text)
#                             attr.text = translated
#                         except Exception as e:
#                             print(f"Text translation error: {e}")
#                     if "Deger" in attr.attrib:
#                         try:
#                             translated_val = translator.translate(attr.attrib["Deger"])
#                             attr.attrib["Deger"] = translated_val
#                         except Exception as e:
#                             print(f"Deger translation error: {e}")
#                     if "Tanim" in attr.attrib:
#                         try:
#                             translated_val = translator.translate(attr.attrib["Tanim"])
#                             attr.attrib["Tanim"] = translated_val
#                         except Exception as e:
#                             print(f"Tanim translation error: {e}")
                    
            

#             # Convert prices in variant
#             for tag in ["AlisFiyati", "SatisFiyati", "IndirimliFiyat"]:
#                 p = variant.find(tag)
#                 if p is not None and p.text:
#                     try:
#                         p_val = float(p.text.replace(",", "."))
#                         p.text = f"{math.ceil(p_val * rate * 100) / 100.0:.2f}"
#                     except Exception as e:
#                         print(f"{tag} conversion failed: {p.text}, {e}")

#     # Append translated product to new root
#     translated_root.append(product)

# # Step 4: Save the translated subset
# translated_tree = ET.ElementTree(translated_root)
# translated_tree.write("translated_sample.xml", encoding="utf-8", xml_declaration=True)
# print("Translated 20 products saved to translated_sample.xml.")






# import os
# import requests
# import xml.etree.ElementTree as ET
# from deep_translator import GoogleTranslator
# from forex_python.converter import CurrencyRates
# import math

# # Display current directory
# print(f"Current working directory: {os.getcwd()}")

# # Step 1: Download XML
# url = "https://gecelikmagazasi.com/TicimaxXml/CB0C2D2195694477A0657C567D29C8AF"
# response = requests.get(url)
# print("XML downloaded successfully.")

# with open("original.xml", "wb") as f:
#     f.write(response.content)

# tree = ET.parse("original.xml")
# root = tree.getroot()
# print("XML parsed successfully.")

# # Step 2: Set up translator and exchange rate
# translator = GoogleTranslator(source='auto', target='en')
# currency = CurrencyRates()
# try:
#     rate = currency.get_rate('TRY', 'USD')
# except Exception as e:
#     print(f"Currency API failed. Using fallback rate. Error: {e}")
#     rate = 0.031  # fallback rate
# print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# # Step 3: Process all products
# translated_root = ET.Element(root.tag)
# products = root.findall(".//Urun")
# print(f"Found {len(products)} products. Translating all...")

# for i, product in enumerate(products, start=1):
#     print(f"Translating product {i}...")

#     # Translate name
#     name = product.find("UrunAdi")
#     if name is not None and name.text:
#         name.text = translator.translate(name.text)

#     # Translate description
#     description = product.find("Aciklama")
#     if description is not None and description.text:
#         description.text = translator.translate(description.text)

#     # Translate EksecenekOzellik (if present at product level)
#     secenek = product.find("EksecenekOzellik")
#     if secenek is not None and secenek.text:
#         secenek.text = translator.translate(secenek.text)

#     # Convert product price
#     price = product.find("Fiyat")
#     if price is not None and price.text:
#         try:
#             lira_value = float(price.text.replace(",", "."))
#             usd_value = math.ceil(lira_value * rate * 100) / 100.0
#             price.text = f"{usd_value:.2f}"
#         except Exception as e:
#             print(f"Could not convert price: {price.text}, error: {e}")

#     # Process variants
#     urun_secenek = product.find("UrunSecenek")
#     if urun_secenek is not None:
#         for variant in urun_secenek.findall("Secenek"):
#             # Translate EkSecenekOzellik
#             eksecenek = variant.find("EkSecenekOzellik")
#             if eksecenek is not None:
#                 for attr in eksecenek.findall("Ozellik"):
#                     if attr.text:
#                         try:
#                             attr.text = translator.translate(attr.text)
#                         except Exception as e:
#                             print(f"Text translation error: {e}")
#                     if "Deger" in attr.attrib:
#                         try:
#                             attr.attrib["Deger"] = translator.translate(attr.attrib["Deger"])
#                         except Exception as e:
#                             print(f"Deger translation error: {e}")
#                     if "Tanim" in attr.attrib:
#                         try:
#                             attr.attrib["Tanim"] = translator.translate(attr.attrib["Tanim"])
#                         except Exception as e:
#                             print(f"Tanim translation error: {e}")

#             # Convert prices in variant
#             for tag in ["AlisFiyati", "SatisFiyati", "IndirimliFiyat"]:
#                 p = variant.find(tag)
#                 if p is not None and p.text:
#                     try:
#                         p_val = float(p.text.replace(",", "."))
#                         p.text = f"{math.ceil(p_val * rate * 100) / 100.0:.2f}"
#                     except Exception as e:
#                         print(f"{tag} conversion failed: {p.text}, {e}")

#     # Append translated product to new root
#     translated_root.append(product)

# # Step 4: Save to final output file
# translated_tree = ET.ElementTree(translated_root)
# translated_tree.write("translatedsample_icgiyim.xml", encoding="utf-8", xml_declaration=True)
# print("All translated products saved to translatedsample_icgiyim.xml.")




import os
import requests
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
from forex_python.converter import CurrencyRates
import math

# Files
translated_file = "translatedsample_icgiyim.xml"
original_file = "original.xml"

# Load previously translated barcodes
def extract_first_variant_barkod(urun):
    urun_secenek = urun.find("UrunSecenek")
    if urun_secenek is not None:
        for secenek in urun_secenek.findall("Secenek"):
            barkod = secenek.find("Barkod")
            if barkod is not None and barkod.text and barkod.text.strip():
                return barkod.text.strip()
    return None

if os.path.exists(translated_file) and os.path.getsize(translated_file) > 0:
    try:
        old_tree = ET.parse(translated_file)
        old_root = old_tree.getroot()
        old_products = old_root.findall(".//Urun")
        translated_barcodes = {
            extract_first_variant_barkod(p) for p in old_products
        }
        translated_barcodes = {b for b in translated_barcodes if b}
        print(f"Loaded {len(translated_barcodes)} previously translated products.")
    except ET.ParseError:
        print("Warning: Translated file corrupted or invalid. Starting fresh.")
        translated_barcodes = set()
else:
    translated_barcodes = set()
    print("No previously translated file found or it's empty.")

# Step 1: Download XML
url = "https://gecelikmagazasi.com/TicimaxXml/CB0C2D2195694477A0657C567D29C8AF"
response = requests.get(url)
print("XML downloaded successfully.")

with open(original_file, "wb") as f:
    f.write(response.content)

tree = ET.parse(original_file)
root = tree.getroot()
print("XML parsed successfully.")

# Step 2: Set up translator and exchange rate
translator = GoogleTranslator(source='auto', target='en')
currency = CurrencyRates()
try:
    rate = currency.get_rate('TRY', 'USD')
except Exception as e:
    print(f"Currency API failed. Using fallback rate. Error: {e}")
    rate = 0.031
print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# Step 3: Process products
translated_root = ET.Element(root.tag)
products = root.findall(".//Urun")
print(f"Found {len(products)} products. Translating only new ones...")

def safe_translate(element):
    if element is not None and element.text:
        try:
            element.text = translator.translate(element.text)
        except Exception as e:
            print(f"Translation failed: {e}")

def convert_price(el):
    if el is not None and el.text:
        try:
            val = float(el.text.replace(",", "."))
            el.text = f"{math.ceil(val * rate * 100) / 100:.2f}"
        except Exception as e:
            print(f"Price conversion failed: {e}")

translated_count = 0

for i, product in enumerate(products, start=1):
    barkod = extract_first_variant_barkod(product)
    if not barkod or barkod in translated_barcodes:
        continue

    # Check if at least one variant has stock > 0
    has_stock = False
    urun_secenek = product.find("UrunSecenek")
    if urun_secenek is not None:
        for secenek in urun_secenek.findall("Secenek"):
            stok_el = secenek.find("StokAdedi")
            if stok_el is not None and stok_el.text and stok_el.text.isdigit() and int(stok_el.text) > 0:
                has_stock = True
                break
    if not has_stock:
        continue

    print(f"Translating product {i} - Barkod: {barkod}")
    safe_translate(product.find("UrunAdi"))
    safe_translate(product.find("Aciklama"))
    safe_translate(product.find("EksecenekOzellik"))
    convert_price(product.find("Fiyat"))

    if urun_secenek is not None:
        for variant in urun_secenek.findall("Secenek"):
            eksecenek = variant.find("EkSecenekOzellik")
            if eksecenek is not None:
                for attr in eksecenek.findall("Ozellik"):
                    if attr.text:
                        try:
                            attr.text = translator.translate(attr.text)
                        except Exception as e:
                            print(f"Text translation error: {e}")
                    if "Deger" in attr.attrib:
                        try:
                            attr.attrib["Deger"] = translator.translate(attr.attrib["Deger"])
                        except Exception as e:
                            print(f"Deger translation error: {e}")
                    if "Tanim" in attr.attrib:
                        try:
                            attr.attrib["Tanim"] = translator.translate(attr.attrib["Tanim"])
                        except Exception as e:
                            print(f"Tanim translation error: {e}")

            for tag in ["AlisFiyati", "SatisFiyati", "IndirimliFiyat"]:
                convert_price(variant.find(tag))

    translated_root.append(product)
    translated_barcodes.add(barkod)
    translated_count += 1

print(f"Translated {translated_count} new products.")

# Step 4: Save to final output file
translated_tree = ET.ElementTree(translated_root)
translated_tree.write(translated_file, encoding="utf-8", xml_declaration=True)
print(f"All translated products saved to {translated_file}.")
