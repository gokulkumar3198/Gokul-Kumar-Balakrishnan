import numpy as np
from PIL import Image

path = 'Galaxy_data/1.jpeg' #image path from root folder should be given
img = Image.open(path)
img1 = np.asarray(img)
thresh = np.sum(np.sum(img1)) / (img1.shape[0] * img1.shape[1] * img1.shape[2])
if thresh>104:
    print('Day')
else:
    print('Night')

