import numpy as np
import cv2
ph1 = cv2.imread('img.jpg')
dis1 = cv2.imread('imgg.jpg')
ph = cv2.resize(ph1,(1000,700) ,interpolation= cv2.INTER_LINEAR)
dis = cv2.resize(dis1,(600,500), interpolation= cv2.INTER_LINEAR)
phg= cv2.cvtColor(ph, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(phg, 149, 255, cv2.THRESH_BINARY)
cont, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
l = [0,0,0,0] # "triangle,square,rectangle,circle"
for i in cont:
    approx = cv2.approxPolyDP(i, 0.01* cv2.arcLength(i, True), True)
    area = cv2.contourArea(i)
    #cv2.drawContours(ph, [i], 0, (100,13,45), 8)
    if 4000 < area < 80000:
        if len(approx) == 3:
            l[0]+=1
        
        elif len(approx) == 4:
            
            x1 ,y1, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w)/h
            if aspectRatio >= 0.8 and aspectRatio <= 1.2:
                l[1]+=1

            else:
                l[2]+=1

        else:
            l[3]+=1

cv2.putText(dis, f"{l[3]}", (100, 90), cv2.FONT_HERSHEY_COMPLEX, 2, color=(0,0, 255),thickness=3)
cv2.putText(dis, f"{l[0]}", (100, 220), cv2.FONT_HERSHEY_COMPLEX, 2, color=(0,0, 255),thickness=3)
cv2.putText(dis, f"{l[2]}", (100, 310), cv2.FONT_HERSHEY_COMPLEX, 2, color=(0,0, 255),thickness=3)
cv2.putText(dis, f"{l[1]}", (100, 430), cv2.FONT_HERSHEY_COMPLEX, 2, color=(0,0, 255),thickness=3)
cv2.imshow("imgg", dis)
cv2.waitKey(0)
cv2.destroyAllWindows()
