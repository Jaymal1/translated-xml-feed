# import os
# import requests
# import xml.etree.ElementTree as ET
# from deep_translator import GoogleTranslator
# from forex_python.converter import CurrencyRates
# import math
# import copy
# import xml.dom.minidom

# def run_script1():
#     print("Running Script 1 (Ayakkabi XML)...")

#     url = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
#     response = requests.get(url)
#     with open("original_ayakkabi.xml", "wb") as f:
#         f.write(response.content)

#     tree = ET.parse("original_ayakkabi.xml")
#     root = tree.getroot()

#     translator = GoogleTranslator(source='auto', target='en')
#     currency = CurrencyRates()
#     try:
#         rate = currency.get_rate('TRY', 'USD')
#     except Exception as e:
#         print(f"Currency API failed. Using fallback rate. Error: {e}")
#         rate = 0.031

#     translated_root = ET.Element(root.tag)
#     products = root.findall(".//Product")

#     for i, product in enumerate(products, start=1):
#         print(f"Translating product {i}...")
#         product_copy = copy.deepcopy(product)

#         pname = product_copy.find("ProductName")
#         if pname is not None and pname.text:
#             try:
#                 pname.text = translator.translate(pname.text)
#             except Exception as e:
#                 print(f"ProductName translation error: {e}")

#         fdesc = product_copy.find("FullDescription")
#         if fdesc is not None and fdesc.text:
#             try:
#                 fdesc.text = translator.translate(fdesc.text)
#             except Exception as e:
#                 print(f"FullDescription translation error: {e}")

#         price = product_copy.find("ProductPrice")
#         if price is not None and price.text:
#             try:
#                 lira = float(price.text.replace(",", "."))
#                 usd = math.ceil(lira * rate * 100) / 100.0
#                 price.text = f"{usd:.2f}"
#             except Exception as e:
#                 print(f"ProductPrice conversion error: {e}")

#         combinations = product_copy.find("ProductCombinations")
#         if combinations is not None:
#             for combination in combinations.findall("ProductCombination"):
#                 attributes = combination.find("ProductAttributes")
#                 if attributes is not None:
#                     for attr in attributes.findall("ProductAttribute"):
#                         vname = attr.find("VariantName")
#                         vval = attr.find("VariantValue")
#                         if vname is not None and vname.text:
#                             try:
#                                 vname.text = translator.translate(vname.text)
#                             except Exception as e:
#                                 print(f"VariantName translation error: {e}")
#                         if vval is not None and vval.text:
#                             try:
#                                 vval.text = translator.translate(vval.text)
#                             except Exception as e:
#                                 print(f"VariantValue translation error: {e}")

#         translated_root.append(product_copy)

#     rough_string = ET.tostring(translated_root, encoding='utf-8')
#     reparsed = xml.dom.minidom.parseString(rough_string)
#     with open("translatedsample_ayakkabi.xml", "w", encoding="utf-8") as f:
#         f.write(reparsed.toprettyxml(indent="  "))

#     print("Script 1 completed.")


# def run_script2():
#     print("Running Script 2 (Gecelik XML)...")

#     url = "https://gecelikmagazasi.com/TicimaxXml/CB0C2D2195694477A0657C567D29C8AF"
#     response = requests.get(url)
#     with open("original.xml", "wb") as f:
#         f.write(response.content)

#     tree = ET.parse("original.xml")
#     root = tree.getroot()

#     translator = GoogleTranslator(source='auto', target='en')
#     currency = CurrencyRates()
#     try:
#         rate = currency.get_rate('TRY', 'USD')
#     except Exception as e:
#         print(f"Currency API failed. Using fallback rate. Error: {e}")
#         rate = 0.031

#     translated_root = ET.Element(root.tag)
#     products = root.findall(".//Urun")

#     for i, product in enumerate(products, start=1):
#         print(f"Translating product {i}...")

#         name = product.find("UrunAdi")
#         if name is not None and name.text:
#             name.text = translator.translate(name.text)

#         description = product.find("Aciklama")
#         if description is not None and description.text:
#             description.text = translator.translate(description.text)

#         secenek = product.find("EksecenekOzellik")
#         if secenek is not None and secenek.text:
#             secenek.text = translator.translate(secenek.text)

#         price = product.find("Fiyat")
#         if price is not None and price.text:
#             try:
#                 lira_value = float(price.text.replace(",", "."))
#                 usd_value = math.ceil(lira_value * rate * 100) / 100.0
#                 price.text = f"{usd_value:.2f}"
#             except Exception as e:
#                 print(f"Could not convert price: {price.text}, error: {e}")

