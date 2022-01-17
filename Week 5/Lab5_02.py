import cv2 as cv
import numpy as np

# Reading the original image from the system as gray image
gray = cv.imread(r"C:\Users\Ayushi\Downloads\512px-Yonge_Street_south_of_College_St.,_Toronto.JPG", cv.IMREAD_GRAYSCALE)


# Defining the dimensions for resizing of the image
#scale_percent = 50
#width = int(img.shape[1] * scale_percent / 100)
#height = int(img.shape[0] * scale_percent / 100)
#dimension = (width, height)

# Resizing the read image with dimensions specified
#resized_img = cv.resize(img, dimension, interpolation = cv.INTER_AREA)

# Taking input from the user for the probability
#input_val = float(input("Enter your value between 0 and 1: "))
#print(input_val)

# Checking for a valid user input
#if (input_val > 1 or input_val < 0):
 #   print("Invalid input")

# Printing number of pixels to be affected
#print("- Number of Pixels to be affected: " + str(resized_img.size))

# Split the image into its channels
#blue, green, red = cv.split(resized_img)

# Convert image to grayscale
#gray_image = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)

# Display the grayscale version of image
#cv.imshow("Gray Image", gray_image)

# Adding salt & pepper noise to an image
#def salt_pepper(prob):
      # Extract image dimensions
      #row, col = gray_image.shape

      # Declare salt & pepper noise ratio
      #poportion = 0.5 # Proportion of the noise
      #noisy = np.copy(gray_image)

      # Apply salt noise on each pixel individually
      #num_salt = np.ceil(prob * gray_image.size * poportion)
      #coords = [np.random.randint(0, i - 1, int(num_salt))
       #     for i in gray_image.shape]
      #noisy[coords] = 1

      # Apply pepper noise on each pixel individually
      #num_pepper = np.ceil(prob * gray_image.size * (1. - poportion))
     # coords = [np.random.randint(0, i - 1, int(num_pepper))
       #     for i in gray_image.shape]
      #noisy[coords] = 0
      # Displaying the noisy image
     # cv.imshow("Noisy Image", noisy)

     # return noisy

# Call salt & pepper function with user's input as probability
# on the grayscale image of nail_polish.jpg
# with the salt and pepper ratio as 0.5
#noisy_image = salt_pepper(input_val)


# Using box function to blur the original image
#blurred = cv.boxFilter(resized_img, -1, (3,3))
#cv.imshow("Blurred Image", blurred)

# Using bilateral filter to reduce noise in the image
#bilateral = cv.bilateralFilter(noisy_image,9,3,3)
#cv.imshow("Bilateral Image", bilateral)

# Using Median filter to reduce noise in the image
#median = cv.medianBlur(noisy_image,3)
#cv.imshow("Median Image", median)

# Using Gaussian filter to reduce noise in the image
#sigma = 1.5
#myKernel = cv.getGaussianKernel(3,sigma)
#gaussian = cv.sepFilter2D(noisy_image, -1, myKernel, myKernel)
#cv.imshow("Gaussian Image", gaussian)

# Displaying the Original image
cv.imshow("Original Image", gray)

# Canny recommended a upper:lower ratio between 2:1 and 3:1.
canny_map = cv.Canny(gray, 50, 150)
# Displaying Canny edge map
cv.imshow("Canny Map", canny_map)

threshold=0
value=50
iteration=1

for item in range(3):
        threshold+=value
        lines = cv.HoughLinesP(canny_map, 1, np.pi / 180, threshold, minLineLength=50, maxLineGap=10)
        # Draw lines on the image
        result = cv.cvtColor(canny_map, cv.COLOR_GRAY2BGR)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            result = cv.line(result, (x1, y1), (x2, y2), (0, 0, 255), 1)

        windowName = "Result" + str(iteration)
        iteration += 1
        # Show result
        cv.imshow(windowName,result)

key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyWindow("DisplayPasta")
