import argparse
from datetime import datetime
import numpy as np
import cv2

#Parse Arguments

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade",required = True,
                help="path to plant haar cascade")
ap.add_argument("-v", "--video", required=True, help="path to video")
ap.add_argument("-f", "--fps", required=True,
                help="The FPS must be FPS <= video's FPS and a factor of the FPS")
args = vars(ap.parse_args())

habit_cascade = cv2.CascadeClassifier(args["cascade"])

cap = cv2.VideoCapture(args["video"])

#Frames per second (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)
fps_new = (fps/int(args["fps"]))

#Total Number of frames
total_frames_actual = cap.get(cv2.CAP_PROP_FRAME_COUNT)
total_frames = 100

#Initialize Variable Count total Number of identificaitons 
total_num_iden = 0


print("Total Actual Frames: " + str(total_frames_actual))

# intialize output file
time = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
output_name = "./output/output_video_" + time + ".txt"
output_f = open(output_name, "a")
output_f.write("../video/miccal_drone.mp4\n")

# Only read 6 seconds for testing purposes

frame_num = 0
frame_pos_list = []

while(frame_num < 100):
    frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES)-1)
    ret, frame = cap.read()

    # adjust frame rate (see bellow frame_num%10)



    if frame_num == 0 or frame_num%fps_new == 0:
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
            
            total_num_iden += 1

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
percent_iden = "Percentage of Identifications: " + str(int((total_num_iden/total_frames) * 100)) + "%\n"
print(percent_iden)
cap.release()
cv2.destroyAllWindows()
