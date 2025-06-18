

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




# import os
# import requests
# import xml.etree.ElementTree as ET
# from deep_translator import GoogleTranslator
# from forex_python.converter import CurrencyRates
# import math

# # Files
# translated_file = "translatedsample_icgiyim.xml"
# original_file = "original.xml"

# # Load previously translated barcodes
# def extract_first_variant_barkod(urun):
#     urun_secenek = urun.find("UrunSecenek")
#     if urun_secenek is not None:
#         for secenek in urun_secenek.findall("Secenek"):
#             barkod = secenek.find("Barkod")
#             if barkod is not None and barkod.text and barkod.text.strip():
#                 return barkod.text.strip()
#     return None

# if os.path.exists(translated_file) and os.path.getsize(translated_file) > 0:
#     try:
#         old_tree = ET.parse(translated_file)
#         old_root = old_tree.getroot()
#         old_products = old_root.findall(".//Urun")
#         translated_barcodes = {
#             extract_first_variant_barkod(p) for p in old_products
#         }
#         translated_barcodes = {b for b in translated_barcodes if b}
#         print(f"Loaded {len(translated_barcodes)} previously translated products.")
#     except ET.ParseError:
#         print("Warning: Translated file corrupted or invalid. Starting fresh.")
#         translated_barcodes = set()
# else:
#     translated_barcodes = set()
#     print("No previously translated file found or it's empty.")

# # Step 1: Download XML
# url = "https://gecelikmagazasi.com/TicimaxXml/CB0C2D2195694477A0657C567D29C8AF"
# response = requests.get(url)
# print("XML downloaded successfully.")

# with open(original_file, "wb") as f:
#     f.write(response.content)

# tree = ET.parse(original_file)
# root = tree.getroot()
# print("XML parsed successfully.")

# # Step 2: Set up translator and exchange rate
# translator = GoogleTranslator(source='auto', target='en')
# currency = CurrencyRates()
# try:
#     rate = currency.get_rate('TRY', 'USD')
# except Exception as e:
#     print(f"Currency API failed. Using fallback rate. Error: {e}")
#     rate = 0.031
# print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# # Step 3: Process products
# translated_root = ET.Element(root.tag)
# products = root.findall(".//Urun")
# print(f"Found {len(products)} products. Translating only new ones...")

# def safe_translate(element):
#     if element is not None and element.text:
#         try:
#             element.text = translator.translate(element.text)
#         except Exception as e:
#             print(f"Translation failed: {e}")

# def convert_price(el):
#     if el is not None and el.text:
#         try:
#             val = float(el.text.replace(",", "."))
#             el.text = f"{math.ceil(val * rate * 100) / 100:.2f}"
#         except Exception as e:
#             print(f"Price conversion failed: {e}")

# translated_count = 0

# for i, product in enumerate(products, start=1):
#     barkod = extract_first_variant_barkod(product)
#     if not barkod or barkod in translated_barcodes:
#         continue

#     # Check if at least one variant has stock > 0
#     has_stock = False
#     urun_secenek = product.find("UrunSecenek")
#     if urun_secenek is not None:
#         for secenek in urun_secenek.findall("Secenek"):
#             stok_el = secenek.find("StokAdedi")
#             if stok_el is not None and stok_el.text and stok_el.text.isdigit() and int(stok_el.text) > 0:
#                 has_stock = True
#                 break
#     if not has_stock:
#         continue

#     print(f"Translating product {i} - Barkod: {barkod}")
#     safe_translate(product.find("UrunAdi"))
#     safe_translate(product.find("Aciklama"))
#     safe_translate(product.find("EksecenekOzellik"))
#     convert_price(product.find("Fiyat"))

#     if urun_secenek is not None:
#         for variant in urun_secenek.findall("Secenek"):
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

#             for tag in ["AlisFiyati", "SatisFiyati", "IndirimliFiyat"]:
#                 convert_price(variant.find(tag))

#     translated_root.append(product)
#     translated_barcodes.add(barkod)
#     translated_count += 1

# print(f"Translated {translated_count} new products.")

# # Step 4: Save to final output file
# translated_tree = ET.ElementTree(translated_root)
# translated_tree.write(translated_file, encoding="utf-8", xml_declaration=True)
# print(f"All translated products saved to {translated_file}.")





# import os
# import requests
# import xml.etree.ElementTree as ET
# from deep_translator import GoogleTranslator
# from forex_python.converter import CurrencyRates
# import math
# import copy

# # Config
# URL = "https://gecelikmagazasi.com/TicimaxXml/CB0C2D2195694477A0657C567D29C8AF"
# ORIGINAL_FILE = "original_icgiyim.xml"
# TRANSLATED_FILE = "translatedsample_icgiyim.xml"

# # Download XML
# response = requests.get(URL, timeout=60)
# response.raise_for_status()
# with open(ORIGINAL_FILE, "wb") as f:
#     f.write(response.content)
# print("Downloaded XML.")

