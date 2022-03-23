# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:29:48 2022

@author: sandr
"""

import cv2
import numpy as np


body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

webcam = cv2.VideoCapture(0)  #instancia o uso da webcam

while True:
    s, imagem = webcam.read() #pega efeticamente a imagem da webcam
    imagem = cv2.flip(imagem,180) #espelha a imagem
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    print(bodies)
    
    for (x,y,w,h) in bodies:
        cv2.rectangle(imagem,(x,y),(x+w,y+h),(0,255,255),2)
    
    cv2.imshow('Video', imagem) #mostra a imagem captura na janela
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas a janelas abertas