from typing import Counter
import cv2

# 讀取image，並命名為img
img = cv2.imread('hsu_contours_test.png')
# 將image灰階化，並命名為gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 將gray圖片二值化，並存入變數陣列binary中
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# 利用二值化的變數來找出輪廓，並存入變數陣列contours中
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 在img上繪出第n個輪廓(-1則為全部輪廓)
draw_img = cv2.drawContours(img,contours,-1,(0,0,255),3)  
# 顯示最終結果
print ("contours 數量：",len(contours))
cv2.imshow("draw_contours", draw_img)
cv2.waitKey(0)