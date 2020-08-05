#===========================#
# @2020 Konstantinos Thanos #
#    All Rights Reserved    #
#         05/08/2020        #
#===========================# 

# Import Libraries
import os, os.path
import numpy as np
import math
import cv2

# Import rename.py file content
from rename import *

# Set the directory which contains the images
directory = "images"

# Count the number of images with os library
image_num = len([file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))])

# Video Capture
cap = cv2.VideoCapture(1)

# Set desired 'cap' dimensions based on screen
# Width and Height
w, h = 870, 652
midx, midy = int(w/2), int(h/2)

# Set dimensions for the inside frame windows
#=============================================
# Set dimensions for image window based on images dimensions (img)
# Desired image window dimensions : (500, 255)
img_top_left = (int((w-500)/2), 30)
img_bottom_right = (img_top_left[0]+500, img_top_left[1]+255)

# Set dimensions for left/past image window (img_past)
# Desired left/past image dimensions : (180, 90)
img_past_top_left = (30, img_bottom_right[1]+30)
img_past_bottom_right = (img_past_top_left[0]+180, img_past_top_left[1]+90) 

# Set dimensions for right/new image window (img_new)
# Desired right/new image dimensions : (180, 90)
img_new_top_left = (w-30-180, img_bottom_right[1]+30)
img_new_bottom_right = (img_new_top_left[0]+180, img_new_top_left[1]+90)

# Initializations
pic_num = 1
frames = 0

# Start camera
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (w, h))
    frame = cv2.flip(frame, 1) # Flip frame horizontaly if it's necessary

    frames += 1       # Increase the number of frames
    img_temp = False 
 
    # HSV format for the frame and the contour search
    #=================================================
    # Apply hsv format on frame for color tracking
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Define range for green color (this can be changed to any color)
    lower_color = np.array([67, 231, 0])
    upper_color = np.array([180, 255, 255])

    # Create a mask
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find the contours for the above mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Find the maximum contour area and track the center of it (color tracking)
    for contour in contours:
        # Find the area of each contour
        area = cv2.contourArea(contour)
        M = cv2.moments(contour)
        # Continue only if area > 100
        if area > 100:
            # Draw each contour
            cv2.drawContours(frame, [contour], -1, (0,255,0), 2)
            # Find each contour center
            if int(M["m00"])!=0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 2, (0,0,255), 2)
                temp = True             

    # Load the centered basic (first) image to start the Image Slider
    img = cv2.imread("images/pic"+str(pic_num)+".jpg")

    # Check the number of current image
    if pic_num < image_num:
        # Add one for the new image (right image)
        img_new = cv2.imread("images/pic"+str(pic_num+1)+".jpg")
        if pic_num == 1:
            img_past = frame[img_past_top_left[1]:img_past_bottom_right[1], img_past_top_left[0]:img_past_bottom_right[0]]
        else:
            # Subtract one for the past image (left image)
            img_past = cv2.imread("images/pic"+str(pic_num-1)+".jpg") 

    # Set image window frame
    cv2.rectangle(frame, img_top_left, img_bottom_right, (0,250,250), 4)

    # Set past image window frame
    cv2.rectangle(frame, img_past_top_left, img_past_bottom_right, (0,250,250), 4)

    # Set new image window frame
    cv2.rectangle(frame, img_new_top_left, img_new_bottom_right, (0,250,250), 4)

    # Set the color-finger tracking window frame
    # Comment the above 2 lines to hide polygon color
    finger_window = np.array([[[0,460], [0,h], [320,h], [320,460], [w-320,460], [w-320,h], [w,h], [w,460]]], np.int32)
    cv2.polylines(frame, [finger_window], True, (0,255,0), thickness=3)
 
    # Left & Right window frame for the color tracking part
    finger_left_window = np.array([[[0,460], [0,h], [320,h], [320,460]]], np.int32)  # Finger Left Window
    finger_right_window = np.array([[[w-320,460], [w-320,h], [w,h], [w,460]]], np.int32) # Finger Right Window

    # Resize images
    frame[img_top_left[1]: img_bottom_right[1], img_top_left[0]: img_bottom_right[0]] = cv2.resize(img, (500,255))
    frame[img_new_top_left[1]:img_new_bottom_right[1], img_new_top_left[0]:img_new_bottom_right[0]] = cv2.resize(img_new, (180,90))
    frame[img_past_top_left[1]:img_past_bottom_right[1], img_past_top_left[0]:img_past_bottom_right[0]] = cv2.resize(img_past, (180,90))

    # Text-Info settings
    #====================
    font = cv2.FONT_HERSHEY_PLAIN # Font family
    text1 = "From this point and below move the color tracker left"
    text2 =  "for next/new image or right for previous/past image"
    text_color = (255,255,255)    # Text color
    cv2.putText(frame, text1, (70, int((2/3)*h)), font, 1.5, text_color, 2)
    cv2.putText(frame, text2, (80, int((2/3)*h)+20), font, 1.5, text_color, 2)

    # Every 5 frames start frame count from 0 and set variable img_temp to True
    if frames == 5:
        img_temp = True
        frames = 0 

    if temp:
        # Check if center of color-contour is on the finger_left_window
        if (cv2.pointPolygonTest(finger_left_window,(cx,cy),True)>0) and (img_temp == True):
            pic_num += 1
            if pic_num > image_num:
                pic_num = 1
        # Check if center of color-contour is on the finger_right_window
        elif (cv2.pointPolygonTest(finger_right_window,(cx,cy),True)>0) and (img_temp == True):
            pic_num -= 1
            if pic_num < 1:
                pic_num = 1
        temp = False

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key==27: # Press Esc to exit from the Image Slider
        break
    
cap.release()
cv2.destroyAllWindows()
