import json

def transformer(jfile):
        
    file = open(jfile, 'r')
    x = json.load(file)
    file.close()

    for anno in x['annotations']:
        anno['segmentation'] = []
        bbox = anno['bbox']
        seg = []

        # topright
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

        print(seg)

    file = open(jfile, 'w')
    
    json.dump(x, file, indent = 4)
    file.close()

        
# Change to your json file
transformer('xml.json')

# import json
# import os

# def transformer(jfile):
        
#     file = open(jfile, 'r')
#     x = json.load(file)
#     file.close()

#     for anno in x['annotations']:
#         anno['segmentation'] = []
#         bbox = anno['bbox']
#         seg = []

#         # topright
#         seg.append(bbox[0]+bbox[2])
#         seg.append(bbox[1])

#         #bottomright
#         seg.append(bbox[0]+bbox[2])
#         seg.append(bbox[1]+bbox[3])

#         #bottomleft
#         seg.append(bbox[0])
#         seg.append(bbox[1]+bbox[3])

#         #topleft
#         seg.append(bbox[0])
#         seg.append(bbox[1])

#         anno['segmentation'].append(seg)

#         print(seg)

#     annonr = 0

#     # iterates through files in folder and read every line
#     for filename in os.listdir('labels'):
#         textfile = open('labels/' + filename, 'r')
#         lines = textfile.readlines()

#         # finds the confidence of every annotation
#         for i in lines:
#             conf = i.split(' ',5)[5]
#             conf = conf.strip('\n')

#             #conf = all confidences 
#             #add "score" to json object 
#             for annotations in x['annotations']:
#                 if annotations['id'] == annonr:
#                     annotations['score'] = float(conf)
#             annonr += 1    

#     file = open(jfile, 'w')
    
#     json.dump(x, file, indent = 4)
#     file.close()

        
# # Change to your json file
# transformer('dataset123.json')