#         urun_secenek = product.find("UrunSecenek")
#         if urun_secenek is not None:
#             for variant in urun_secenek.findall("Secenek"):
#                 eksecenek = variant.find("EkSecenekOzellik")
#                 if eksecenek is not None:
#                     for attr in eksecenek.findall("Ozellik"):
#                         if attr.text:
#                             try:
#                                 attr.text = translator.translate(attr.text)
#                             except Exception as e:
#                                 print(f"Text translation error: {e}")
#                         if "Deger" in attr.attrib:
#                             try:
#                                 attr.attrib["Deger"] = translator.translate(attr.attrib["Deger"])
#                             except Exception as e:
#                                 print(f"Deger translation error: {e}")
#                         if "Tanim" in attr.attrib:
#                             try:
#                                 attr.attrib["Tanim"] = translator.translate(attr.attrib["Tanim"])
#                             except Exception as e:
#                                 print(f"Tanim translation error: {e}")

#         translated_root.append(product)

#     rough_string = ET.tostring(translated_root, encoding='utf-8')
#     reparsed = xml.dom.minidom.parseString(rough_string)
#     with open("translatedsample_gecelik.xml", "w", encoding="utf-8") as f:
#         f.write(reparsed.toprettyxml(indent="  "))

#     print("Script 2 completed.")


# def run_script(request=None):
#     run_script1()
#     run_script2()
#     return "Both scripts executed successfully!"



# import os
# import json
# import hashlib
# import requests
# import xml.etree.ElementTree as ET
# from deep_translator import GoogleTranslator
# from forex_python.converter import CurrencyRates
# import math
# import copy
# import xml.dom.minidom

# def load_processed_ids(filename):
#     if os.path.exists(filename):
#         with open(filename, "r", encoding="utf-8") as f:
#             return set(json.load(f))
#     return set()

# def save_processed_ids(ids, filename):
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(list(ids), f)

# def hash_text(text):
#     return hashlib.md5(text.strip().lower().encode("utf-8")).hexdigest()

# def get_product_id_ayakkabi(product):
#     # No explicit ID: hash ProductName as ID
#     pname = product.find("ProductName")
#     if pname is not None and pname.text:
#         return hash_text(pname.text)
#     return None

# def get_product_id_gecelik(product):
#     pid = product.find("UrunKartiID")
#     if pid is not None and pid.text and pid.text.isdigit():
#         return pid.text.strip()
#     # fallback: combine UrunAdi + Marka + UrunUrl
#     parts = []
#     for tag in ["UrunAdi", "Marka", "UrunUrl"]:
#         elem = product.find(tag)
#         if elem is not None and elem.text:
#             parts.append(elem.text.strip().lower())
#     if parts:
#         combined = "|".join(parts)
#         return hash_text(combined)
#     return None

# def run_script1():
#     print("Running Script 1 (Ayakkabi XML)...")

#     url = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
#     response = requests.get(url)
#     with open("original_ayakkabi.xml", "wb") as f:
#         f.write(response.content)

#     tree = ET.parse("original_ayakkabi.xml")
#     root = tree.getroot()

#     translator = GoogleTranslator(source='auto', target='en')
#     currency = CurrencyRates()
#     try:
#         rate = currency.get_rate('TRY', 'USD')
#     except Exception as e:
#         print(f"Currency API failed. Using fallback rate. Error: {e}")
#         rate = 0.031

#     processed_ids_file = "processed_ids_ayakkabi.json"
#     processed_ids = load_processed_ids(processed_ids_file)
#     new_processed_ids = set()

#     translated_root = ET.Element(root.tag)
#     products = root.findall(".//Product")

#     for i, product in enumerate(products, start=1):
#         product_id = get_product_id_ayakkabi(product)
#         if product_id is None:
#             print(f"Skipping product {i} with no valid ID.")
#             continue

#         if product_id in processed_ids:
#             print(f"Skipping already processed product {i}")
#             translated_root.append(copy.deepcopy(product))  # Append without translating
#             continue

#         print(f"Translating new product {i}...")
#         product_copy = copy.deepcopy(product)

#         pname = product_copy.find("ProductName")
#         if pname is not None and pname.text:
#             try:
#                 pname.text = translator.translate(pname.text)
#             except Exception as e:
#                 print(f"ProductName translation error: {e}")

