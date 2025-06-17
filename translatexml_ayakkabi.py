# import os
# import requests
# import xml.etree.ElementTree as ET
# from deep_translator import GoogleTranslator
# from forex_python.converter import CurrencyRates
# import math
# import copy
# import xml.dom.minidom

# # Step 1: Download XML
# url = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
# response = requests.get(url)
# print("XML downloaded successfully.")

# with open("original_ayakkabi.xml", "wb") as f:
#     f.write(response.content)

# # Step 2: Parse XML
# tree = ET.parse("original_ayakkabi.xml")
# root = tree.getroot()
# print("XML parsed successfully.")

# # Step 3: Setup translator and currency converter
# translator = GoogleTranslator(source='auto', target='en')
# currency = CurrencyRates()
# try:
#     rate = currency.get_rate('TRY', 'USD')
# except Exception as e:
#     print(f"Currency API failed. Using fallback rate. Error: {e}")
#     rate = 0.031
# print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# # Step 4: Translate and convert first 20 products
# translated_root = ET.Element(root.tag)
# products = root.findall(".//Product")[:10]
# print(f"Found {len(products)} products. Translating all products...")

# for i, product in enumerate(products, start=1):
#     print(f"Translating product {i}...")

#     product_copy = copy.deepcopy(product)

#     # Translate ProductName
#     pname = product_copy.find("ProductName")
#     if pname is not None and pname.text:
#         try:
#             pname.text = translator.translate(pname.text)
#         except Exception as e:
#             print(f"ProductName translation error: {e}")

#     # Translate FullDescription (often contains HTML tags, translate carefully)
#     fdesc = product_copy.find("FullDescription")
#     if fdesc is not None and fdesc.text:
#         try:
#             # Optionally strip HTML tags for translation or translate raw text
#             fdesc.text = translator.translate(fdesc.text)
#         except Exception as e:
#             print(f"FullDescription translation error: {e}")

#     # Convert ProductPrice
#     price = product_copy.find("ProductPrice")
#     if price is not None and price.text:
#         try:
#             lira = float(price.text.replace(",", "."))
#             usd = math.ceil(lira * rate * 100) / 100.0
#             price.text = f"{usd:.2f}"
#         except Exception as e:
#             print(f"ProductPrice conversion error: {e}")

#     # Translate attributes in ProductCombinations
#     combinations = product_copy.find("ProductCombinations")
#     if combinations is not None:
#         for combination in combinations.findall("ProductCombination"):
#             # Convert VariantStockQuantity if needed (optional)

#             attributes = combination.find("ProductAttributes")
#             if attributes is not None:
#                 for attr in attributes.findall("ProductAttribute"):
#                     vname = attr.find("VariantName")
#                     vval = attr.find("VariantValue")
#                     if vname is not None and vname.text:
#                         try:
#                             vname.text = translator.translate(vname.text)
#                         except Exception as e:
#                             print(f"VariantName translation error: {e}")
#                     if vval is not None and vval.text:
#                         try:
#                             vval.text = translator.translate(vval.text)
#                         except Exception as e:
#                             print(f"VariantValue translation error: {e}")

#     translated_root.append(product_copy)

# # Step 5: Save pretty printed XML
# rough_string = ET.tostring(translated_root, encoding='utf-8')
# reparsed = xml.dom.minidom.parseString(rough_string)
# with open("translatedsample_ayakkabi.xml", "w", encoding="utf-8") as f:
#     f.write(reparsed.toprettyxml(indent="  "))

# print("Translated products saved to translatedsample_ayakkabi.xml")



# import os
# import requests
# import xml.etree.ElementTree as ET
# from deep_translator import GoogleTranslator
# from forex_python.converter import CurrencyRates
# import math
# import copy
# import xml.dom.minidom

# # Step 1: Download latest XML
# url = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
# response = requests.get(url)
# with open("original_ayakkabi.xml", "wb") as f:
#     f.write(response.content)
# print("Downloaded and saved original XML.")

# # Step 2: Parse XML
# tree = ET.parse("original_ayakkabi.xml")
# root = tree.getroot()

# # Step 3: Load previously translated products
# translated_file = "translatedsample_ayakkabi.xml"
# if os.path.exists(translated_file):
#     translated_tree = ET.parse(translated_file)
#     translated_root = translated_tree.getroot()
#     old_products = {p.find("ProductId").text: p for p in translated_root.findall(".//Product")}
# else:
#     translated_root = ET.Element(root.tag)
#     old_products = {}

