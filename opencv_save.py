import cv2

img = cv2.imread("maze_car.png")

cv2.imwrite("car_img.jpg", img)

cv2.imshow("robot", img)
cv2.waitKey(0)