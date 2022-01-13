import cv2

img = cv2.imread("maze_car.png")
cv2.putText(img, "Bill Chuang", (318,376), cv2.FONT_HERSHEY_COMPLEX, 0.35, (0,255,150), 1)
cv2.imshow("robot", img)
cv2.waitKey(0)