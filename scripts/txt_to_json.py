import os
import json
from pylabel import importer

#change to your paths, a folder with txt files and one with unannotated images should be placed in the same folder as the script
path_to_annotations = 'labels' 
path_to_images = 'multiple_videos' 
newdataset = 'newdataset2.json' #the name of the new file which will be created
yoloclasses = ['adult', 'chick', 'egg'] #list all classes in your dataset

scores = []

for filename in sorted(os.listdir(path_to_annotations)):
    print(filename)
    with open(path_to_annotations+ '/' + filename, 'r') as x:
        lines = x.readlines()
    
    newlist = []
    for i in lines:
        print(i)
        conf = i.split(' ',5)[5]
        conf = conf.strip('\n')
        scores.append(conf)
        conf = conf + '\n'
        if conf in i:
            i = i.replace(conf, '')
            newlist.append(i + '\n')

    with open(path_to_annotations+ '/' + filename, 'w') as x:
        for cdncd in newlist:
            x.write(cdncd)   

# Don't remove ../ from path_to_images
dataset = importer.ImportYoloV5(path=path_to_annotations, path_to_images='../'+path_to_images, cat_names=yoloclasses,
    img_ext="jpg", name=newdataset) 

dataset.export.ExportToCoco(newdataset)

with open(newdataset) as json_file:
    json_decoded = json.load(json_file)

anno_nr = 0

for annotations in json_decoded['annotations']:
    if annotations['id'] == anno_nr:
        annotations['score'] = float(scores[anno_nr])
    anno_nr += 1     

with open(newdataset, 'w') as json_file:
    json.dump(json_decoded, json_file)

file = open(newdataset, 'r')
addseg = json.load(file)
file.close()

for anno in addseg['annotations']:
    anno['segmentation'] = []
    bbox = anno['bbox']
    seg = []

    #topright
    seg.append(bbox[0]+bbox[2])
    seg.append(bbox[1])

    #bottomright
    seg.append(bbox[0]+bbox[2])
    seg.append(bbox[1]+bbox[3])

    #bottomleft
    seg.append(bbox[0])
    seg.append(bbox[1]+bbox[3])

    #topleft
    seg.append(bbox[0])
    seg.append(bbox[1])

    anno['segmentation'].append(seg)

file = open(newdataset, 'w')

json.dump(addseg, file, indent = 4)
file.close()


    