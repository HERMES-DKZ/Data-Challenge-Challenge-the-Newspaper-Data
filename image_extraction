import pandas as pd
import requests
import xml.etree.ElementTree as ET
import os
import heapq

# Lade deine Datensätze
#Hier die Datei eintragen, die als Grundlage verwendet wird
zeitungen = pd.read_pickle("newspapers_ger_1914_part_1") 

#Für die API wird ein Schlüssel und ein Account bei der DDB benötigt. Unter folgendem Link kann ein Account erstellt werden und anschließend kostenlos ein API-Key beantragt werden: https://www.deutsche-digitale-bibliothek.de/user/apikey
api_key = ""                                                                                              
base_url = "https://api.deutsche-digitale-bibliothek.de/items"                                            
headers = {'accept': 'application/xml'}
if not os.path.exists(images):
    os.mkdir(images)
download_dir = "images"


id_old=1
for index, data in zeitungen.iterrows():         # Iteriere durch DataFrame-Reihen
    id = data['page_id'][:32]                    # Zuschneiden der page_id, da dies die ID der Zeitschrift ist



    # Da in Datensatz jede Seite einzeln enthalten ist, wird hier geguckt, ob ID schonmal verwendet wurde
    if id != id_old:

        # URL zusammenstellen, für API anfrage
        url_zeitung = f"{base_url}/{id}/source/record?oauth_consumer_key={api_key}"

        # API-Anfrage
        response = requests.get(url_zeitung, headers=headers)

        # XML Daten parsen
        root = ET.fromstring(response.content)

        # Namespace Definitionen
        namespaces = {
            'mets': 'http://www.loc.gov/METS/',
            'xlink': 'http://www.w3.org/1999/xlink'
        }

        # Alle `file` Elemente suchen, die das MIMETYPE-Attribut "image/jpeg" haben
        image_files = root.findall('.//mets:file[@MIMETYPE="image/jpeg"]', namespaces=namespaces)

        # Extrahieren der URLs der Bilder aus dem XML
        image_urls = []
        for file in image_files:
            image_url = file.find('mets:FLocat', namespaces=namespaces).get('{http://www.w3.org/1999/xlink}href')
            image_urls.append(image_url)

        number_pages = int(len(image_urls)/4)               #Herausfinden, wie viele Seiten die Zeitschrift hat, da Bilder immer in vier Formaten vorhanden sind, wird durch 4 geteilt


        # Bilder herunterladen und nur die größten Speichern
        images = []
        images_len = []
        for image_url in image_urls:
            response_image = requests.get(image_url)
            if response_image.status_code == 200:
                images.append(response_image)
                images_len.append(len(response_image.content))

        image_pairs = list(zip(images, images_len))


        largest_images = heapq.nlargest(number_pages, image_pairs, key=lambda x: x[1])

        # Sortiere die extrahierten größten Bilder nach ihrem ursprünglichen Index, um die Reihenfolge beizubehalten
        largest_images_sorted = sorted(largest_images, key=lambda x: images_len.index(x[1]))

        # Extrahiere die Bilder aus den größten Bildpaaren in der ursprünglichen Reihenfolge
        largest_images = [pair[0] for pair in largest_images_sorted]

        counter = 1
        path = f"{download_dir}/{id}"
        if not os.path.exists(path):
            os.makedirs(path)

        for image in largest_images:
            with open(f"{path}/{counter}.jpg", 'wb') as f:
                f.write(image.content)
            counter += 1


        id_old = id
