import matplotlib.pyplot as plt
import cv2
from mosaic import mosaic as mosaic

#make mosaic on pic
img = cv2.imread("cat.jpg")
mos_pic = mosaic(img, (50, 50, 450, 450), 10)

cv2.imwrite("cat-mosaic.png", mos_pic)
plt.imshow(cv2.cvtColor(mos, cv2.COLOR_BGR2RGB))
plt.show()
