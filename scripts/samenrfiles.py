import os 

txtfiles = sorted(os.listdir('../../../yolov5/runs/detect/test/labels'))

# for txtfile in txtfiles:
#     print(txtfile)

for imgfile in sorted(os.listdir('../Frames_for_Lysekil_copy')):
    if '.jpg' in imgfile:
        strippedfile = imgfile.strip('.jpg')
        newfile = strippedfile+'.txt'
        if newfile not in txtfiles:
            os.remove('../Frames_for_Lysekil_copy/'+imgfile)
            print(imgfile)
    
            

    