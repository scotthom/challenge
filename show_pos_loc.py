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

# Delete Percentage of Identificaitons Information
del image_list[0]

pos_image_list = []

for image_info in image_list:
    obj_num = int(image_info.split(" ")[1]) 

    if obj_num != 0:
        split = image_info.split(" ")
        pos_image_list.append(list(split))

print(
"""Controls:
Press 'n' for next image or 'q' to quit"""
)

# Show images with positive objects highlighted
for i in range(len(pos_image_list)):
    img_name = pos_image_list[i][0]
    img_num_obj = int(pos_image_list[i][1])

    img = cv2.imread(img_name)

    for j in range(img_num_obj):
        x = int(pos_image_list[i][4*j+2])
        y = int(pos_image_list[i][4*j+3])
        w = int(pos_image_list[i][4*j+4])
        h = int(pos_image_list[i][4*j+5])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow(img_name, img)

    k = cv2.waitKey(0) & 0xff

    if k == ord('n'):
        pass
      
    elif k == ord('q'):
        cv2.destroyAllWindows
        break
        
        



 
    
