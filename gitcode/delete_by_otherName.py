import os

from PIL import Image

SourcePath = r'D:\\task\\paper\\ReadPaper\\others\\code\\deocclusion-master\\demos\\outputs\\occlusion_dataset_simplify_now\\background'
DealPath = r'D:\\task\\paper\\ReadPaper\\others\\code\\deocclusion-master\\demos\\outputs\\occlusion_dataset_simplify_now\\mask_cut'


def picture(SourcePath,DealPath):
    sfiles = os.listdir(SourcePath)
    dfiles = os.listdir(DealPath)
    j = 0
    for i in dfiles:       
        if i != sfiles[j]:
            files = os.path.join(DealPath, i)
            os.remove(files)
            print("delete"+ files)
        else:
            j = j + 1




picture(SourcePath,DealPath)