import os

for file in os.listdir('yolojoakim_lyse copy/'):

    print(file)

    with open('yolojoakim_lyse copy/' + file, 'r') as x:
        lines = x.readlines()



    
    zyz = 0

    for i in lines:
        conf = i.split(' ',4)[0]

        
        i = i[1:]
        print(i)

        conf = int(conf)-1
        conf = str(conf)


        i = conf + i

        lines[zyz] = i

        zyz+=1

    print(lines)

    

    with open('yolojoakim_lyse copy/' + file, "w") as x:
        x.writelines(lines)

        
        
        