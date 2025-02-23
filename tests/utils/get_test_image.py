from django.core.files.uploadedfile import SimpleUploadedFile
import os


def get_test_image():
    image_path = os.path.join(os.path.dirname(__file__), "test_image.png")
    with open(image_path, "rb") as img:
        return SimpleUploadedFile("test_image.png", img.read(), content_type="image/png")