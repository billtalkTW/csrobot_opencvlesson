import cv2

img = cv2.imread("maze_car.png")
cv2.imshow("robot", img)
cv2.waitKey(0)