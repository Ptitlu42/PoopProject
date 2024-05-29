import requests
from generate_image import generate_image

import os

def download_image(image_url):
    filename = image_url.split('?')[0].split('/')[-1]
    safe_filename = filename.replace(':', '_').replace('/', '_').replace('?', '_').replace('&', '_') + ".jpg"
    file_path = os.path.join('generated', safe_filename)

    os.makedirs('generated', exist_ok=True)

    response = requests.get(image_url)

    if response.status_code == 200:
        with open(file_path, 'wb') as image_file:
            image_file.write(response.content)
        print(f"L'image a été téléchargée et enregistrée sous : {file_path}")
    else:
        print(f"Erreur lors du téléchargement de l'image : {response.status_code}")
