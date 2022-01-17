import cv2
import uuid
import time

# Define the duration (in seconds) of the video capture here
capture_duration = 5
cap = cv2.VideoCapture(0)
start_time = time.time()

if(cap.isOpened()==False):
    print("Error opening video stream")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    while( int(time.time() - start_time) < capture_duration ):
        #Captureframe-by-frame
        ret, frame = cap.read()
        img_name = './Images/Test/{}.jpg'.format(str(uuid.uuid1()))
        cv2.imwrite(img_name, frame)
        cv2.imshow('frame', frame)
    break

cap.release()
cv2.destroyAllWindows()
