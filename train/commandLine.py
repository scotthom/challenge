import subprocess

def posInfo():
    subprocess.call(['opencv_annotation', '--images=./clean_pos', '--annotations=./pos_img_obj_loc.dat'], shell=True)
    subprocess.call(['opencv_createsample', '--images=./clean_pos', '--annotations=./pos_img_obj_loc.dat'], shell=True)

posInfo()
