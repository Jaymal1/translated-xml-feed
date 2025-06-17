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
import requests
import copy
import os
from datetime import datetime

RAW_URL = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
RAW_FILE = "debug_raw_ayakkabi.xml"
TRANSLATED_FILE = "translatedsample_ayakkabi.xml"

# Fetch and save the raw XML
def fetch_raw_xml():
    response = requests.get(RAW_URL)
    with open(RAW_FILE, "wb") as f:
        f.write(response.content)

# Load XML tree from file
def load_tree(file_path):
    tree = ET.parse(file_path)
    return tree, tree.getroot()

# Save XML tree to file
def save_tree(tree, file_path):
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

# Get USD exchange rate from TRY
def get_usd_rate():
    try:
        response = requests.get("https://api.exchangerate.host/latest?base=TRY&symbols=USD")
        return response.json()["rates"]["USD"]
    except:
        return 0.031  # fallback rate

# Translate text with fallback
def translate_text(text):
    try:
        return GoogleTranslator(source="auto", target="en").translate(text)
    except:
        return text

# Get all existing product IDs to avoid re-translating
def get_existing_ids(root):
    return {prod.find("ProductId").text for prod in root.findall("Product")}

# Main translation and merging logic
def translate_and_merge():
    fetch_raw_xml()

    raw_tree, raw_root = load_tree(RAW_FILE)

    if os.path.exists(TRANSLATED_FILE):
        translated_tree, translated_root = load_tree(TRANSLATED_FILE)
    else:
        translated_root = ET.Element("Products")
        translated_tree = ET.ElementTree(translated_root)

    existing_ids = get_existing_ids(translated_root)
    usd_rate = get_usd_rate()

    for raw_product in raw_root.findall("Product"):
        product_id = raw_product.find("ProductId").text

        # If product already exists, update stock only
        existing_product = next((p for p in translated_root.findall("Product") if p.find("ProductId").text == product_id), None)
        if existing_product:
            # Update stock quantities
            existing_product.find("ProductStockQuantity").text = raw_product.find("ProductStockQuantity").text

            raw_combinations = raw_product.find("ProductCombinations")
            translated_combinations = existing_product.find("ProductCombinations")
            if raw_combinations is not None and translated_combinations is not None:
                for raw_comb in raw_combinations.findall("ProductCombination"):
                    comb_id = raw_comb.find("ProductCombinationId").text
                    matching_comb = translated_combinations.find(f"./ProductCombination[ProductCombinationId='{comb_id}']")
                    if matching_comb is not None:
                        matching_comb.find("VariantStockQuantity").text = raw_comb.find("VariantStockQuantity").text
            continue

        # Translate new product
        new_product = copy.deepcopy(raw_product)

        # Translate ProductName
        name_tag = new_product.find("ProductName")
        if name_tag is not None:
            name_tag.text = translate_text(name_tag.text or "")

        # Translate FullDescription
        desc_tag = new_product.find("FullDescription")
        if desc_tag is not None:
            desc_tag.text = translate_text(desc_tag.text or "")

        # Translate variant attributes
        combinations = new_product.find("ProductCombinations")
        if combinations is not None:
            for comb in combinations.findall("ProductCombination"):
                attrs = comb.find("ProductAttributes")
                if attrs is not None:
                    for attr in attrs.findall("ProductAttribute"):
                        var_name = attr.find("VariantName")
                        var_value = attr.find("VariantValue")
                        if var_name is not None:
                            var_name.text = translate_text(var_name.text or "")
                        if var_value is not None:
                            var_value.text = translate_text(var_value.text or "")

        # Convert price from TRY to USD
        price_tag = new_product.find("ProductPrice")
        if price_tag is not None:
            try:
                price_try = float(price_tag.text)
                price_usd = round(price_try * usd_rate, 2)
                price_tag.text = str(price_usd)
            except:
                pass

        # Copy Pictures
        pictures_tag = raw_product.find("Pictures")
        if pictures_tag is not None:
            existing_pictures = new_product.find("Pictures")
            if existing_pictures is not None:
                new_product.remove(existing_pictures)
            new_product.append(copy.deepcopy(pictures_tag))

        # Copy Categories
        categories_tag = raw_product.find("Categories")
        if categories_tag is not None:
            existing_categories = new_product.find("Categories")
            if existing_categories is not None:
                new_product.remove(existing_categories)
            new_product.append(copy.deepcopy(categories_tag))

        # Copy Manufacturers
        manufacturers_tag = raw_product.find("Manufacturers")
        if manufacturers_tag is not None:
            existing_manufacturers = new_product.find("Manufacturers")
            if existing_manufacturers is not None:
                new_product.remove(existing_manufacturers)
            new_product.append(copy.deepcopy(manufacturers_tag))

        # Append translated product
        translated_root.append(new_product)

    save_tree(translated_tree, TRANSLATED_FILE)
    print(f"[{datetime.now().isoformat()}] Translation completed and saved to {TRANSLATED_FILE}")

if __name__ == "__main__":
    translate_and_merge()
