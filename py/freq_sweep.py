import pyautogui
import shutil
import os
from time import sleep
 

checkfolder = '/home/spqr/spqr/TempestSDR_EMEye/JavaGUI/EMEye_Data'


i_start = 673    # the start frequncy 
i_end = 2000    # the end frequncy
i_now = i_start



num_images_prev = 0

# tempest_sdr should already be running
# start image recording 
pyautogui.moveTo(1089, 169)
pyautogui.click() 


while i_now <= i_end:

    sleep(6)    # time for each frequency


    # move on to the next frequency
    pyautogui.moveTo(911, 489)
    pyautogui.click()


    allfolders = os.listdir(checkfolder)
    allfolders.sort()
    lastfolder = allfolders[-1]
    num_images = len(os.listdir(os.path.join(checkfolder, lastfolder)))
    if num_images == num_images_prev:
        print('Need to restart tempest_sdr')
        pyautogui.moveTo(790, 169)
        pyautogui.click()
        sleep(.5)
        pyautogui.moveTo(790, 169)
        pyautogui.click()
        sleep(2)
        # start image recording 
        pyautogui.moveTo(1089, 169)
        pyautogui.click() 
        sleep(1)
        continue

    num_images_prev = num_images
    i_now += 1

# stop image recording 
pyautogui.moveTo(790, 169)
pyautogui.click()  
print('all done')





    
