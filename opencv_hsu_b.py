import cv2

img = cv2.imread("new_img.jpg")
height = img.shape[0]
width = img.shape[1]

cv2.circle(img, ((width//2),(height//2)-20), 3, (0,0,255), 3)
point1 = img[(height//2)-20,(width//2)]
print("point1: "+str(point1))
cv2.circle(img, ((width//2),(height//2)-2), 3, (0,0,255), 3)
point2 = img[(height//2)-2,(width//2)]
print("point2: "+str(point2))
cv2.circle(img, ((width//2),(height//2)+20), 3, (0,0,255), 3)
point3 = img[(height//2)+20,(width//2)]
print("point3: "+str(point3))


if max(point1) < max(point2) and max(point1) < max(point3) :
    hsu = "S"
elif max(point2) < max(point1) and max(point2) < max(point3) :
    hsu = "H"
elif max(point3) < max(point1) and max(point3) < max(point2) :
    hsu = "U"
else :
    hsu = "error"

print("This image is '" + hsu + ".jpg'" )
cv2.imshow(hsu, img)
cv2.waitKey(0)