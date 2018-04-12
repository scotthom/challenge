# USAGE
# python3 --output output_date_time.txt
# Execute this program in the same folder directory.py was executed.
# See output_date_time.txt for help find folder
#Press "n" for next image or "q" to quit

import cv2
import argparse

#Parse positive_object_info.txt
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output",
	help="file name of of output")
args = vars(ap.parse_args())
file_r = open(args["output"], "r")
image_list = file_r.readlines()

path = image_list.pop(0).strip("\n")
pos_image_list = []

for image_info in image_list:
    image_info_list = image_info.split(" ")

    obj_num = int(image_info_list[2]) 

    if obj_num != 0:
        split = image_info_list
        pos_image_list.append(list(split))

print(
"""Controls:
Press 'n' for next image or 'q' to quit"""
)

cap = cv2.VideoCapture(path)

while(cap.isOpened()):

    # Show images with positive objects highlighted
    for i in range(len(pos_image_list)):
        frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES)-1)
        cap.set(1, frame_num)
        ret, frame = cap.read()

        img_num_obj = int(pos_image_list[i][3])

        for j in range(img_num_obj):
            x = int(pos_image_list[i][4*j+4])
            y = int(pos_image_list[i][4*j+5])
            w = int(pos_image_list[i][4*j+6])
            h = int(pos_image_list[i][4*j+7])
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
        frame = cv2.resize(frame, (1248,702))
        cv2.imshow(path, frame)

        k = cv2.waitKey(0) & 0xff

        if k == ord('n'):
            pass
      
        elif k == ord('q'):
            cv2.destroyAllWindows
            break
        if i > len(pos_image_list):
            break
    break

        



 
    
