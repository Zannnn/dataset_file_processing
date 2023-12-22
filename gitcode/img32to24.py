import os

from PIL import Image

path = r'D:\\task\\paper\\ReadPaper\\others\\code\\deocclusion-master\\demos\\outputs\\occlusion_dataset\\COI32'
newpath = r'D:\\task\\paper\\ReadPaper\\others\\code\\deocclusion-master\\demos\\outputs\\occlusion_dataset\\COI'


def picture(path):
    files = os.listdir(path)
    for i in files:
        files = os.path.join(path, i)
        img = Image.open(files).convert('RGB')
        dirpath = newpath
        file_name, file_extend = os.path.splitext(i)
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.jpg')
        img.save(dst)


picture(path)