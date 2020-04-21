# move the file to the directory where images are stored
# pip install Pillow if you don't already have it

# import image utilities
from PIL import Image

# import os utilities
import os

# define a function that rotates images in the current directory
# given the rotation in degrees as a parameter


def rotateImages(rotationAmt):
    # for each image in the current directory
    for image in os.listdir(os.getcwd()):
        # open the image
        img = Image.open(image)
        # rotate and save the image with the same filename
        img.rotate(270).save(image)
        print('Rotating '+str(image))
        # close the image
        img.close()


# Calling the method.

rotateImages(270)
