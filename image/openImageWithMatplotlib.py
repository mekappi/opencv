import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C://Users/takasugi/Pictures/cat.JPG', 0)
plt.imshow(img, camp='gray', interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()