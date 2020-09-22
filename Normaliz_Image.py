import cv2
import numpy as np
img = cv2.imread('peppers.png',0)
norm_img = np.zeros((800,800))
final_img = cv2.normalize(img,  norm_img, 0, 100, cv2.NORM_MINMAX)
cv2.imshow('Original',img)
cv2.imshow('Normalized Image', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()