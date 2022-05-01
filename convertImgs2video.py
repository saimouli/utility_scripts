import cv2
import numpy as np
import glob
  
# choose codec according to format needed
video = cv2.VideoWriter('/home/saimouli/Desktop/Drone_data/May1/result_d25a1b.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 20, (1280, 720))

files = glob.glob('/home/saimouli/Desktop/Drone_data/May1/frame_org_d52a1b9c9d55398c_1651358044000/*.png')
files = sorted(files, key=lambda x : int( x.split("/")[7].split(".")[0] ))
print(len(files))

for fil in files:
    img = cv2.imread(fil)
    img_ = cv2.resize(img, (1280, 720))
    video.write(img_)

cv2.destroyAllWindows()
video.release()
