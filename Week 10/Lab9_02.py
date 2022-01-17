import cv2 as cv
import numpy as np

img_counter = 0

# Start a video capture, using device's camera
cap = cv.VideoCapture(0)

# Check if video file opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

ret, frame = cap.read()
back = frame.copy()

height, width, _ = frame.shape
num_pixels = height * width

# Read until video is completed
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the frame
    cv.imshow('Camera', frame)

    # Converting color background frame to grayscale
    background = cv.cvtColor(back, cv.COLOR_BGR2GRAY)

    # Converting color current frame to grayscale
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Converting gray current frame to colour display
    display = cv.cvtColor(frame_gray, cv.COLOR_GRAY2BGR)

    # Showing the converted image
    cv.imshow("Background Image", background)

    method = cv.calcOpticalFlowFarneback
    params = [0.5, 3, 15, 3, 5, 1.2, 0]  # default params for method

    # Calculate Optical Flow
    flow = method(background, frame_gray, None, *params)

    # Visualize
    for row in range(4, display.shape[0], 8):
        for col in range(4, display.shape[1], 8):
            flow_at = flow[row, col]
            cv.line(display, (col, row), (col + round(flow_at[1]), row + round(flow_at[0])), (0, 255, 0))

    cv.imshow("Test", display)

    # Convert optical flow into Polar coordinates to get magnitude
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])

    # Use a threshold, to only count the significant ones
    mag_threshold = (mag > 20)

    percent = mag_threshold.sum() / (width * height)

    key = cv.waitKey(30)

    # Press Q or Esc on keyboard to exit
    if key & 0xFF == ord('q') or 0xFF == 27:
        break

    if mag_threshold.any() > 0:
        cv.waitKey(5000)
        img_name = "image{}.png".format(img_counter)
        cv.imwrite(img_name, frame)
        img_counter += 1

# Release the video capture
cap.release()
# Close all the frames
cv.destroyAllWindows()
