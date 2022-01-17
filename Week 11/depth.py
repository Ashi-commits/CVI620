import cv2 as cv
import numpy as np
import depth as dp

path = cv.imread(r"C:\Users\Ayushi\OneDrive\Desktop\CVI\Week 11\5_of_diamonds.png")

cv.imshow("image", path)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()