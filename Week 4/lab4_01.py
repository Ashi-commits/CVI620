import cv2 as cv

img1 = cv.imread(r"C:\Users\dlehd\OneDrive - Seneca\Semetster 6\CVI620\Workshop 4\pasta.jpg")


scale_percent = 50
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dimension = (width, height)

resized_img1 = cv.resize(img1, dimension, interpolation = cv.INTER_AREA)

cv.imshow("DisplayPasta", resized_img1)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyWindow("DisplayPasta")