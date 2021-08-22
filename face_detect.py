import cv2
import numpy as np
import matplotlib.pyplot as plt 
%matplotlib inline
 

# Reading in the image and creating copies
img = cv2.imread("C:/Users/91630/Downloads/gg.jfif")
img_copy = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()
 
# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
 
 
 
# create a function to detect face
def adjusted_detect_face(img):
     
    face_img = img.copy()
     
    face_rect = face_cascade.detectMultiScale(face_img,scaleFactor = 1.2,minNeighbors = 5)
     
    for (x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y),(x + w, y + h), (255, 255, 255), 10)
         
    return face_img
 
 
# create a function to detect eyes
def detect_eyes(img):
     
    eye_img = img.copy()   
    eye_rect = eye_cascade.detectMultiScale(eye_img,scaleFactor = 1.2,minNeighbors = 5)   
    for (x, y, w, h) in eye_rect:
        cv2.rectangle(eye_img, (x, y),(x + w, y + h), (255, 255, 255), 10)       
    return eye_img
 

# Detecting the face
face = adjusted_detect_face(img_copy)
plt.imshow(face)
# Saving the image
cv2.imwrite('face.jpg', face)

eyes = detect_eyes(img_copy2)
plt.imshow(eyes)
cv2.imwrite('face_eyes.jpg', eyes)

imga=cv2.addWeighted(face,0.5,eyes,0.5, 0)
plt.imshow(imga)
cv2.imwrite('imaga.jpg',imga)  
# Show the image
cv2.imshow('image',imga)
cv2.waitKey(0)
cv2.destroyAllWindows()