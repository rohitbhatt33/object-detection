import cv2
import numpy as np
path = "img/py.jpg"
img = cv2.imread(path)


width, height, _ = img.shape

cv2.rectangle(img, (385, 155), (851, 613), (0, 255, 0), 3)
roi = img[155:543, 613:1326]

cv2.imshow("sc", roi)
cv2.waitKey(0)
