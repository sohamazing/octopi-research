import cv2
from numpy import std, square, mean

def crop_image(image,crop_width,crop_height):
    image_height = image.shape[0]
    image_width = image.shape[1]
    roi_left = int(max(image_width/2 - crop_width/2,0))
    roi_right = int(min(image_width/2 + crop_width/2,image_width))
    roi_top = int(max(image_height/2 - crop_height/2,0))
    roi_bottom = int(min(image_height/2 + crop_height/2,image_height))
    image_cropped = image[roi_top:roi_bottom,roi_left:roi_right]
    return image_cropped

def calculate_focus_measure(image):
	if image.shape[2] > 1:
		image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY) # optional
	lap = cv2.Laplacian(image,cv2.CV_16S)
	focus_measure = mean(square(lap))
	return focus_measure