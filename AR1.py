import dlib
import cv2 as cv
from math import hypot
import numpy as np



cap = cv.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

noseImg = cv.imread("mustache.png")
noseClown = noseImg

_, img = cap.read()
rows, cols, _ = img.shape
noseMask = np.zeros((rows, cols), np.uint8)

while True:

    _, img = cap.read()

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = detector(imgGray)

    for face in faces:
        landmarks = predictor(imgGray, face)
        # Nose coordinates
        topNose = (landmarks.part(29).x, landmarks.part(29).y)
        centerNose = (landmarks.part(30).x, landmarks.part(30).y + 55)
        leftNose = (landmarks.part(31).x, landmarks.part(31).y)
        rightNose = (landmarks.part(35).x, landmarks.part(35).y)

        # cv.circle(img, rightNose, 3, (255, 0, 0), -1)
        noseWidth = int(hypot(leftNose[0] - rightNose[0], leftNose[1] - rightNose[1]) * 2)

        topLeft = (int(centerNose[0] - noseWidth / 2), int(centerNose[1] - noseWidth / 2))
        bottomRight = (int(centerNose[0] + noseWidth / 2), int(centerNose[1] + noseWidth / 2))

        #adding new nose
        noseClown = cv.resize(noseImg, (noseWidth, noseWidth))
        noseClownGray = cv.cvtColor(noseClown, cv.COLOR_BGR2GRAY)
        _, noseMask = cv.threshold(noseClownGray, 25, 255, cv.THRESH_BINARY_INV)
        noseArea = img[topLeft[1]: topLeft[1] + noseWidth, topLeft[0]: topLeft[0] + noseWidth]
        noNose = cv.bitwise_and(noseArea, noseArea, mask = noseMask)
        finalNose = cv.add(noNose, noseClown)
        img[topLeft[1]: topLeft[1] + noseWidth, topLeft[0]: topLeft[0] + noseWidth] = finalNose


        #cv.imshow("nose", noNose)

    cv.imshow("img0", img)
    #cv.imshow("img1", noseClown)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break