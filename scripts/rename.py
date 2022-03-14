import os 

# for fil in sorted(os.listdir('../yolodata/April2020_new/April2020_images_new')):
#     strippedfil = fil.strip('.jpg')
#     newfil = strippedfil.replace(strippedfil, strippedfil + '.txt')
#     if newfil not in sorted(os.listdir('../yolodata/April2020_new/April2020_txt_new')):
#         strippedfil2 = newfil.strip('.txt')
#         newfil2 = strippedfil2.replace(strippedfil2, strippedfil2 + '.jpg')
#         #print(os.getcwd())
#         os.remove("../yolodata/April2020_new/April2020_images_new/" + newfil2)

for fil in sorted(os.listdir('../yolodata/April2020_new/April2020_txt_new')):
    strippedfil = fil.strip(').txt')
    strippedfil1 = strippedfil.strip('Screenshot (')
    os.rename('../yolodata/April2020_new/April2020_txt_new/'+fil, '../yolodata/April2020_new/April2020_txt_new/April2020_'+strippedfil1+'.txt')