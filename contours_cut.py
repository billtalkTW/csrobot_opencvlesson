from typing import Counter
import cv2

img = cv2.imread('image_l.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 1

# 畫書第i個輪廓
draw_img = cv2.drawContours(img.copy(),contours,i,(0,255,0),3) 
cv2.imshow("draw_contour_img", draw_img)

# 找出第i個矩形輪廓的起點座標(左上角)的 x,y ，以及矩形寬高的 w,h
ct_x, ct_y, ct_w, ct_h = cv2.boundingRect(contours[i])
print ("contour x：",ct_x)
print ("contour y：",ct_y)
print ("contour w：",ct_w)
print ("contour h：",ct_h)

# 找出第i個矩形輪廓的面積資訊，其中第三項為輪廓的「角度」
ct_area = cv2.minAreaRect(contours[i])
print ("contour area：",ct_area)
ct_angle = ct_area[2]
print("contour angle : ",ct_angle)
if ct_angle == 90:
    ct_angle = 0

# 依照矩形輪廓進行裁切
new_img = img.copy()[ct_y:ct_y+ct_h, ct_x:ct_x+ct_w]
cv2.imshow("new_image", new_img)
cv2.imwrite("new_img.jpg", new_img)
# 依照輪廓角度進行旋轉
new_h, new_w, new_d = new_img.shape #讀取圖片大小
new_center = (new_w//2, new_h//2) #找出圖片中心
#製作旋轉矩陣
#第一個參數旋轉中心，第二個參數旋轉角度(-順時針/+逆時針)，第三個參數縮放比例
rotate_martix = cv2.getRotationMatrix2D(new_center, ct_angle, 1.0)
print("rotate matrix : ", rotate_martix)
#製作旋轉後的圖片，第三個參數為變化後的圖片大小
rotate_img = cv2.warpAffine(new_img, rotate_martix, (new_w, new_h))
cv2.imshow("rotate_image", rotate_img)
cv2.waitKey(0)