import os
from PIL import Image

# Input the original image format
format = ".bmp"

# Input the path of image folder
path = "/home/jiahui/codes/image/"

dirs = os.listdir(path + ".")

def image_converter(fmt):
    """Convert image into .jpg.

    Args:
        fmt: The format of original image.

    Returns:
        Image without any specific format.
    """

    im = Image.open(str(os.path.splitext(file)[0]) + fmt)
    rgb_im = im.convert('RGB')
    im.close()
    return rgb_im


for file in dirs:
    if os.path.splitext(file)[1] == format:
        image_converter(format).save(str(os.path.splitext(file)[0]) + '.jpg')
        os.remove(str(os.path.splitext(file)[0]) + format) # Remove original file.