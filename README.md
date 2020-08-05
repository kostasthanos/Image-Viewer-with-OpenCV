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

### [2] 3 windows inside the frame
We define the dimensions of 3 basic windows inside the frame in which the images will be displayed. The left window is used for the past (*already seen*) image, the right window is used for the new (*not seen yet*) image and the middle window is for the current (*watching now*) image.

<p align="center">
  <img with="400" height="334" src="https://raw.githubusercontent.com/kostasthanos/Image-Viewer-with-OpenCV/master/imgs/slider1.png"
  <img with="400" height="334" src="https://raw.githubusercontent.com/kostasthanos/Image-Viewer-with-OpenCV/master/imgs/slider6.png"       
</p>

### [3]
