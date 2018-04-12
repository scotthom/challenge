import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help="path to Haar Cascade")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(0)

cascade = cv2.CascadeClassifier(args["cascade"])

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    pos_obj_coord = cascade.detectMultiScale(gray, scaleFactor=1.99, minNeighbors=3, minSize=(215,215))

    for (x,y,w,h) in pos_obj_coord:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),1)

    # Display the resulting frame
    cv2.imshow('Detections',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()