# # Step 4: Setup translator and currency converter
# translator = GoogleTranslator(source='auto', target='en')
# currency = CurrencyRates()
# try:
#     rate = currency.get_rate('TRY', 'USD')
# except Exception as e:
#     print(f"Currency API failed. Using fallback rate. Error: {e}")
#     rate = 0.031
# print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# # Step 5: Translate and update product list
# new_products = root.findall(".//Product")
# final_products = {}

# for product in new_products:
#     product_id = product.find("ProductId").text.strip()

#     # Get total stock (sum of VariantStockQuantity)
#     total_stock = 0
#     for comb in product.findall(".//ProductCombination"):
#         stock_node = comb.find("VariantStockQuantity")
#         if stock_node is not None:
#             total_stock += int(stock_node.text or "0")

#     # Skip if stock is 0
#     if total_stock == 0:
#         continue

#     if product_id in old_products:
#         final_products[product_id] = old_products[product_id]
#         continue  # Already translated, no need to translate again

#     print(f"Translating new product ID: {product_id}")
#     product_copy = copy.deepcopy(product)

#     # Translate name
#     pname = product_copy.find("ProductName")
#     if pname is not None and pname.text:
#         try:
#             pname.text = translator.translate(pname.text)
#         except Exception as e:
#             print(f"ProductName translation error: {e}")

#     # Translate description
#     fdesc = product_copy.find("FullDescription")
#     if fdesc is not None and fdesc.text:
#         try:
#             fdesc.text = translator.translate(fdesc.text)
#         except Exception as e:
#             print(f"FullDescription translation error: {e}")

#     # Convert price
#     price = product_copy.find("ProductPrice")
#     if price is not None and price.text:
#         try:
#             lira = float(price.text.replace(",", "."))
#             usd = math.ceil(lira * rate * 100) / 100.0
#             price.text = f"{usd:.2f}"
#         except Exception as e:
#             print(f"ProductPrice conversion error: {e}")

#     # Translate variant attributes
#     combinations = product_copy.find("ProductCombinations")
#     if combinations is not None:
#         for combination in combinations.findall("ProductCombination"):
#             attributes = combination.find("ProductAttributes")
#             if attributes is not None:
#                 for attr in attributes.findall("ProductAttribute"):
#                     vname = attr.find("VariantName")
#                     vval = attr.find("VariantValue")
#                     if vname is not None and vname.text:
#                         try:
#                             vname.text = translator.translate(vname.text)
#                         except Exception as e:
#                             print(f"VariantName translation error: {e}")
#                     if vval is not None and vval.text:
#                         try:
#                             vval.text = translator.translate(vval.text)
#                         except Exception as e:
#                             print(f"VariantValue translation error: {e}")

#     final_products[product_id] = product_copy

# # Step 6: Remove zero-stock old products
# for pid in list(old_products.keys()):
#     if pid not in [p.find("ProductId").text for p in new_products]:
#         continue  # Product no longer exists
#     for p in new_products:
#         if p.find("ProductId").text == pid:
#             stock = sum(int(c.find("VariantStockQuantity").text or "0") for c in p.findall(".//ProductCombination"))
#             if stock == 0:
#                 print(f"Removing old product ID {pid} due to zero stock.")
#                 final_products.pop(pid, None)

# # Step 7: Write back to file
# translated_root = ET.Element(root.tag)
# for product in final_products.values():
#     translated_root.append(product)

# tree = ET.ElementTree(translated_root)
# tree.write(translated_file, encoding="utf-8", xml_declaration=True)
# print(f"Updated translations saved to {translated_file}")

#rough_string = ET.tostring(translated_root, encoding='utf-8')
#reparsed = xml.dom.minidom.parseString(rough_string)
#with open(translated_file, "w", encoding="utf-8") as f:
    #f.write(reparsed.toprettyxml(indent="  "))

#print(f"Updated translations saved to {translated_file}")










# import os
# import requests
# import xml.etree.ElementTree as ET
# from deep_translator import GoogleTranslator
# from forex_python.converter import CurrencyRates
# import math
# import copy

# # Step 1: Download latest XML
# url = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
# response = requests.get(url)
# with open("original_ayakkabi.xml", "wb") as f:
#     f.write(response.content)
# print("Downloaded and saved original XML.")

# # Step 2: Parse XML
# tree = ET.parse("original_ayakkabi.xml")
# root = tree.getroot()

