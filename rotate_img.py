import numpy as np
import cv2

def adjust_img(image):
    image = resize_img(image, 500)
    image = rotate_image(image)
    enhanced = remove_noise(image)
    return enhanced

def resize_img(image, resize_val):
    width = int(image.shape[1])
    height = int(image.shape[0])
    ratio = height/width
    image = cv2.resize(image, ( resize_val,int(resize_val*ratio))) # resizing the image
    return image

####### Rotate the image #####
def rotate_image(image):
    _,thresh = cv2.threshold(image,150,255,1)
    lines = cv2.HoughLinesP(thresh,1,np.pi/180,200,maxLineGap=30)
    line = lines[0]
    x1, y1, x2, y2 = line[0]
    slope = (y2-y1)/(x2-x1)
    angle = int(np.arctan(slope)*90) # getting the angle of the page
    image = rotate_image_sup(image,angle)
    return image

def rotate_image_sup(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

#### getting an image with the marked answers and removing any noise ####
def remove_noise(image):
    _,thresh = cv2.threshold(image,10,255,1)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    enhanced = cv2.erode(thresh,kernel)
    return enhanced

