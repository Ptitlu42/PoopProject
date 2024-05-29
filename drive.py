import dropbox
from config import dropbox_token


def drive_image(image_path):
    dbx = dropbox.Dropbox(dropbox_token)
    dropbox_path = f"/POOP/{image_path}"

    with open(image_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mute=True)

    link = dbx.sharing_create_shared_link_with_settings(dropbox_path).url
    download_link = link.replace("?dl=0", "?dl=1")

    return download_link
