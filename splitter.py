import cv2
import numpy as np
import os

# place the movie name below,dont forget to mention the movie format also
video = cv2.VideoCapture('moviename.mov')

# before running the code sample make a file called 'data' in the same directory
try:
    if not os.path.exists('data'):
        os.mkdir('data')
except OSError:
    print('Error : Creating folder to save images')

# removing garbage values
currentframe = 0
total = 0
total = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print('Total Number of Frames in the Video :' + str(total))

# saving the images
while currentframe <= total:
    ret, frame = video.read()
    name = './data/frame' + str(currentframe) + '.jpg'
    print('creating ' + name)
    cv2.imwrite(name, frame)
    currentframe += 1


video.release()
cv2.destroyAllWindows()
