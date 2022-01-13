import cv2

img = cv2.imread("maze_car.png")
cv2.circle(img, (270,210), 40, (255,0,0), 3)
cv2.imshow("robot", img)
cv2.waitKey(0)