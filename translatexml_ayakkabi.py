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



import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
from forex_python.converter import CurrencyRates
import os

# Load the raw XML file
raw_file = "debug_raw_ayakkabi.xml"
tree = ET.parse(raw_file)
root = tree.getroot()

# Load or create the translated output XML
output_file = "translatedsample_ayakkabi.xml"

if os.path.exists(output_file):
    output_tree = ET.parse(output_file)
    output_root = output_tree.getroot()
else:
    output_root = ET.Element("Products")
    output_tree = ET.ElementTree(output_root)

# Keep track of existing Product IDs to avoid duplicates
existing_ids = set()
for product in output_root.findall("Product"):
    pid = product.find("ProductId")
    if pid is not None:
        existing_ids.add(pid.text)

# Set up translators and currency converter
translator = GoogleTranslator(source='tr', target='en')
currency = CurrencyRates()
try:
    rate = currency.get_rate('TRY', 'USD')
except:
    rate = 0.031  # fallback if API fails

def translate_text(text):
    if text is None or text.strip() == "":
        return ""
    try:
        return translator.translate(text.strip())
    except:
        return text.strip()

for product in root.findall("Product"):
    product_id = product.find("ProductId").text
    if product_id in existing_ids:
        continue

    product_elem = ET.SubElement(output_root, "Product")
    for tag in ["ProductId", "ModelCode", "ProductSku", "ProductGtin", "Tax", "DeliveryTime"]:
        val = product.find(tag)
        if val is not None:
            el = ET.SubElement(product_elem, tag)
            el.text = val.text

    # Translated fields
    pname = product.find("ProductName")
    desc = product.find("FullDescription")
    color = product.find("ProductColor")

    pname_el = ET.SubElement(product_elem, "ProductName")
    pname_el.text = translate_text(pname.text) if pname is not None else ""

    desc_el = ET.SubElement(product_elem, "FullDescription")
    desc_el.text = translate_text(desc.text) if desc is not None else ""

    color_el = ET.SubElement(product_elem, "ProductColor")
    color_el.text = translate_text(color.text) if color is not None else ""

    # Price conversion
    price = product.find("ProductPrice")
    if price is not None:
        try:
            price_usd = float(price.text) * rate
            price_el = ET.SubElement(product_elem, "ProductPrice")
            price_el.text = f"{price_usd:.2f}"
        except:
            pass

    # Product Stock
    stock = product.find("ProductStockQuantity")
    if stock is not None:
        stock_el = ET.SubElement(product_elem, "ProductStockQuantity")
        stock_el.text = stock.text

    # Product Combinations and Variants
    combinations = product.find("ProductCombinations")
    if combinations is not None:
        combos_el = ET.SubElement(product_elem, "ProductCombinations")
        for combo in combinations.findall("ProductCombination"):
            combo_el = ET.SubElement(combos_el, "ProductCombination")
            for ctag in ["ProductCombinationId", "VariantGtin", "VariantStockQuantity"]:
                cval = combo.find(ctag)
                if cval is not None:
                    c_el = ET.SubElement(combo_el, ctag)
                    c_el.text = cval.text
            attrs = combo.find("ProductAttributes")
            if attrs is not None:
                attrs_el = ET.SubElement(combo_el, "ProductAttributes")
                for attr in attrs.findall("ProductAttribute"):
                    attr_el = ET.SubElement(attrs_el, "ProductAttribute")
                    vname = attr.find("VariantName")
                    vval = attr.find("VariantValue")
                    vn_el = ET.SubElement(attr_el, "VariantName")
                    vn_el.text = translate_text(vname.text) if vname is not None else ""
                    vv_el = ET.SubElement(attr_el, "VariantValue")
                    vv_el.text = translate_text(vval.text) if vval is not None else ""

    # Pictures
    pictures = product.find("Pictures")
    if pictures is not None:
        pictures_elem = ET.SubElement(product_elem, "Pictures")
        for picture in pictures.findall("Picture"):
            picture_elem = ET.SubElement(pictures_elem, "Picture")
            url = picture.find("PictureUrl")
            if url is not None:
                url_elem = ET.SubElement(picture_elem, "PictureUrl")
                url_elem.text = url.text.strip() if url.text else ""

# Write the updated XML
output_tree.write(output_file, encoding="utf-8", xml_declaration=True)
print("Translation and picture inclusion complete.")
