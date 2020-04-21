# Improting Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open("data/frame1.jpg")

# Setting the points for cropped image
left = 155
top = 65
right = 360
bottom = 270

# Cropped image of above dimension
# (It will not change orginal image)
im1 = im.crop((left, top, right, bottom))

# Shows the image in image viewer
im1.show()
im.show()
