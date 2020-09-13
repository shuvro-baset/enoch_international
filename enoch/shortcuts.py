import os


def product_image_upload_path(instance, file_name):
    return os.path.join("product_images", str(instance.id)+'_'+file_name)
