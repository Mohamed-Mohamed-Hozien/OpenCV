import cv2 as cv
import os
# Read the video from specified path
cam = cv.VideoCapture("DataExample.mp4")

try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):
    
        # reading from frame
        ret, frame = cam.read()
    
        if ret:
            # if video is still left continue creating images
            # name = './data/frame' + str(currentframe) + '.jpg'
            name = f"./data/frame{currentframe}.jpg"
            print('Creating...' + name)
    
            # writing the extracted images
            cv.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

img = cv.imread('data/frame0.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow('image', img_gray)
cv.waitKey(0)