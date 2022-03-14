import json
import os
import numpy as np

# load json files with annotations from d2 and yolov5
d2file = open('newlabels.json', 'r')
yolofile = open('newdataset1.json', 'r') 
d2dict = json.load(d2file)
yolodict = json.load(yolofile)

# path to json file with new annotations
newpath = 'newannotations.json'

# variables
distanceallowed = 120 # smaller value requires more exact incoming annotations from the models 
numberofannotations = 0

# creates the new dictionary and append images and categories from the yolo file to the new dictionary
dict = {
    'images': [],
    'annotations': [],
    'categories': [
        {
            "id": 0,
            "name": "adult"
        },
        {
            "id": 1,
            "name": "chick"
        },
        {
            "id": 2,
            "name": "egg"
        }
    ]
}

# loops through all images in the dictionary
for image in yolodict['images']:
    for yoloanno in yolodict['annotations']:
        if yoloanno['image_id'] == image['id']:
            yolosegmentation = [yoloanno['segmentation'][0][6], yoloanno['segmentation'][0][7], yoloanno['segmentation'][0][2], yoloanno['segmentation'][0][3]] # tlx, tly, brx, bry
            for d2anno in d2dict['annotations']:
                if d2anno['image_id'] == image['id']:
                    d2segmentation = [d2anno['segmentation'][0][6], d2anno['segmentation'][0][7], d2anno['segmentation'][0][2], d2anno['segmentation'][0][3]] # tlx, tly, brx, bry

                    # checks the distance between annotations from different models
                    if abs(yolosegmentation[0] - d2segmentation[0]) < distanceallowed and abs(yolosegmentation[1] - d2segmentation[1]) < distanceallowed: # checks if the difference between the top left values are small enough
                        if abs(yolosegmentation[2] - d2segmentation[2]) < distanceallowed and abs(yolosegmentation[3] - d2segmentation[3]) < distanceallowed: # checks if the difference between the bottom right values are small enough
                            
                            # calculates the new annotation values, using weighted arithmetic mean
                            tlx = float((yolosegmentation[0] * yoloanno['score'] + d2segmentation[0] * d2anno['score']) / (yoloanno['score'] + d2anno['score']))
                            tly = float((yolosegmentation[1] * yoloanno['score'] + d2segmentation[1] * d2anno['score']) / (yoloanno['score'] + d2anno['score']))
                            brx = float((yolosegmentation[2] * yoloanno['score'] + d2segmentation[2] * d2anno['score']) / (yoloanno['score'] + d2anno['score']))
                            bry = float((yolosegmentation[3] * yoloanno['score'] + d2segmentation[3] * d2anno['score']) / (yoloanno['score'] + d2anno['score']))
                            newscore = float((yoloanno['score'] * yoloanno['score'] + d2anno['score'] * d2anno['score']) / (yoloanno['score'] + d2anno['score']))

                            width = float(image['width'] - (tlx + (image['width'] - brx)))
                            height = float(image['height'] - (tly + (image['height'] - bry)))

                            # creates dictionary for every annotation and appends to the main dictionary
                            dictanno = {
                                "image_id": d2anno['image_id'],
                                "id": int(d2anno['id']),
                                "bbox": [tlx, tly, width, height],
                                "area": float(width * height),
                                "segmentation": [
                                    [
                                        brx,
                                        tly,
                                        brx,
                                        bry,
                                        tlx,
                                        bry,
                                        tlx,
                                        tly
                                    ]                         
                                ],
                                "iscrowd": 0,
                                "category_id": int(d2anno['category_id']),
                                "score": float(newscore)
                            }
                            dict['annotations'].append(dictanno)
                            numberofannotations += 1

    # creates dictionary for every image and appends to main dictionary
    dictimage = {
        'id': image['id'],
        "folder": "../multiple_videos",
        "file_name": image['file_name'],
        "width": 1920,
        "height": 1080,
        "depth": 3,
    }
    dict['images'].append(dictimage)

print("Done, total amount of annotations: " + str(numberofannotations))    

# writes over to the new json file
newlabels = open(newpath, 'w')
json.dump(dict, newlabels, indent = 4)
newlabels.close()
