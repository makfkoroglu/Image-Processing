import cv2
import numpy as np
resim=cv2.imread("lena.jpg")
a,b,c=resim.shape
print(a,b)
sifirmatris=np.zeros((a,b,c),dtype="uint8")
print(sifirmatris.shape)
for i in range(1,a-1):
    for j in range(1,b-1):
        sifirmatris[i+1,j+1]=resim[i+1,b-j]
        
cv2.imshow("Sonuc",sifirmatris)
cv2.imshow("Orijinal",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()