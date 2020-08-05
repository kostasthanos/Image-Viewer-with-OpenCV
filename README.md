# Image-Viewer-with-OpenCV
This a simple image viewer using OpenCV library and color tracking.

## Main Idea
The main idea of this project is that any user having a folder with image files in it can run the script and watch the images one by one using hand+color movement  and trackig in order to view the next image each time.

There are two basic python files in this project.
1. *rename.py*
2. *image_viewer.py*

## *rename.py*
This file contains the code required to rename all the images in the main folder. If we have a folder containing for example 5 image files, then when we run *rename.py* all of the image files are being renamed to the form **pic+number_of_image+.+extension** (e.g. pic2.jpg)

## *image_viewer.py*
Inside this file we are importing *rename.py*. These are some details about the program.

### [1] Directory of image files
First of all we must define the directory to our folder with the image files.

```python
directory = "path_to_imag_files/images"
```

### [2] Three windows inside the frame
We define the dimensions of 3 basic windows inside the frame in which the images will be displayed. The left window is used for the past (*already seen*) image, the right window is used for the new (*not seen yet*) image and the middle window is for the current (*watching now*) image.

```python
# Desired frame dimensions (width and height)
# Width and Height
w, h = 870, 652

# Middle winndow
img_top_left = (int((w-500)/2), 30)
img_bottom_right = (img_top_left[0]+500, img_top_left[1]+255)

# Left/past image window
img_past_top_left = (30, img_bottom_right[1]+30)
img_past_bottom_right = (img_past_top_left[0]+180, img_past_top_left[1]+90) 

# Right/new image window
img_new_top_left = (w-30-180, img_bottom_right[1]+30)
img_new_bottom_right = (img_new_top_left[0]+180, img_new_top_left[1]+90)
```

<p align="center">
  <img with="400" height="334" src="https://raw.githubusercontent.com/kostasthanos/Image-Viewer-with-OpenCV/master/imgs/slider1.png">     
</p>

### [3] Define the testing area
Now it's time to set our testing area. This will be the area (sub-frame) inside the main frame in which our color-finger tracking will be active.

```python
# Set the color-finger tracking window frame
finger_window = np.array([[[0,460], [0,h], [320,h], [320,460], [w-320,460], [w-320,h], [w,h], [w,460]]], np.int32)
cv2.polylines(frame, [finger_window], True, (0,255,0), thickness=3)

# Left & Right window frame for the color tracking part
finger_left_window = np.array([[[0,460], [0,h], [320,h], [320,460]]], np.int32)  # Finger Left Window
finger_right_window = np.array([[[w-320,460], [w-320,h], [w,h], [w,460]]], np.int32) # Finger Right Window
```
<p align="center">
  <img with="400" height="334" src="https://raw.githubusercontent.com/kostasthanos/Image-Viewer-with-OpenCV/master/imgs/slider5.png">     
</p>

The area in which the color-finger tracking is active is with green color in the picture below.
<p align="center">
  <img with="400" height="334" src="https://raw.githubusercontent.com/kostasthanos/Image-Viewer-with-OpenCV/master/imgs/slider4.png">     
</p>
