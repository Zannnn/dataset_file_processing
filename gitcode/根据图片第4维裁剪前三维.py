import os
import numpy as np
from PIL import Image

path = r'/pub/data/lz/DeepLabV3Plus-Pytorch/datasets/data/VOCdevkit/VOC2012/JPEGImages8'
newpath = r'/pub/data/lz/DeepLabV3Plus-Pytorch/datasets/data/VOCdevkit/VOC2012/JPEGImages'


def picture(path):
    files = os.listdir(path)
    for file in files:
        filepath = os.path.join(path, file)
        img = Image.open(filepath)
        img = np.array(img)
        for i in range(3):
            img[:,:,i] = np.multiply(img[:,:,i],img[:,:,3]/255)
        img = img[:,:,0:3]
        img = Image.fromarray(img)

        dirpath = newpath
        file_name, file_extend = os.path.splitext(file)
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.jpg') #不创建文件夹，自己先创建好
        img.save(dst)


picture(path)
