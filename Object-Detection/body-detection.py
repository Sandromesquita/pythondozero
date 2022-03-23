# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:39:47 2022

@author: sandr
"""

import cv2
import numpy as np


body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

frame = cv2.imread('people-in-park.jpg')  
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

bodies = body_classifier.detectMultiScale(gray, 1.2, 3) 

print(bodies)

for (x,y,w,h) in bodies:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
    
cv2.imshow('Humans',frame)
cv2.waitKey()
cv2.destroyAllWindows()