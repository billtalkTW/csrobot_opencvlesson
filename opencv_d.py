import cv2

img = cv2.imread("maze_car.png")
print(img.shape)
height = img.shape[0]
width = img.shape[1]
img_resize = cv2.resize(img, (width*3 , height*2) )
cv2.imshow("robot", img_resize)
cv2.waitKey(0)