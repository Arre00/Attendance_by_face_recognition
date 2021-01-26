# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:58:08 2020

@author: user
"""

import cv2

def camer():
    
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    #cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    #cam.set(3, 640)  # set video width
    #cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, im = cam.read() #OR cam.opoen(RTSP URL)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5,minSize = (int(minW), int(minH)),flags = cv2.CASCADE_SCALE_IMAGE)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (10, 159, 255), 2)

            if w < 175:
                tt = str(w) + " * " + str(h) + " Come near to the camera\n"
                cv2.putText(im, str(tt), (x+5,y-5), font, 1, (0, 0, 255), 2)
            else:
                tm = str(w) + " * " + str(h) + "[Alright! Good to go.]"
                cv2.putText(im, str(tm), (x + 5, y - 5), font, 1, (0, 255, 0), 2)

        cv2.imshow('Attendance', im)
        # Stop if escape key is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object
    cam.release()
    cv2.destroyAllWindows()