import pyautogui
import shutil
import os
from time import sleep
 
# # returns a point  object with
# # x and y values
# print(pyautogui.position())

checkfolder = '/home/spqr/spqr/TempestSDR_EMEye/JavaGUI/EMEye_Data'
# shutil.rmtree(checkfolder)
# os.mkdir(checkfolder)

allfolders_prev = os.listdir(checkfolder)


pyautogui.moveTo(3815, 800)   # the Record Data button
pyautogui.click()

i_start = 1
i_end =   3000
i_now = i_start

restarted = []

# at the very beginning, the displayed photo should be the previous photo of i_start
# tempest_sdr should be started and reconstrcting images 

while i_now <= i_end:


    # move on to the next photo
    pyautogui.moveTo(3815, 800)
    pyautogui.click()
    pyautogui.press('right')
    sleep(.6)


    # start image recording
    pyautogui.moveTo(1089, 169)
    pyautogui.click()     

    sleep(2)     # Record for 3s. In the tempest_sdr GUI, use raw frame and a step of ~30

    # stop image recording 
    pyautogui.moveTo(1089, 169)
    pyautogui.click()   


    # check if files are generated
    allfolders = os.listdir(checkfolder)
    allfolders.sort()
    if allfolders == allfolders_prev:
        print('Error! No new folders created!')
        break
    lastfolder = allfolders[-1]
    num_images = len(os.listdir(os.path.join(checkfolder, lastfolder)))
    if  num_images == 0 :
        print('Error! No images saved!')    # this means tempest_sdr is getting timeout errors and need restart

        # restart the recording from the previous photo
        pyautogui.moveTo(3815, 800)
        pyautogui.click()
        pyautogui.press('left')
        sleep(.5)

        os.rmdir(os.path.join(checkfolder, lastfolder))
        # restart tempest_sdr 
        pyautogui.moveTo(790, 169)
        pyautogui.click()
        sleep(.5)
        pyautogui.moveTo(790, 169)
        pyautogui.click()
        sleep(2)
        restarted.append(i_now)

        continue

    print(str(len(allfolders)) + 'th photos done, ' + str(num_images) + ' images recorded')
    print('restarted at: ' + str(restarted))
    allfolders_prev = allfolders
    i_now += 1


# stop image recording 
pyautogui.moveTo(790, 169)
pyautogui.click()  
print('all done')





    
