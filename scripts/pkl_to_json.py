from __future__ import annotations
import pickle
import os
import json

#file where json object will be saved
file_path = 'dataset1.json'

# dictionary in the json-format necessary for coco-annotation tool. 
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

# sorting variables
image_nr = 0
annotation_id = 0
annotation_list = 0

file = open('dataset123.json', 'r')
timbuktu = json.load(file)
file.close()
        
directory = 'output'


# loop through all output files from detectron2 (.pkl)
for fille in sorted(os.listdir(directory)):
    with open('output/' + fille, 'rb') as f:
        data = pickle.load(f)
        
        # dictionary made for the image section in the jsonfile
        dict1 = {
            'id': image_nr,
            "folder": "../img2",
            "file_name": timbuktu['images'][image_nr]['file_name'],
            "width": 1920,
            "height": 1080,
            "depth": 3,
        }

        dict['images'].append(dict1)

        for image in data['pred_boxes']:
            width_bbox = dict1['width'] - (data['pred_boxes'][annotation_list][0] + (dict1['width'] - data['pred_boxes'][annotation_list][2]))
            height_bbox = dict1['height'] - (data['pred_boxes'][annotation_list][1] + (dict1['height'] - data['pred_boxes'][annotation_list][3]))

            # dictionary made for the annotation part of the jsonfile 
            dict2 = {
                "image_id": image_nr,
                "id": annotation_id,
                "bbox": [],
                "area": float(width_bbox * height_bbox),
                "segmentation": [],
                "iscrowd": 0,
                "category_id": int(data['pred_classes'][annotation_list])
            }

            seg = []

            # add bboxes to the annotation section
            dict2['bbox'].append(float(data['pred_boxes'][annotation_list][0]))
            dict2['bbox'].append(float(data['pred_boxes'][annotation_list][1]))
            dict2['bbox'].append(float(width_bbox))
            dict2['bbox'].append(float(height_bbox))

            #tr
            seg.append(float(data['pred_boxes'][annotation_list][2]))
            seg.append(float(data['pred_boxes'][annotation_list][1]))

            # #br
            seg.append(float(data['pred_boxes'][annotation_list][2]))
            seg.append(float(data['pred_boxes'][annotation_list][3]))

            #bl
            seg.append(float(data['pred_boxes'][annotation_list][0]))
            seg.append(float(data['pred_boxes'][annotation_list][3]))

            #tl
            seg.append(float(data['pred_boxes'][annotation_list][0]))
            seg.append(float(data['pred_boxes'][annotation_list][1]))

            dict2['segmentation'].append(seg)

            dict['annotations'].append(dict2)
            

            annotation_id += 1
            annotation_list += 1

    
        annotation_list = 0
    image_nr += 1


newfile = open(file_path, 'w')

json.dump(dict, newfile, indent = 4)
newfile.close()
