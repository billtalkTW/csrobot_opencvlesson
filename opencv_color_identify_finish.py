import cv2

img = cv2.imread("color_circle.jpg")
print("image size:")
print(img.shape)


cv2.circle(img, (180, 80), 7, (0,0,0), 12)
pointA_color = img[(180, 80)]
print("color of the point a:")
print(pointA_color)

cv2.circle(img, (100, 400), 7, (0,0,0), 12)
pointB_color = img[(100, 400)]
print("color of the point b:")
print(pointB_color)

cv2.circle(img, (275, 210), 7, (0,0,0), 12)
pointC_color = img[(275, 210)]
print("color of the point c:")
print(pointC_color)

cv2.circle(img, (405, 450), 7, (0,0,0), 12)
pointD_color = img[(405, 450)]
print("color of the point d:")
print(pointD_color)

cv2.imshow("color_identify", img)
cv2.waitKey(0)