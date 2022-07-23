import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector
import socket

cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = FaceDetector(minDetectionCon=0.8)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)


while True:
    _, img = cap.read()
    img, bbox = detector.findFaces(img)

    if bbox:
        center = bbox[0]["center"]
        print(center)
        data = str.encode(str(center))
        sock.sendto(data, serverAddressPort)


    cv.imshow("img0", img)

    key = cv.waitKey(1)

    if key == ord("q"):
        break