# # Parse XML
# tree = ET.parse(ORIGINAL_FILE)
# root = tree.getroot()
# products = root.find("Urunler").findall("Urun")
# print(f"Found {len(products)} products.")

# # Load existing translated output
# if os.path.exists(TRANSLATED_FILE) and os.path.getsize(TRANSLATED_FILE) > 0:
#     try:
#         old_root = ET.parse(TRANSLATED_FILE).getroot()
#         old_by_id = {p.findtext("UrunKartiID"): p for p in old_root.findall("Urun")}
#         print(f"Loaded {len(old_by_id)} previously translated.")
#     except ET.ParseError:
#         old_by_id = {}
#         print("Warning: Corrupted old XML. Ignoring.")
# else:
#     old_by_id = {}
#     print("No existing translated file.")

# translator = GoogleTranslator(source="auto", target="en")
# try:
#     rate = CurrencyRates().get_rate("TRY", "USD")
# except Exception:
#     rate = 0.031
# print(f"Using exchange rate: {rate:.4f}")

# final_products = []

# for prod in products:
#     pid = prod.findtext("UrunKartiID")
#     if not pid:
#         continue

#     stok = sum(int(s.findtext("StokAdedi") or 0) for s in prod.findall(".//Secenek"))
#     if stok == 0:
#         continue

#     if pid in old_by_id:
#         final_products.append(old_by_id[pid])
#         continue

#     # New product → translate & convert
#     print(f"Translating new product {pid}")
#     cp = copy.deepcopy(prod)

#     for tag in ["UrunAdi", "Kategori", "KategoriTree", "Marka"]:
#         el = cp.find(tag)
#         if el is not None and el.text:
#             el.text = translator.translate(el.text)

#     price_el = cp.find(".//SatisFiyati")
#     if price_el is not None and price_el.text:
#         try:
#             tr = float(price_el.text.replace(",", "."))
#             price_el.text = f"{math.ceil(tr * rate * 100)/100:.2f}"
#         except:
#             pass

#     final_products.append(cp)

# # Clean up old products not present or zero stock
# valid_ids = {p.findtext("UrunKartiID") for p in products}
# final_products = [
#     p for p in final_products
#     if p.findtext("UrunKartiID") in valid_ids and sum(int(s.findtext("StokAdedi") or 0) for s in p.findall(".//Secenek")) > 0
# ]

# # Write updated XML
# root_new = ET.Element("Root")
# uv = ET.SubElement(root_new, "Urunler")
# for p in final_products:
#     uv.append(p)

# ET.ElementTree(root_new).write(
#     TRANSLATED_FILE,
#     encoding="utf-8",
#     xml_declaration=True,
#     method="xml",
#     short_empty_elements=True
# )
# print(f"Translated {len(final_products)} products to {TRANSLATED_FILE}.")






import requests
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
import os
import time

# Constants
XML_URL = "https://www.gecelikmagazasi.com/XMLYukle"
RAW_XML_PATH = "debug_raw_icgiyim.xml"
OUTPUT_XML_PATH = "translatedsample_icgiyim.xml"
TRANSLATOR = GoogleTranslator(source='tr', target='en')

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
    response = requests.get(XML_URL)
    response.encoding = 'utf-8'

    # Save raw content for debugging
    with open(RAW_XML_PATH, "w", encoding="utf-8") as f:
        f.write(response.text)

    # Check if response is valid XML
    if not response.ok:
        raise Exception(f"Failed to fetch XML. Status code: {response.status_code}")

    if not response.text.strip().startswith("<?xml"):
        preview = response.text[:300].strip()
        raise Exception(f"Response does not appear to be valid XML. Preview:\n{preview}")

    try:
        return ET.ElementTree(ET.fromstring(response.text))
    except ET.ParseError as e:
        with open("error_log_icgiyim.txt", "w", encoding="utf-8") as err_file:
            err_file.write(response.text)
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

        # Copy and add images as pictureUrls
        images = urun.find("Resimler")
        if images is not None:
            for resim in images.findall("Resim"):
                pic = ET.SubElement(urun_kopya, "pictureUrl")
                pic.text = resim.text

        # Process variations (Secenek)
        urunsecenek_tag = urun.find("UrunSecenek")
        if urunsecenek_tag is not None:
            secenek_group = ET.SubElement(urun_kopya, "UrunSecenek")

            for secenek in urunsecenek_tag.findall("Secenek"):
                barkod = secenek.findtext("Barkod", "").strip()
                stok_adedi = secenek.findtext("StokAdedi", "0")
                satis_fiyati = secenek.findtext("SatisFiyati", "0").replace(",", ".")

                # Update if new product or update stock
                is_new = barkod and barkod not in barcodes_out

                if is_new or True:  # Always update stock and price
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

        # Merge if new product
        if barkod and barkod not in barcodes_out:
            root_out.append(urun_kopya)
        else:
            # update existing stock in place
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





