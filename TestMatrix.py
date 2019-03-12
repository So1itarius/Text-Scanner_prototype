import numpy as np
from PIL import Image

img = Image.open('ans.jpg')
arr = np.array(img)  # 640x480x4 array

print(list(img.getdata()[123]))
