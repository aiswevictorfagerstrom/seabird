from pylabel import importer

path_to_annotations = 'AnnotationApril2020/annoteringar_xml' 
path_to_images = 'bilder2' 

# List all classes in your dataset
yoloclasses = ['AdultBird', 'Chick', 'Egg', 'Leaving', 'Flapping', 'Incoming']

# Don't remove ../ from path_to_images
dataset = importer.ImportVOC(path=path_to_annotations, path_to_images='../'+path_to_images, 
     name="AnnotationsApril2020YOLO") 

# Change to the name you want your new file to have
dataset.export.ExportToYoloV5('AnnotationsApril2020YOLO')