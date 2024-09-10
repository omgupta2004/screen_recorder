import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width= GetSystemMetrics(0)#width 0 se strt krega
height= GetSystemMetrics(1)
dim=(width,height)

f=cv2.VideoWriter_fourcc(*"mp4v")

output=cv2.VideoWriter("test.mp4",f,30.0,dim)#change location in this also, 30 is frames per second

now_start_time=time.time()
dur=10+4 #duration , +4 is for code compile timme
end_time=now_start_time + dur

while True:
    image=pyautogui.screenshot()#screenshot capture
    frame_1=np.array(image)#collect all images
    frame=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)

    output.write(frame)
    
    c_time=time.time()#for current time

    if c_time > end_time:
        break

output.release()

print("___end__")




