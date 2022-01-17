import cv2 as cv
import numpy as np
import sys
import matplotlib.pyplot as plt

width = 640
height = 480
dim = (width, height)

nail_polish = cv.imread(r"C:\Users\Ayushi\Downloads\nail_polish.jpg")
if nail_polish is None:

    sys.exit("Could not read the image.")
# resize image
nail_polish1 = cv.resize(nail_polish, dim, interpolation=cv.INTER_AREA)

#converting color image to HSV color scale
hsvImage = cv.cvtColor(nail_polish, cv.COLOR_BGR2HSV)
#Splitting the HSV scale image to equalize in color image format
#hsv_planes = cv.split(hsvImage)
#using CLAHE to equalize color image with clipping limit at 2 and the tile grid size (splits an image into 64 tiles with 8 columns and 8 rows)
#clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
#hsv_planes[2] = clahe.apply(hsv_planes[2])
#hsv = cv.merge(hsv_planes)
#equalized = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)



# create the histogram
#histogram, bin_edges = np.histogram(nail_polish, bins=256, range=(0, 1))

# configure and draw the histogram figure
#plt.figure()
#plt.title("Grayscale Histogram")
#plt.xlabel("grayscale value")
#plt.ylabel("pixels")
#plt.xlim([0.0, 1.0])  # <- named arguments do not work here

#plt.plot(bin_edges[0:-1], histogram)  # <- or here
#plt.show()


# create the histogram
#equalized_histogram, bin_edges = np.histogram(equalized, bins=256, range=(0, 1))

# configure and draw the histogram figure
#plt.figure()
#plt.title("Equalized Grayscale Histogram")
#plt.xlabel("grayscale value")
#plt.ylabel("pixels")
#plt.xlim([0.0, 1.0])  # <- named arguments do not work here

#plt.plot(bin_edges[0:-1], equalized_histogram)  # <- or here
#plt.show()


img_hsv = cv.cvtColor(nail_polish, cv.COLOR_BGR2HSV)
img_hsv_equalized = img_hsv
img_hsv_equalized[:,:,2] = cv.equalizeHist(img_hsv[:,:,2])
equalized_img = cv.cvtColor(img_hsv_equalized, cv.COLOR_HSV2BGR)
cv.imshow("original image", nail_polish)
cv.imshow("equalized image", equalized_img)
fig, ax = plt.subplots(1, 2, figsize=(11,5))
hist = cv.calcHist([nail_polish],[2], None, [256], [0, 256])
ax[0].plot(hist)
ax[0].set_title("Histogram of the original image, Value Channel")
equalized_hist = cv.calcHist([img_hsv_equalized], [2], None, [256], [0, 256])
ax[1].plot(equalized_hist)
ax[1].set_title("Equalized histogram, Value Channel")
plt.show()



#img2 = cv.add(img1, np.ones(img1.shape, dtype = "uint8") * 100)
# resize image
#resized2 = cv.resize(img2, dim, interpolation=cv.INTER_AREA)
#cv.imshow("Display2", resized2)

#TODO :: open another window for img3 to increase the contrast

#img3 = cv.multiply(img2, np.ones(img2.shape, dtype = "uint8"), scale = 1.5)
# resize image
#resized3 = cv.resize(img3, dim, interpolation=cv.INTER_AREA)
#cv.imshow("Display3", resized3)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyWindow("Display1")
    #cv.destroyWindow("Display2")
    #cv.destroyWindow("Display3")

#img4 = cv.imread(r"C:\Users\Ayushi\OneDrive\Pictures\Screenshots\black.png")
#img4=cv.resize(img4,(img1.shape[1],img1.shape[0]))

#userInputValue = float(input('Enter a value between 0 and 1: '))
#corresponding_value = 1 - userInputValue

#img5=cv.addWeighted(img1, userInputValue, img4, corresponding_value,0)

#cv.imshow("Display window4", img5)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    sys.exit("Exiting all the windows")