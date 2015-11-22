import cv2
import sys
import pyautogui
import uuid
from time import sleep

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
camera_port = 0
frequency = 30;

def has_face(image):
    print "check if has face"
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    result = len(faces) and True or False
    print result and "faces detected" or "no face detected"
    return result

def delay_screensaver():
    print "delay screensaver by press ctrl"
    pyautogui.press('ctrl')

while True:
    video_capture = cv2.VideoCapture()

    if not video_capture.open(camera_port):
        print "camera is busy. delay screensaver default"
        delay_screensaver()
    else:
        video_capture.open(camera_port)
        ret, frame = video_capture.read()
        if has_face(frame):
            delay_screensaver()
    video_capture.release()
    sleep(frequency)
