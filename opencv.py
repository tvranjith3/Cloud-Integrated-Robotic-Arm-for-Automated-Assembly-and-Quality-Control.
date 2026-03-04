import cv2
import numpy as np

img = cv2.imread("rust.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([5,100,100])
upper = np.array([20,255,255])

mask = cv2.inRange(hsv, lower, upper)

contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Rust Detection", img)
cv2.waitKey(0)