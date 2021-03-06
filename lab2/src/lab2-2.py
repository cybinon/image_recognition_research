import cv2 #OpenCV 
import numpy as np
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = "./lab2/rose.tif"

image = cv2.imread(file_path);
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY);

ogImage = cv2.resize(image, [300,300]);
cv2.imshow("Original", ogImage);

down = [
  [128,128],
  [64,64],
  [32,32]
]

plt.figure();
j=1

for i in down:
  nearest_resize = cv2.resize(ogImage, i, interpolation=cv2.INTER_NEAREST);
  pic_plot = plt.subplot(3,3,j);
  pic_plot.imshow(nearest_resize);

  linear_resize = cv2.resize(ogImage, i, interpolation=cv2.INTER_LINEAR);
  pic_plot = plt.subplot(3,3,j+3);
  pic_plot.imshow(linear_resize);
  j+=1;

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