#         fdesc = product_copy.find("FullDescription")
#         if fdesc is not None and fdesc.text:
#             try:
#                 fdesc.text = translator.translate(fdesc.text)
#             except Exception as e:
#                 print(f"FullDescription translation error: {e}")

#         price = product_copy.find("ProductPrice")
#         if price is not None and price.text:
#             try:
#                 lira = float(price.text.replace(",", "."))
#                 usd = math.ceil(lira * rate * 100) / 100.0
#                 price.text = f"{usd:.2f}"
#             except Exception as e:
#                 print(f"ProductPrice conversion error: {e}")

#         combinations = product_copy.find("ProductCombinations")
#         if combinations is not None:
#             for combination in combinations.findall("ProductCombination"):
#                 attributes = combination.find("ProductAttributes")
#                 if attributes is not None:
#                     for attr in attributes.findall("ProductAttribute"):
#                         vname = attr.find("VariantName")
#                         vval = attr.find("VariantValue")
#                         if vname is not None and vname.text:
#                             try:
#                                 vname.text = translator.translate(vname.text)
#                             except Exception as e:
#                                 print(f"VariantName translation error: {e}")
#                         if vval is not None and vval.text:
#                             try:
#                                 vval.text = translator.translate(vval.text)
#                             except Exception as e:
#                                 print(f"VariantValue translation error: {e}")

#         translated_root.append(product_copy)
#         new_processed_ids.add(product_id)

#     all_processed_ids = processed_ids.union(new_processed_ids)
#     save_processed_ids(all_processed_ids, processed_ids_file)

#     rough_string = ET.tostring(translated_root, encoding='utf-8')
#     reparsed = xml.dom.minidom.parseString(rough_string)
#     with open("translatedsample_ayakkabi.xml", "w", encoding="utf-8") as f:
#         f.write(reparsed.toprettyxml(indent="  "))

#     print("Script 1 completed.")

# def run_script2():
#     print("Running Script 2 (Gecelik XML)...")

#     url = "https://gecelikmagazasi.com/TicimaxXml/CB0C2D2195694477A0657C567D29C8AF"
#     response = requests.get(url)
#     with open("original.xml", "wb") as f:
#         f.write(response.content)

#     tree = ET.parse("original.xml")
#     root = tree.getroot()

#     translator = GoogleTranslator(source='auto', target='en')
#     currency = CurrencyRates()
#     try:
#         rate = currency.get_rate('TRY', 'USD')
#     except Exception as e:
#         print(f"Currency API failed. Using fallback rate. Error: {e}")
#         rate = 0.031

#     processed_ids_file = "processed_ids_gecelik.json"
#     processed_ids = load_processed_ids(processed_ids_file)
#     new_processed_ids = set()

#     translated_root = ET.Element(root.tag)
#     products = root.findall(".//Urun")

#     for i, product in enumerate(products, start=1):
#         product_id = get_product_id_gecelik(product)
#         if product_id is None:
#             print(f"Skipping product {i} with no valid ID.")
#             continue

#         if product_id in processed_ids:
#             print(f"Skipping already processed product {i}")
#             translated_root.append(copy.deepcopy(product))  # Append without translating
#             continue

#         print(f"Translating new product {i}...")

#         product_copy = copy.deepcopy(product)

#         name = product_copy.find("UrunAdi")
#         if name is not None and name.text:
#             try:
#                 name.text = translator.translate(name.text)
#             except Exception as e:
#                 print(f"UrunAdi translation error: {e}")

#         description = product_copy.find("Aciklama")
#         if description is not None and description.text:
#             try:
#                 description.text = translator.translate(description.text)
#             except Exception as e:
#                 print(f"Aciklama translation error: {e}")

#         secenek = product_copy.find("EksecenekOzellik")
#         if secenek is not None and secenek.text:
#             try:
#                 secenek.text = translator.translate(secenek.text)
#             except Exception as e:
#                 print(f"EksecenekOzellik translation error: {e}")

#         price = product_copy.find("Fiyat")
#         if price is not None and price.text:
#             try:
#                 lira_value = float(price.text.replace(",", "."))
#                 usd_value = math.ceil(lira_value * rate * 100) / 100.0
#                 price.text = f"{usd_value:.2f}"
#             except Exception as e:
#                 print(f"Price conversion error: {e}")

