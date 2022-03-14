from PIL import Image
import os

for file in os.listdir('AnnotationApril2020/bilder'):
    
    im1 = Image.open('AnnotationApril2020/bilder/' + file)

    im1 = im1.convert('RGB')

    filename = file.strip('.png')

    # filename1 = filename.strip(' ')

    newfilename = filename.replace(filename, filename + '.jpg')

    print(newfilename)

    im1.save('AnnotationApril2020/bilder2/' + newfilename)