# # Step 3: Load previously translated products
# translated_file = "translatedsample_ayakkabi.xml"
# if os.path.exists(translated_file) and os.path.getsize(translated_file) > 0:
#     try:
#         translated_tree = ET.parse(translated_file)
#         translated_root = translated_tree.getroot()
#         old_products = {p.find("ProductId").text.strip(): p for p in translated_root.findall(".//Product")}
#     except ET.ParseError:
#         print("Warning: Translated file is corrupted. Starting fresh.")
#         translated_root = ET.Element(root.tag)
#         old_products = {}
# else:
#     translated_root = ET.Element(root.tag)
#     old_products = {}

# # Step 4: Setup translator and currency converter
# translator = GoogleTranslator(source='auto', target='en')
# currency = CurrencyRates()
# try:
#     rate = currency.get_rate('TRY', 'USD')
# except Exception as e:
#     print(f"Currency API failed. Using fallback rate. Error: {e}")
#     rate = 0.031
# print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# # Step 5: Translate and update product list
# new_products = root.findall(".//Product")
# final_products = {}

# for product in new_products:
#     product_id_el = product.find("ProductId")
#     if product_id_el is None or not product_id_el.text:
#         continue
#     product_id = product_id_el.text.strip()

#     # Get total stock
#     total_stock = 0
#     for comb in product.findall(".//ProductCombination"):
#         stock_node = comb.find("VariantStockQuantity")
#         if stock_node is not None:
#             try:
#                 total_stock += int(stock_node.text or "0")
#             except:
#                 pass

#     # Skip if stock is 0
#     if total_stock == 0:
#         continue

#     # Use previously translated product if it exists
#     if product_id in old_products:
#         final_products[product_id] = old_products[product_id]
#         continue

#     print(f"Translating new product ID: {product_id}")
#     product_copy = copy.deepcopy(product)

#     # Translate name
#     pname = product_copy.find("ProductName")
#     if pname is not None and pname.text:
#         try:
#             pname.text = translator.translate(pname.text)
#         except Exception as e:
#             print(f"ProductName translation error: {e}")

#     # Translate description
#     fdesc = product_copy.find("FullDescription")
#     if fdesc is not None and fdesc.text:
#         try:
#             fdesc.text = translator.translate(fdesc.text)
#         except Exception as e:
#             print(f"FullDescription translation error: {e}")

#     # Convert price
#     price = product_copy.find("ProductPrice")
#     if price is not None and price.text:
#         try:
#             lira = float(price.text.replace(",", "."))
#             usd = math.ceil(lira * rate * 100) / 100.0
#             price.text = f"{usd:.2f}"
#         except Exception as e:
#             print(f"ProductPrice conversion error: {e}")

#     # Translate variant attributes
#     combinations = product_copy.find("ProductCombinations")
#     if combinations is not None:
#         for combination in combinations.findall("ProductCombination"):
#             attributes = combination.find("ProductAttributes")
#             if attributes is not None:
#                 for attr in attributes.findall("ProductAttribute"):
#                     vname = attr.find("VariantName")
#                     vval = attr.find("VariantValue")
#                     if vname is not None and vname.text:
#                         try:
#                             vname.text = translator.translate(vname.text)
#                         except Exception as e:
#                             print(f"VariantName translation error: {e}")
#                     if vval is not None and vval.text:
#                         try:
#                             vval.text = translator.translate(vval.text)
#                         except Exception as e:
#                             print(f"VariantValue translation error: {e}")

#     final_products[product_id] = product_copy

# # Step 6: Remove zero-stock or missing old products
# new_product_ids = {p.find("ProductId").text.strip() for p in new_products if p.find("ProductId") is not None}
# for pid in list(old_products.keys()):
#     if pid not in new_product_ids:
#         final_products.pop(pid, None)
#         print(f"Removing old product ID {pid} (missing from source).")
#     else:
#         for p in new_products:
#             if p.find("ProductId").text.strip() == pid:
#                 stock = sum(int(c.find("VariantStockQuantity").text or "0") for c in p.findall(".//ProductCombination") if c.find("VariantStockQuantity") is not None)
#                 if stock == 0:
#                     final_products.pop(pid, None)
#                     print(f"Removing old product ID {pid} due to zero stock.")

# # Step 7: Remove unnecessary whitespace to reduce file size
# def strip_whitespace(elem):
#     for el in elem.iter():
#         if el.text and el.text.strip() == "":
#             el.text = None
#         if el.tail and el.tail.strip() == "":
#             el.tail = None

# out_root = ET.Element(root.tag)
# for product in final_products.values():
#     out_root.append(product)

# strip_whitespace(out_root)

