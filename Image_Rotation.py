import cv2
import numpy as np
resim=cv2.imread("lena.jpg")
a,b,c=resim.shape
print(a,b)
sifirmatris=np.zeros((b,a,c),dtype="uint8")
print(sifirmatris.shape)
for i in range(0,a):
    for j in range(0,b):
        sifirmatris[i,j]=resim[a-j-1,b-i-1]
        
cv2.imshow("Sonuc",sifirmatris)
cv2.imshow("Orijinal",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()