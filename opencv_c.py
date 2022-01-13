import cv2

img = cv2.imread("H.jpg")
img_blur = cv2.GaussianBlur(img, (15,15), 0)
cv2.imshow("robot", img_blur)
cv2.waitKey(0)