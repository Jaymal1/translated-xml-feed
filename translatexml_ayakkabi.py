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



import os
import requests
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
from forex_python.converter import CurrencyRates
import math
import copy
import xml.dom.minidom

# Step 1: Download latest XML
url = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
response = requests.get(url)
with open("original_ayakkabi.xml", "wb") as f:
    f.write(response.content)
print("Downloaded and saved original XML.")

# Step 2: Parse XML
tree = ET.parse("original_ayakkabi.xml")
root = tree.getroot()

# Step 3: Load previously translated products
translated_file = "translatedsample_ayakkabi.xml"
if os.path.exists(translated_file):
    translated_tree = ET.parse(translated_file)
    translated_root = translated_tree.getroot()
    old_products = {p.find("ProductId").text: p for p in translated_root.findall(".//Product")}
else:
    translated_root = ET.Element(root.tag)
    old_products = {}

# Step 4: Setup translator and currency converter
translator = GoogleTranslator(source='auto', target='en')
currency = CurrencyRates()
try:
    rate = currency.get_rate('TRY', 'USD')
except Exception as e:
    print(f"Currency API failed. Using fallback rate. Error: {e}")
    rate = 0.031
print(f"Using exchange rate: 1 TRY = {rate:.4f} USD")

# Step 5: Translate and update product list
new_products = root.findall(".//Product")
final_products = {}

for product in new_products:
    product_id = product.find("ProductId").text.strip()

    # Get total stock (sum of VariantStockQuantity)
    total_stock = 0
    for comb in product.findall(".//ProductCombination"):
        stock_node = comb.find("VariantStockQuantity")
        if stock_node is not None:
            total_stock += int(stock_node.text or "0")

    # Skip if stock is 0
    if total_stock == 0:
        continue

    if product_id in old_products:
        final_products[product_id] = old_products[product_id]
        continue  # Already translated, no need to translate again

    print(f"Translating new product ID: {product_id}")
    product_copy = copy.deepcopy(product)

    # Translate name
    pname = product_copy.find("ProductName")
    if pname is not None and pname.text:
        try:
            pname.text = translator.translate(pname.text)
        except Exception as e:
            print(f"ProductName translation error: {e}")

    # Translate description
    fdesc = product_copy.find("FullDescription")
    if fdesc is not None and fdesc.text:
        try:
            fdesc.text = translator.translate(fdesc.text)
        except Exception as e:
            print(f"FullDescription translation error: {e}")

    # Convert price
    price = product_copy.find("ProductPrice")
    if price is not None and price.text:
        try:
            lira = float(price.text.replace(",", "."))
            usd = math.ceil(lira * rate * 100) / 100.0
            price.text = f"{usd:.2f}"
        except Exception as e:
            print(f"ProductPrice conversion error: {e}")

    # Translate variant attributes
    combinations = product_copy.find("ProductCombinations")
    if combinations is not None:
        for combination in combinations.findall("ProductCombination"):
            attributes = combination.find("ProductAttributes")
            if attributes is not None:
                for attr in attributes.findall("ProductAttribute"):
                    vname = attr.find("VariantName")
                    vval = attr.find("VariantValue")
                    if vname is not None and vname.text:
                        try:
                            vname.text = translator.translate(vname.text)
                        except Exception as e:
                            print(f"VariantName translation error: {e}")
                    if vval is not None and vval.text:
                        try:
                            vval.text = translator.translate(vval.text)
                        except Exception as e:
                            print(f"VariantValue translation error: {e}")

    final_products[product_id] = product_copy

# Step 6: Remove zero-stock old products
for pid in list(old_products.keys()):
    if pid not in [p.find("ProductId").text for p in new_products]:
        continue  # Product no longer exists
    for p in new_products:
        if p.find("ProductId").text == pid:
            stock = sum(int(c.find("VariantStockQuantity").text or "0") for c in p.findall(".//ProductCombination"))
            if stock == 0:
                print(f"Removing old product ID {pid} due to zero stock.")
                final_products.pop(pid, None)

# Step 7: Write back to file
translated_root = ET.Element(root.tag)
for product in final_products.values():
    translated_root.append(product)

rough_string = ET.tostring(translated_root, encoding='utf-8')
reparsed = xml.dom.minidom.parseString(rough_string)
with open(translated_file, "w", encoding="utf-8") as f:
    f.write(reparsed.toprettyxml(indent="  "))

print(f"Updated translations saved to {translated_file}")

