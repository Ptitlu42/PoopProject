import dropbox
from config import dropbox_token
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode

def drive_image(image_path):
    dbx = dropbox.Dropbox(dropbox_token)
    dropbox_path = f"/POOP/{image_path}"

    with open(image_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mute=True)

    link_metadata = dbx.sharing_create_shared_link_with_settings(dropbox_path)
    link = link_metadata.url

    parsed_link = urlparse(link)
    query = parse_qs(parsed_link.query)
    
    query['dl'] = '1'
    
    parsed_link = parsed_link._replace(query=urlencode(query, doseq=True))
    download_link = urlunparse(parsed_link)

    return download_link
