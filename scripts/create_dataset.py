# Code to resize images and create a random 80/20 train test split
from PIL import Image, ImageOps
import os
import shutil
import random

# Initializing constants
SOURCE = 'D://COURSES//COM Third Year//Disseration Project//Dataset//Dataset from Turkey/'
DESTINATION = 'ResizedImages/'
IMG_FORMAT = 'jpg'
IMG_HEIGHT = 640
IMG_WIDTH = 480

# Creating a directory for resizing the images and placing them
os.mkdir(DESTINATION[:-1])

# Setting the resolution to resize
resolution = [IMG_WIDTH, IMG_HEIGHT]

# Getting all the images in the directory
images = []
for file in os.listdir(SOURCE):
    if file.endswith('.' + IMG_FORMAT):
        images.append(file)

# Creating and resizing the images
for i in range(0, len(images)):
    im = Image.open(SOURCE + '/' + images[i])
    im = ImageOps.exif_transpose(im)
    im_resized = im.resize(resolution, Image.ANTIALIAS)
    im_resized.save(DESTINATION + '/' + str(i + 10) + ".png")

print("Finished creating resized images")

os.mkdir(DESTINATION + 'Train')
os.mkdir(DESTINATION + 'Test')

# Getting all the resized images in the directory
resized_images = []
for file in os.listdir(DESTINATION):
    if file.endswith('.png'):
        resized_images.append(file)

# Creating a random list of train and test with a 80/20 split
train = random.sample(resized_images, int(len(resized_images) * 0.8))
test = set(resized_images).difference(set(train))
test = list(test)

# Moving the images to the source directory
for i in range(len(train)):
    shutil.move(DESTINATION + train[i], SOURCE + "Train/")
for j in range(len(test)):
    shutil.move(DESTINATION + test[j], SOURCE + "Test/")

print("Finished dataset creation")