#         urun_secenek = product_copy.find("UrunSecenek")
#         if urun_secenek is not None:
#             for variant in urun_secenek.findall("Secenek"):
#                 eksecenek = variant.find("EkSecenekOzellik")
#                 if eksecenek is not None:
#                     for attr in eksecenek.findall("Ozellik"):
#                         if attr.text:
#                             try:
#                                 attr.text = translator.translate(attr.text)
#                             except Exception as e:
#                                 print(f"EkSecenekOzellik text translation error: {e}")
#                         if "Deger" in attr.attrib:
#                             try:
#                                 attr.attrib["Deger"] = translator.translate(attr.attrib["Deger"])
#                             except Exception as e:
#                                 print(f"Deger translation error: {e}")
#                         if "Tanim" in attr.attrib:
#                             try:
#                                 attr.attrib["Tanim"] = translator.translate(attr.attrib["Tanim"])
#                             except Exception as e:
#                                 print(f"Tanim translation error: {e}")

#         translated_root.append(product_copy)
#         new_processed_ids.add(product_id)

#     all_processed_ids = processed_ids.union(new_processed_ids)
#     save_processed_ids(all_processed_ids, processed_ids_file)

#     rough_string = ET.tostring(translated_root, encoding='utf-8')
#     reparsed = xml.dom.minidom.parseString(rough_string)
#     with open("translatedsample_gecelik.xml", "w", encoding="utf-8") as f:
#         f.write(reparsed.toprettyxml(indent="  "))

#     print("Script 2 completed.")

# def run_script(request=None):
#     run_script1()
#     run_script2()
#     return "Both scripts executed successfully!"








import os
import json
import hashlib
import requests
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
from forex_python.converter import CurrencyRates
import math
import copy
import xml.dom.minidom

