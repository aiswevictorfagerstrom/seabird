import os
import json

# open json file and save it in variable
with open('dataset.json') as json_file:
    json_decoded = json.load(json_file)

annonr = 0 

# iterates through files in folder and read every line
for filename in sorted(os.listdir('labels')):
    x = open('labels/' + filename, 'r')
    lines = x.readlines()

    # finds the confidence of every annotation
    for i in lines:
        conf = i.split(' ',5)[5]
        conf = conf.strip('\n')


        #conf = all confidences 
        #add "score" to json object 
        for annotations in json_decoded['annotations']:
            if annotations['id'] == annonr:
                annotations['score'] = float(conf)
        annonr += 1     


# writes the updated json file to the original
with open('dataset123.json', 'w') as json_file:
    json.dump(json_decoded, json_file)
