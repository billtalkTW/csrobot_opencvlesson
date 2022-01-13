import cv2

img = cv2.imread("maze_car.png")
img_cut = img[ 0:375 , 0:375 ]
cv2.imshow("robot", img_cut)
cv2.waitKey(0)