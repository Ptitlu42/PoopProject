import os
import requests

def download_image(image_url):
    filename = image_url.split('?')[0].split('/')[-1]
    safe_filename = filename.replace(':', '_').replace('/', '_').replace('?', '_').replace('&', '_') + ".jpg"
    file_path = os.path.join('generated', safe_filename)

    os.makedirs('generated', exist_ok=True)
    
    try:
        response = requests.get(image_url, timeout=4242)
    except requests.Timeout:
        download_image(image_url)
        return

    if response.status_code == 200:
        with open(file_path, 'wb') as image_file:
            image_file.write(response.content)
    else:
        download_image(image_url)
