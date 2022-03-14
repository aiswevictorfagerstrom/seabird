import numpy as np
import cv2
import glob
import os
from PIL import Image


# for img in glob.glob('images'+'/*.jpg'):

# 	read = cv2.imread(img)

# 	cropped_image = read[0:40, 0:400]

# 	newstr = img.replace('images/', '')	

# 	#cv2.imwrite('cropped/' + newstr, cropped_image)

# for img2 in glob.glob('images2'+'/*.jpg'):

# 	read2 = cv2.imread(img2)

# 	dim = (960, 540)

# 	resized = cv2.resize(read2, dim, interpolation = cv2.INTER_AREA)

# 	print(read.shape)

# 	cropped_image2 = resized[0:40, 0:400]

# 	newstr2 = img2.replace('images2/', '')	

# 	#cv2.imwrite('cropped2/' + newstr2, cropped_image2)




for newimg in glob.glob('cropped'+'/*.jpg'):
	
	pillow = Image.open(newimg)

	image_array = np.array(pillow)

	for newimg2 in glob.glob('cropped2'+'/*.jpg'):

		pillow2 = Image.open(newimg2)

		image_array2 = np.array(pillow2)

		# print(image_array[0][0], image_array2[0][0])

		# print('--------------------')

		if (image_array == image_array2).all():
			
			print(newimg2, newimg)


# print(image_array[0])