def load_processed_ids(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_processed_ids(ids, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(list(ids), f)

def hash_text(text):
    return hashlib.md5(text.strip().lower().encode("utf-8")).hexdigest()

def get_product_id_ayakkabi(product):
    pname = product.find("ProductName")
    if pname is not None and pname.text:
        return hash_text(pname.text)
    return None

def get_product_id_gecelik(product):
    pid = product.find("UrunKartiID")
    if pid is not None and pid.text and pid.text.isdigit():
        return pid.text.strip()
    parts = []
    for tag in ["UrunAdi", "Marka", "UrunUrl"]:
        elem = product.find(tag)
        if elem is not None and elem.text:
            parts.append(elem.text.strip().lower())
    if parts:
        combined = "|".join(parts)
        return hash_text(combined)
    return None

def get_product_id_moda(product):
    pid = product.find("ProductId")
    if pid is not None and pid.text and pid.text.strip().isdigit():
        return pid.text.strip()
    name = product.find("ProductName")
    if name is not None and name.text:
        return hash_text(name.text)
    return None

def run_script1():
    print("Running Script 1 (Ayakkabi XML)...")
    url = "https://www.ayakkabixml.com/index.php?route=ddaxml/xml_export&kullanici_adi=64f72a582b29a&sifre=53160962&key=da3fc42e3"
    response = requests.get(url)
    with open("original_ayakkabi.xml", "wb") as f:
        f.write(response.content)

    tree = ET.parse("original_ayakkabi.xml")
    root = tree.getroot()
    translator = GoogleTranslator(source='auto', target='en')
    currency = CurrencyRates()
    try:
        rate = currency.get_rate('TRY', 'USD')
    except Exception as e:
        print(f"Currency API failed. Using fallback rate. Error: {e}")
        rate = 0.031

    processed_ids_file = "processed_ids_ayakkabi.json"
    processed_ids = load_processed_ids(processed_ids_file)
    new_processed_ids = set()
    translated_root = ET.Element(root.tag)
    products = root.findall(".//Product")

    for i, product in enumerate(products, start=1):
        product_id = get_product_id_ayakkabi(product)
        if product_id is None:
            print(f"Skipping product {i} with no valid ID.")
            continue
        if product_id in processed_ids:
            print(f"Skipping already processed product {i}")
            translated_root.append(copy.deepcopy(product))
            continue

        print(f"Translating new product {i}...")
        product_copy = copy.deepcopy(product)
        for tag in ["ProductName", "FullDescription"]:
            elem = product_copy.find(tag)
            if elem is not None and elem.text:
                try:
                    elem.text = translator.translate(elem.text)
                except Exception as e:
                    print(f"{tag} translation error: {e}")

        price = product_copy.find("ProductPrice")
        if price is not None and price.text:
            try:
                lira = float(price.text.replace(",", "."))
                usd = math.ceil(lira * rate * 100) / 100.0
                price.text = f"{usd:.2f}"
            except Exception as e:
                print(f"ProductPrice conversion error: {e}")

        combinations = product_copy.find("ProductCombinations")
        if combinations is not None:
            for combination in combinations.findall("ProductCombination"):
                attributes = combination.find("ProductAttributes")
                if attributes is not None:
                    for attr in attributes.findall("ProductAttribute"):
                        for tag in ["VariantName", "VariantValue"]:
                            elem = attr.find(tag)
                            if elem is not None and elem.text:
                                try:
                                    elem.text = translator.translate(elem.text)
                                except Exception as e:
                                    print(f"{tag} translation error: {e}")

        translated_root.append(product_copy)
        new_processed_ids.add(product_id)

    save_processed_ids(processed_ids.union(new_processed_ids), processed_ids_file)
    rough_string = ET.tostring(translated_root, encoding='utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    with open("translatedsample_ayakkabi.xml", "w", encoding="utf-8") as f:
        f.write(reparsed.toprettyxml(indent="  "))
    print("Script 1 completed.")

def run_script2():
    print("Running Script 2 (Gecelik XML)...")
    url = "https://gecelikmagazasi.com/TicimaxXml/CB0C2D2195694477A0657C567D29C8AF"
    response = requests.get(url)
    with open("original.xml", "wb") as f:
        f.write(response.content)

    tree = ET.parse("original.xml")
    root = tree.getroot()
    translator = GoogleTranslator(source='auto', target='en')
    currency = CurrencyRates()
    try:
        rate = currency.get_rate('TRY', 'USD')
    except Exception as e:
        print(f"Currency API failed. Using fallback rate. Error: {e}")
        rate = 0.031

    processed_ids_file = "processed_ids_gecelik.json"
    processed_ids = load_processed_ids(processed_ids_file)
    new_processed_ids = set()
    translated_root = ET.Element(root.tag)
    products = root.findall(".//Urun")

    for i, product in enumerate(products, start=1):
        product_id = get_product_id_gecelik(product)
        if product_id is None:
            print(f"Skipping product {i} with no valid ID.")
            continue
        if product_id in processed_ids:
            print(f"Skipping already processed product {i}")
            translated_root.append(copy.deepcopy(product))
            continue

        print(f"Translating new product {i}...")
        product_copy = copy.deepcopy(product)
        for tag in ["UrunAdi", "Aciklama", "EksecenekOzellik"]:
            elem = product_copy.find(tag)
            if elem is not None and elem.text:
                try:
                    elem.text = translator.translate(elem.text)
                except Exception as e:
                    print(f"{tag} translation error: {e}")

        price = product_copy.find("Fiyat")
        if price is not None and price.text:
            try:
                lira_value = float(price.text.replace(",", "."))
                usd_value = math.ceil(lira_value * rate * 100) / 100.0
                price.text = f"{usd_value:.2f}"
            except Exception as e:
                print(f"Price conversion error: {e}")

        urun_secenek = product_copy.find("UrunSecenek")
        if urun_secenek is not None:
            for variant in urun_secenek.findall("Secenek"):
                eksecenek = variant.find("EkSecenekOzellik")
                if eksecenek is not None:
                    for attr in eksecenek.findall("Ozellik"):
                        if attr.text:
                            try:
                                attr.text = translator.translate(attr.text)
                            except Exception as e:
                                print(f"EkSecenekOzellik text translation error: {e}")
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

        translated_root.append(product_copy)
        new_processed_ids.add(product_id)

    save_processed_ids(processed_ids.union(new_processed_ids), processed_ids_file)
    rough_string = ET.tostring(translated_root, encoding='utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    with open("translatedsample_gecelik.xml", "w", encoding="utf-8") as f:
        f.write(reparsed.toprettyxml(indent="  "))
    print("Script 2 completed.")



# def run_script(request=None):
#     run_script1()
#     run_script2()
#     run_script3()
#     return "All three scripts executed successfully!"
def run_script():
    print("Starting XML translation scripts...\n")
    run_script1()
    print("\nFinished Script 1 (Gecelik)\n")
    
    run_script2()
    print("\nFinished Script 2 (Ayakkabi)\n")
    
    # run_script3()
    # print("\nFinished Script 3 (Moda Yakamoz)\n")
    
    print("All scripts completed.")
