# from unittest import skip
# import cv2
# import os
# import time
# from numpy import random

# frames = 100 # how many random frames
# length = 5000 # video length (sec)
# fps = 60 # fps
# path = 'Bonden5_20200516_035844' # path to video 
# newpath = 'Frames_for_lysekil' # path to directory with new images

# totalframes = fps * length
# x = 0

# # Read the video from specified path
# cam = cv2.VideoCapture(path)

# try:
#     # creating a folder named data
#     if not os.path.exists(newpath):
#         os.makedirs(newpath)
#     # if not created then raise error
# except OSError:
#     print('Error: Creating directory of data')

# while (x < frames):
#     currentFrame = random.randint(totalframes)
#     cam.set(1, currentFrame)
#     ret, frame = cam.read()
#     try:
#         cv2.imwrite(newpath + "/" + str(currentFrame) + '.jpg', frame)
#         print(currentFrame)
#         x += 1
#     except: 
#         continue

    

# cam.release()
# cv2.destroyAllWindows()

import cv2
import os
import time
from numpy import random
frames = 100 # how many random frames
# length = 2 * 60 * 60
length = 2 * 60 * 60 + 15 * 60 + 48  # video length (sec)
fps = 60 # fps
path = 'ROST3_20210618_155324.avi' # path to video
newpath = 'Frames_for_Lysekil' # path to directory with new images
totalframes = fps * length
x = 0
# Read the video from specified path
cam = cv2.VideoCapture(path)
try:
    # creating a folder named data
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')
while (x < frames):
    currentFrame = random.randint(totalframes)
    cam.set(1, currentFrame)
    ret, frame = cam.read()
    try:
        cv2.imwrite(newpath + "/" + str(currentFrame) + '.jpg', frame)
        print(currentFrame)
        x += 1
    except:
        continue
cam.release()