# # Step 8: Write compact XML
# out_tree = ET.ElementTree(out_root)
# out_tree.write(translated_file, encoding="utf-8", xml_declaration=True, method="xml", short_empty_elements=True)

# print(f"Updated translations saved to {translated_file}")



import os
import xml.etree.ElementTree as ET
import requests
import time
import json
from deep_translator import GoogleTranslator

# Constants
XML_URL = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
OUTPUT_FILE = "translatesample_ayakkabi.xml"
TRANSLATION_CACHE = "ayakkabi_translation_cache.json"

# Load or initialize translation cache
if os.path.exists(TRANSLATION_CACHE):
    with open(TRANSLATION_CACHE, "r", encoding="utf-8") as f:
        translation_cache = json.load(f)
else:
    translation_cache = {}

def translate_text(text):
    if not text.strip():
        return text
    if text in translation_cache:
        return translation_cache[text]
    try:
        translated = GoogleTranslator(source='tr', target='en').translate(text)
        translation_cache[text] = translated
        time.sleep(0.5)  # To avoid rate limits
        return translated
    except Exception as e:
        print(f"Translation failed for: {text}\nError: {e}")
        return text

def convert_price(try_price):
    try:
        # Dummy conversion rate, should be updated with real-time API if needed
        usd_rate = 0.031
        return round(float(try_price) * usd_rate, 2)
    except:
        return try_price

def load_existing_translations():
    if not os.path.exists(OUTPUT_FILE):
        return {}
    try:
        tree = ET.parse(OUTPUT_FILE)
        root = tree.getroot()
        existing = {}
        for product in root.findall("Product"):
            pid = product.find("ProductId").text
            existing[pid] = product
        return existing
    except Exception as e:
        print(f"Failed to load existing translations: {e}")
        return {}

# Download XML
resp = requests.get(XML_URL)
with open("debug_raw_ayakkabi.xml", "wb") as f:
    f.write(resp.content)
try:
    root = ET.fromstring(resp.content)
except ET.ParseError as e:
    print("XML parsing failed. Check debug_raw_ayakkabi.xml for the raw content.")
    raise e

# Load existing
existing_translations = load_existing_translations()
translated_root = ET.Element("Products")

for product in root.findall("Product"):
    pid = product.find("ProductId").text

    # If product exists, update stock info
    if pid in existing_translations:
        existing = existing_translations[pid]
        existing.find("ProductStockQuantity").text = product.find("ProductStockQuantity").text
        for pc_old, pc_new in zip(existing.findall("ProductCombinations/ProductCombination"), product.findall("ProductCombinations/ProductCombination")):
            pc_old.find("VariantStockQuantity").text = pc_new.find("VariantStockQuantity").text
        translated_root.append(existing)
        continue

    # Translate new product
    new_product = ET.Element("Product")
    for child in product:
        tag = child.tag
        if tag == "ProductName":
            elem = ET.SubElement(new_product, "ProductName")
            elem.text = translate_text(child.text or "")
        elif tag == "FullDescription":
            elem = ET.SubElement(new_product, "FullDescription")
            elem.text = translate_text(child.text or "")
        elif tag == "ProductPrice":
            elem = ET.SubElement(new_product, "ProductPrice")
            elem.text = str(convert_price(child.text or "0"))
        elif tag == "ProductCombinations":
            combinations = ET.SubElement(new_product, "ProductCombinations")
            for pc in child.findall("ProductCombination"):
                new_pc = ET.SubElement(combinations, "ProductCombination")
                for c in pc:
                    if c.tag == "ProductAttributes":
                        pa = ET.SubElement(new_pc, "ProductAttributes")
                        for attr in c.findall("ProductAttribute"):
                            new_attr = ET.SubElement(pa, "ProductAttribute")
                            vn = ET.SubElement(new_attr, "VariantName")
                            vn.text = translate_text(attr.find("VariantName").text or "")
                            vv = ET.SubElement(new_attr, "VariantValue")
                            vv.text = attr.find("VariantValue").text or ""
                    else:
                        e = ET.SubElement(new_pc, c.tag)
                        e.text = c.text or ""
        else:
            e = ET.SubElement(new_product, tag)
            e.text = child.text or ""

    translated_root.append(new_product)

# Save output XML
translated_tree = ET.ElementTree(translated_root)
translated_tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)

# Save translation cache
with open(TRANSLATION_CACHE, "w", encoding="utf-8") as f:
    json.dump(translation_cache, f, ensure_ascii=False, indent=2)

print(f"Translated XML saved to {OUTPUT_FILE}")
