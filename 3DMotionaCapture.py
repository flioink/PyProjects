import cv2 as cv
from cvzone.PoseModule import PoseDetector
import numpy as np
import os


videoPath0 = "dance.mp4"
videoPath1 = os.path.join("D:\Downloads\RANDOM_VIDZ", "ana2.mp4")
videoPath2 = os.path.join("D:\Downloads\RANDOM_VIDZ", "jumpy.mp4")

cap = cv.VideoCapture(0)
detector = PoseDetector()
posList = []

while True:
    _, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ""

        for lm in lmList:
            #print(lm)
            lmString += f"{str(lm[1])},{str(img.shape[0] - lm[2])},{str(lm[3])},"
        posList.append(lmString)

    #print(posList)

    cv.imshow("img0", img)
    key = cv.waitKey(1)

    if  key == ord("q"):
        break

    elif key == ord("s"):
        with open("AnimFile.txt", "w") as f:
            f.writelines(["%s\n" % item for item in posList])

