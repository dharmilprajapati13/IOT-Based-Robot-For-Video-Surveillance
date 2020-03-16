#https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/5
#for referance see above link


from picamera import PiCamera # import picamera library
from time import sleep #import sleep form time library

camera = PiCamera() # create object for camera
#camera.image_effect = "negative"

camera.start_preview() #strat priview is optinal
#camera.vflip()
#sleep(2)  # it’s important to sleep for at least two seconds before capturing an image, because this gives the camera’s sensor time to sense the light levels.
#camera.capture('/home/pi/Desktop/image4.jpg') #capture image and save at the given location
#camera.start_recording('/home/pi/Desktop/video.h264') #start recording
#sleep(10)
#camera.stop_recording() #stop recording

stop = input("press \'s\' to stop the recording")

if(stop == "s"):
    sleep(2)
    camera.capture('/home/pi/Desktop/image4.jpg') #capture image and save at the given location
    sleep(2)
    camera.stop_preview() #stop preview
