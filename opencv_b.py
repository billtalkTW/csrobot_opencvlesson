import cv2

img = cv2.imread("H.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("robot", img_gray)
cv2.waitKey(0)