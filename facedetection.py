import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('frontalface.xml')

cap = cv2.VideoCapture(0)

while(True):
    #비디오 프레임 읽어오기(ret: true, false / frame : 프레임 읽어옴)
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #표현할 이미지의 색
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors = 5)
    
    for(x,y,w,h) in faces: #x,y는 왼쪽 밑?
        print(x,y,w,h)
        if x:
            print("success!")

        color = (255, 0, 0) #색
        stroke = 2 # 선의 굵기
        #끝 점
        end_x = x + w 
        end_y = y + h
        #네모 그리기
        cv2.rectangle(frame, (x, y), (end_x, end_y), color, stroke)

    #읽어온 프레임 출력
    cv2.imshow('frame', frame)
    #나가기
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 