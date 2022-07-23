from cvzone.HandTrackingModule import HandDetector
import cv2 as cv
import time
import socket

#params
cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
_, img = cap.read()
h, w, _ = img.shape
detector = HandDetector(maxHands=2, detectionCon= 0.8)

prevFrame = 0

#communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

while True:
    _, img = cap.read()
    hands, img = detector.findHands(img, draw=True)

    currFrame = time.time()
    fps = int(1/(currFrame - prevFrame))
    prevFrame = currFrame
    cv.putText(img, f"fps: {str(fps)}", (130, 130), cv.FONT_ITALIC, 1, (0, 0, 0), 2)
    data = []

    if hands:
        #get first hand detected
        hand = hands[0]
        lmList = hand["lmList"]
        #print(lmList)
        for lm in lmList:
            print(len(lm))
            data.extend([lm[0], h - lm[1]])

        sock.sendto(str.encode(str(data)), serverAddressPort)


    cv.imshow("img0", img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()
cap.release()