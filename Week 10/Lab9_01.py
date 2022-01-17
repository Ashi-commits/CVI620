import cv2 as cv
import numpy as np

img_counter=0

# Start a video capture, using device's camera
cap = cv.VideoCapture(0)

# Check if video file opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

ret, frame = cap.read()
back = frame.copy()

height,width,_ = frame.shape
num_pixels = height*width

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the frame
    cv.imshow('Camera', frame)

    # Converting color image to grayscale image
    background = cv.cvtColor(back, cv.COLOR_BGR2GRAY)

    # Converting color image to grayscale image
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Showing the converted image
    cv.imshow("Converted Image", background)

    # make a copy of original image so that we can store the
    # difference of 2 images in the same
    diff = cv.absdiff(background, frame_gray)
    _, binary = cv.threshold(diff, 128, 1, cv.THRESH_BINARY)
    count = binary.sum()

    cv.imshow("Converted Image", binary*255)
    
    key = cv.waitKey(30)

    # Press Q on keyboard to exit
    if key & 0xFF == ord('q'):
        break

    if count > 0.01*num_pixels:
        cv.waitKey(5000)
        img_name = "image{}.png".format(img_counter)
        cv.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

# Release the video capture
cap.release()
# Close all the frames
cv.destroyAllWindows()