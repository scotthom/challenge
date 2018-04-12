import numpy as np
import cv2
from datetime import datetime

habit_cascade = cv2.CascadeClassifier('Cascades/Solomon/miccal-cascade-30stages.xml')

cap = cv2.VideoCapture('video/miccal_drone.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)

# intialize output file
time = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
output_name = "./output/output_video_" + time + ".txt"
output_f = open(output_name, "a")
output_f.write("video/miccal_drone.mp4\n")

# Only read 6 seconds for testing purposes

frame_num = 0
frame_pos_list = []

while(frame_num < 100):
    frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES)-1)
    ret, frame = cap.read()

    # adjust frame rate (see bellow frame_num%10)

    if frame_num == 0 or frame_num%10 == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.blur(frame,(5,5))
        habit = habit_cascade.detectMultiScale(blur, 1.99, minNeighbors=1)
        detect_num = len(habit)
    
        if len(habit) != 0:
            frame_pos_list.append(frame_num)
            minute = int((frame_num/fps)/60)
            second =  int((frame_num/fps)%60)
            fractional_second = str(frame_num - 3600*minute - 60*second)
            time_stamp = str(minute) + ":" + str(second) + " " + "(" + str(fractional_second) + "/" + str(int(fps)) + ") " 
            
            image_info = ""

            for (j ,(x, y, w, h)) in enumerate(habit):
                
                obj_coordinate = str(x) + " " + str(y) + " " + str(w) + " " + str(h)
                if detect_num == 1:
                    image_info += time_stamp
                    image_info += str(frame_num) + " "
                    image_info += str(detect_num) + " "
                    image_info += obj_coordinate + "\n"
                elif detect_num == 2:
                    if j == 0:
                        image_info += time_stamp
                        image_info += str(frame_num) + " "
                        image_info += str(detect_num) + " "
                        image_info += obj_coordinate + " "
                    else:
                        image_info += obj_coordinate + "\n" 
                else:
                    if j == 0:
                        image_info += time_stamp
                        image_info += str(frame_num) + " "
                        image_info += str(detect_num) + " "
                        image_info += obj_coordinate + " "
                       
                    elif j > 0 and j < detect_num - 1:
                        image_info += obj_coordinate + " " 
                        
                    else:
                        image_info += obj_coordinate + "\n" 

            output_f.write(image_info)

cap.release()
cv2.destroyAllWindows()
