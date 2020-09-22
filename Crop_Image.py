import cv2
import numpy as np
resim=cv2.imread("lena.jpg")
cv2.imshow("Resim",resim)
a,b,c=resim.shape
kirpma=np.zeros((a,b),dtype="uint8")
for i in range(0,a):
    for j in range(0,b):
        kesilen=resim[200:i-100,200:j-100]
       
cv2.imshow("CropImage",kesilen)
cv2.waitKey(0)
cv2.destroyAllWindows()