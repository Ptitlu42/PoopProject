import os
import requests

def download_image(image_url):
    filename = image_url.split('?')[0].split('/')[-1]
    filename_parts = filename.split(':')
    filename_parts[0] = filename_parts[0].replace('/', '_')
    filename_parts[0] = filename_parts[0].replace('?', '_')
    filename_parts[0] = filename_parts[0].replace('&', '_')
    filename_parts[0] = filename_parts[0] + ".jpg"
    safe_filename = '_'.join(filename_parts)
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
