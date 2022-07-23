import random
import cv2 as cv
import pygame
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time

# init
pygame.init()

# create window
width, height = 1280, 720

# display
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game 0")

# FPS init
fps = 30
clock = pygame.time.Clock()

#detector
detector = HandDetector(detectionCon = 0.8, maxHands = 1)

#webcam
cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
#images

imgBalloon = pygame.image.load("Project - GUI/BalloonRed.png").convert_alpha()
rectBalloon = imgBalloon.get_rect()
rectBalloon.x = 500
rectBalloon.y = 500

# main loop
start = True

#variables
speed = 5
score = 0
startTime = time.time()
totalTime = 30

def resetBalloon():
    rectBalloon.x = random.randint(100, img.shape[1] - 100)
    rectBalloon.y = img.shape[0] + 50

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic

    #timing
    timeRemain = int(totalTime - (time.time() - startTime))
    if timeRemain < 0:
        window.fill((55, 55, 55))

        # text
        font = pygame.font.Font("Project - GUI/Marcellus-Regular.ttf", 50)
        textScore = font.render(f"Your Score: {str(score)}", True, (50, 50, 250))
        textTime = font.render(f"Time's Up!", True, (250, 250, 250))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))

    else:
        #openCV
        _, img = cap.read()
        img = cv.flip(img, 1)
        hands, img = detector.findHands(img, flipType = False)

        rectBalloon.y -= speed

        if rectBalloon.y < 0:
            resetBalloon()
            speed += 1

        if hands:
            hand = hands[0]
            x, y = hand["lmList"][8]
            if rectBalloon.collidepoint(x, y):
                resetBalloon()
                score += 10
                speed += 1

        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)

        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))

        window.blit(imgBalloon, rectBalloon)

        #text
        font = pygame.font.Font("Project - GUI/Marcellus-Regular.ttf", 50)
        textScore = font.render(f"Score: {str(score)}", True, (50, 50, 250))
        textTime = font.render(f"Time Left: {str(timeRemain)}", True, (50, 50, 250))
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000, 35))

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
