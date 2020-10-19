"""Target format should be .png
"""

import os
from PIL import Image

# Input the original image format (eg. jpg, bmp)
format = ".jpg"

# Input the path of image folder
path = "/home/jiahui/codes/image/"
save_path = "/home/jiahui/codes/image/cvted/"

dirs = os.listdir(path + ".")

def image_converter(file):
    """Convert image into .jpg and saved into folder 'converted_files'.

    Args:
        file: File name of original image.
    """
    im = Image.open(path + file)
    rgb_im = im.convert('RGB')
    rgb_im.save(os.path.join(save_path,str(os.path.splitext(file)[0]) + '.png'))
    rgb_im.close()
    os.remove(path + file)


if __name__ == "__main__":
    for file in dirs:
        if os.path.splitext(file)[1] == format:
            image_converter(file)