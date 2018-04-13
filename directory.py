# USAGE
# python3 --image path_to_directory --cascade path_to_casacade

import argparse
import numpy as np
import cv2
import collections
import os
from imutils import paths
from datetime import datetime

# function parameter sugestion
#def directory(directory, cascade)

# construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade",
	default="penset-cascade-25stages.xml",
	help="path to plant haar cascade")
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
args = vars(ap.parse_args())

# grab the paths to the images,
imagePaths = list(paths.list_images(args["images"]))
images_num = len(imagePaths)
number_total_detect = 0

# initialize the list of images
images = []

imagePath_list = []
imagePath_obj_loc = {}

for i, imagePath in enumerate(imagePaths):
        image = cv2.imread(imagePath)

# load the penset detector Haar cascade, then detect penset
# in the input image
# alter variable for scaleFactor, minNeighbors, minSize
# update the list of image
        detector = cv2.CascadeClassifier(args["cascade"])
        rects = detector.detectMultiScale(image, scaleFactor=1.30, minNeighbors=1, minSize=(24, 24))
        detect_num = len(rects)

        if detect_num > 0:
            imagePath_list.append(imagePath)
            number_total_detect += 1

        image_info = ""

        # loop over the penset and draw a rectangle surrounding each
        for (j, (x, y, w, h)) in enumerate(rects):
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, "Target #{}".format(j + 1), (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 2)
                
                obj_coordinate = str(x) + " " + str(y) + " " + str(w) + " " + str(h)

                if detect_num == 1:
                    image_info += str(detect_num) + " "  
                    image_info += obj_coordinate + "\n"
                    imagePath_obj_loc[imagePath] = image_info
                elif detect_num == 2:
                    if j == 0:
                        image_info += str(detect_num) + " " 
                        image_info += obj_coordinate + " "
                    else:
                        image_info += obj_coordinate + "\n"
                        imagePath_obj_loc[imagePath] = image_info
                else:
                    if j == 0:
                        image_info += str(detect_num) + " " 
                        image_info += obj_coordinate + " " 
                       
                    elif j > 0 and j < detect_num - 1:
                        image_info += obj_coordinate + " " 
                        
                    else:
                        image_info += obj_coordinate + "\n"
                        imagePath_obj_loc[imagePath] = image_info       

imagePath_list_sorted = sorted(imagePath_list, key=lambda f: int(''.join(filter(str.isdigit, f))))

# intialize output file
time = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
output_name = "./output/output_" + time + ".txt"
output_f = open(output_name, "a")

# initialize string to print all image information
image_full = ""

#Percentage of frames with identification(s) to total frames
abspath_img_dir = os.path.abspath(args["images"])
percent_iden_info = os.path.abspath(args["images"]) + " percentage of identifications: " + str(int(number_total_detect/images_num * 100)) + "%\n"
print(percent_iden_info)   

output_f.write(percent_iden_info)

#print all information
for i in imagePath_list_sorted:
        image_full =  i + " " + imagePath_obj_loc[i]
        output_f.write(image_full)
        image_full = ""