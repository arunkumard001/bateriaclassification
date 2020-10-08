#preprocessing
import os
import cv2
import numpy as np
import scipy.io as sc

def create_dataset(IMG_SIZE=128,DATA_DIR="data/"):
    output_file="data/dataset.mat"
    if os.path.exists(output_file):
         os.remove(output_file)
    img_dirs=os.listdir(DATA_DIR)
    labels=np.ndarray([])
    dataset=np.ndarray([])
    CLASSES=0
    CLASSNAMES=[]
    for classname in img_dirs:
        print('================\nCLASS:"+classname+"\n==============')
        if os.path.isfile(DATA_DIR+ classname):
            continue
        files = os.listdir(DATA_DIR+ classname)
        fileCount=0
        for file_name in files:
            fileCount=fileCount+1
            img_file = DATA_DIR +classname +"/" +file_name
            print(fileCount,file_name)
            img=cv2.imread(img_file)
            img=cv2.resize(img(IMG_SIZE,IMG_SIZE))
            img= cv2.normalize(img.astype("float"),None,0.0,1.0,cv2.NORM_MINMAX)
            img =np.reshape(img,(1,img.shape[0],img.shape[1],img.shape[2]))
            if dataset.shape==():
                dataset=img
                labels=CLASSES
            else:
                dataset=np.concatenate((dataset,img),axis=0)
                labels=np.append(labels,CLASSES)
        CLASSNAMES.append(classname)
        CLASSES=CLASSES+1
    sc.savemat(output_file,mdict={"dataset":dataset,"labels":labels,"CLASSES":CLASSES,"CLASSNAMES":CLASSNAMES},oned_as="row")
    print("=============")
    print("Dataset created:",dataset.shape)