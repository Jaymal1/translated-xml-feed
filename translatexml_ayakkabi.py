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










import os
import requests
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
from forex_python.converter import CurrencyRates
import math
import copy

# Files
translated_file = "translatedsample_ayakkabi.xml"
original_file = "original_ayakkabi.xml"

# Download latest XML
url = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
response = requests.get(url)
with open(original_file, "wb") as f:
    f.write(response.content)
print("Downloaded and saved original XML.")

# Parse the downloaded XML
tree = ET.parse(original_file)
root = tree.getroot()
new_products = root.findall(".//Product")
print(f"Parsed XML with {len(new_products)} products.")

# Load previously translated products
if os.path.exists(translated_file) and os.path.getsize(translated_file) > 0:
    try:
        old_tree = ET.parse(translated_file)
        old_root = old_tree.getroot()
        old_products = {p.find("ProductId").text: p for p in old_root.findall(".//Product")}
        print(f"Loaded {len(old_products)} previously translated products.")
    except ET.ParseError:
        print("Warning: Previous translation file corrupted or invalid.")
        old_products = {}
else:
    old_products = {}
    print("No previously translated file found or it's empty.")

# Set up translator and exchange rate
translator = GoogleTranslator(source='auto', target='en')
currency = CurrencyRates()
try:
    rate = currency.get_rate('TRY', 'USD')
except Exception as e:
    print(f"Currency API failed. Using fallback rate. Error: {e}")
    rate = 0.031
print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# Helpers
def get_total_stock(product):
    stock = 0
    for c in product.findall(".//ProductCombination"):
        s = c.find("VariantStockQuantity")
        if s is not None and s.text and s.text.isdigit():
            stock += int(s.text)
    return stock

def translate_text(el):
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

final_products = {}

# Translate and collect valid products
for product in new_products:
    product_id_el = product.find("ProductId")
    if product_id_el is None or not product_id_el.text:
        continue
    pid = product_id_el.text.strip()

    stock = get_total_stock(product)
    if stock == 0:
        continue

    if pid in old_products:
        final_products[pid] = old_products[pid]
        continue

    print(f"Translating new product ID: {pid}")
    translated = copy.deepcopy(product)

    translate_text(translated.find("ProductName"))
    translate_text(translated.find("FullDescription"))
    convert_price(translated.find("ProductPrice"))

    combinations = translated.find("ProductCombinations")
    if combinations is not None:
        for combination in combinations.findall("ProductCombination"):
            attributes = combination.find("ProductAttributes")
            if attributes is not None:
                for attr in attributes.findall("ProductAttribute"):
                    translate_text(attr.find("VariantName"))
                    translate_text(attr.find("VariantValue"))

    final_products[pid] = translated

# Remove old products with 0 stock or missing in new feed
current_ids = {p.find("ProductId").text.strip() for p in new_products if p.find("ProductId") is not None}
for pid, prod in old_products.items():
    if pid not in current_ids:
        print(f"Removing product ID {pid} (no longer exists).")
        continue
    matching = next((p for p in new_products if p.find("ProductId").text.strip() == pid), None)
    if matching and get_total_stock(matching) == 0:
        print(f"Removing product ID {pid} due to zero stock.")
        continue
    final_products[pid] = prod  # Still valid

# Save updated translations
if final_products:
    out_root = ET.Element(root.tag)
    for prod in final_products.values():
        out_root.append(prod)
    out_tree = ET.ElementTree(out_root)
    out_tree.write(translated_file, encoding="utf-8", xml_declaration=True)
    print(f"Saved {len(final_products)} translated products to {translated_file}.")
else:
    print("No valid products to save. Skipping file write.")

