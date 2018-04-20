import numpy as np
import cv2

cap = cv2.VideoCapture("../video/miccal_drone.mp4")

habit_cascade = cv2.CascadeClassifier('cascades/Solomon/miccal-cascade-30stages.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray,(5,5))
    habit = habit_cascade.detectMultiScale(blur, 1.99, minNeighbors=1)

    for (x,y,w,h) in habit:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),1)

    # Display the resulting frame
    cv2.imshow('Detections',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
