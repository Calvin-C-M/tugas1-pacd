import cv2
import os

# Get image list directory
images = os.listdir("./dataset/cat")

for img in images :
    filedir = './dataset/cat/' + img
    imageFile = cv2.imread(filedir)
    grayImage = cv2.cvtColor(imageFile, cv2.COLOR_BGR2GRAY) # Convert to gray
    ret, thresh = cv2.threshold(grayImage, 70,255,0) # Convert to binary

    # Saving image file
    cv2.imwrite("gray_"+img, grayImage)
    cv2.imwrite("binary_"+img, thresh)
