import cv2
image=cv2.imread('peppers.png')
R=image[:,:,2]
G=image[:,:,1]
B=image[:,:,0]
cv2.imshow('Original',image)
cv2.imshow('Red',R)
cv2.imshow('Green',G)
cv2.imshow('Blue',B)
cv2.waitKey()
cv2.destroyAllWindows()