import cv2 as cv
from matplotlib import pyplot as plt

img_rgb = cv.imread(r"C:\Users\Ayushi\Downloads\Trillium_s.jpg")
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
img2 = img_gray.copy()
template = cv.imread(r"C:\Users\Ayushi\Downloads\Trillium_t.jpg",0)
w, h = template.shape[::-1]

# All the 4 methods for comparison in a list
methods = ['cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

cv.imshow('color image',img_rgb)
cv.imshow('gray image',img_gray)
cv.imshow('template',template)

# part d
width = img.shape[1]*2  # twice the original width
height = img.shape[0]*2  # twice the original height
dim = (width, height)

# resize image
resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
print('Resized Dimensions : ', resized.shape)
cv.imshow("Resized image", resized)

height, width = resized.shape[0:2]
angle = 30; scale = 1
rotationMatrix = cv.getRotationMatrix2D((width/2, height/2), angle, scale)
rotatedImage = cv.warpAffine(resized, rotationMatrix, (width, height))

cv.imshow("Rotated image", rotatedImage)

# All the 2 methods for comparison in a list
methodsRotate = ['cv.TM_CCORR', 'cv.TM_CCORR_NORMED']
for meth in methodsRotate:
    imgRotate = rotatedImage.copy()
    methodsRotate = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(imgRotate,template,methodsRotate)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(imgRotate,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(imgRotate,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()


key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()