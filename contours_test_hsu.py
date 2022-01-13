from typing import Counter
import cv2

img = cv2.imread('hsu_contours_test.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)-1):
    if( i % 2 == 0):
        draw_img = cv2.drawContours(img,contours,i,(0,0,255),3)  

print ("contours 數量：",len(contours))
cv2.imshow("find_hsu_contours", draw_img)
cv2.waitKey(0)