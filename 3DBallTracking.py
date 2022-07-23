import cvzone
from cvzone.ColorModule import ColorFinder
import cv2 as cv
import time
import socket


#params
cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

_, img = cap.read()
h, w, _ = img.shape

prevFrame = 0

myColorFinder = ColorFinder(False)

hsvVals = {'hmin': 0, 'smin': 104, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5053)

while True:
    _, img = cap.read()
    imgColor, mask = myColorFinder.update(img, hsvVals)
    imgContour, contours = cvzone.findContours(img, mask, minArea=1000)

    if contours:
        data = contours[0]["center"][0], \
        h - contours[0]["center"][1], \
        int(contours[0]["area"])
        print(data)
        data = str.encode(str(data))
        sock.sendto(data, serverAddressPort)

    currFrame = time.time()
    fps = int(1/(currFrame - prevFrame))
    prevFrame = currFrame
    cv.putText(img, f"fps: {str(fps)}", (130, 130), cv.FONT_ITALIC, 1, (0, 0, 0), 2)

    #imgStack = cvzone.stackImages([img, imgColor, mask, imgContour], 2, 0.5)

    imgContour = cv.resize(imgContour, (0,0), None, 0.3, 0.3)

    cv.imshow("img0", imgContour)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()
cap.release()