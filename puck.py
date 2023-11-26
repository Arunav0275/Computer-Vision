import cvzone
import cv2
import numpy as np
import matplotlib.pyplot as plt

from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=1)



while True:
    success, frame = cap.read()
    img=cv2.imread('donut.jpg',1)
   

    

    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame, flipType=False)

    puck=cv2.circle(frame,(200,300),20,(200,0,200),-1)
    
    initial_puck_velocity = [10, 10] 
    puck_velocity = initial_puck_velocity.copy()

    np.put(frame, np.random.choice(range(1440*1080),5, replace=False),img)


    

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        cv2.circle(frame, pointIndex,30, (0,0,200),-1)
    cv2.imshow('frame',frame)
    
    
    
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


