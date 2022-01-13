import cv2

img = cv2.imread("S.jpg")
height = img.shape[0]
width = img.shape[1]

cv2.circle(img, (600,400), 7, (255,255,0), 12)
point1 = img[(400,600)]
print("point1: "+str(point1))
cv2.circle(img, (600,600), 7, (255,255,0), 12)
point2 = img[(600,600)]
print("point2: "+str(point2))
cv2.circle(img, (600,800), 7, (255,255,0), 12)
point3 = img[(800,600)]
print("point3: "+str(point3))

if 0 in point1 :
    hsu = "S"
elif 0 in point2 :
    hsu = "H"
elif 0 in point3 :
    hsu = "U"
else :
    hsu = "error"

print("This image is '" + hsu + ".jpg'" )
cv2.imshow(hsu, img)
cv2.waitKey(0)