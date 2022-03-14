import os

f = open("lysekilpaths_test_labels.txt", "a")
f1 = open("lysekilpaths_train_labels.txt", "a")

x=0

for fil in sorted(os.listdir('annotated_in_lysekil_labels')):
    if x < 400:
        f.write("/baltic_seabird/images/"+fil+'\n')
    else:
        f1.write("/baltic_seabird/images/"+fil+'\n')
    
    print(str(x)+"/baltic_seabird/images/"+fil)
    x+=1

f.close()
f1.close()
