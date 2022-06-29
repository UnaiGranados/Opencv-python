import cv2
import numpy as np

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:

        circles[counter] = x,y
        counter += counter
        print(circles)

img = cv2.imread('Resources/cards.jpg')
w,h = 640,480

dim = (w, h)
img_r = cv2.resize(img, dim)

p1 = [58,74] #high left point
p2 = [173,97] #high right point
p3 = [36,163] #down left point
p4 = [167,181] #down right point
points1 = np.float32([p1,p2,p3,p4])

cv2.circle(img,p1,3,(255,0,0),cv2.FILLED)
cv2.circle(img,p2,3,(0,255,0),cv2.FILLED)
cv2.circle(img,p3,3,(0,0,255),cv2.FILLED)
cv2.circle(img,p4,3,(7,242,221),cv2.FILLED)

width,height = 272,181
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(points1,points2)
output = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Original image",img)
cv2.imshow("Output image:",output)
#cv2.imshow("Resized image",img_r)
cv2.waitKey(0)


frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    successs,img = cap.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
