from pylabel import importer


path_to_annotations = 'halflysekiljoakim-2.json' 
path_to_images = '../bildertilljocke' 


# List all classes in your dataset
yoloclasses = ['adult', 'chick', 'egg']

# Don't remove ../ from path_to_images
dataset = importer.ImportCoco(path=path_to_annotations, path_to_images=path_to_images, name="yolojoakim_lyse") 

# cat_names=yoloclasses, img_ext="jpg",

# Change to the name you want your new file to have
dataset.export.ExportToYoloV5('yolojoakim_lyse')
