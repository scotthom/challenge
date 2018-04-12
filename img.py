import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help="path to Haar Cascade")
ap.add_argument("-i", "--image", required=True,
	help="path to image")
args = vars(ap.parse_args())


#this is the cascade we just made. Call what you want
cascade = cv2.CascadeClassifier(args["cascade"])

while 1:

    img = cv2.imread(args["image"], 1)

    cv2.imshow('Original', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    pos_obj_coord = cascade.detectMultiScale(gray, 1.20, 2)

    for (x,y,w,h) in pos_obj_coord:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('Detections', img)

    k = cv2.waitKey(0) & 0xff
    if k == 27:
        cv2.destroyAllWindows()
        break
