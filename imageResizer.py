from PIL import Image


def resize_image(size1, size2):
    image = Image.open('my_photo.jpg')
    print(f"Current size: {image.size}")

    resized_image = image.resize((size1, size2))
    resized_image.save("my_new_photo.jpg")


size1 = int(input("Enter width: "))
size2 = int(input("Enter length: "))
resize_image(size1, size2)