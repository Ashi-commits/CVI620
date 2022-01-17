import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
r = 0
g = 0
b = 0
def user_prompt(userInputLetter):
    if userInputLetter == 'r':
        r = 0
        g = 0
        b = 255
    elif userInputLetter == 'w':
        r = 255
        g = 255
        b = 255
    elif userInputLetter == 'g':
        r = 0
        g = 255
        b = 0
    elif userInputLetter == 'y':
        r = 0
        g = 255
        b = 255
    return

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,userInputLetter
    userInputLetter = input('Enter first letter of any color to set the color of the rectangle: ')
    user_prompt(userInputLetter)
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    # elif event == cv.EVENT_MOUSEMOVE:
    #     if drawing == True:
    #         if mode == True:
    #             cv.rectangle(img,(ix,iy),(x,y),(r,g,b))
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(r,g,b), 3)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()