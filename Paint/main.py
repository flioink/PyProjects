import pygame
pygame.init()
import os
from datetime import datetime

fps = 240
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("paint")
run = True
activeSize = 0
activeColor = (255, 255, 255)
paintingList = []

def drawMenu(activeSize, activeColor):
    pygame.draw.rect(screen, "gray", [0, 0, WIDTH, 70])
    pygame.draw.line(screen, "black", (0, 70), (WIDTH, 70), 3)

    xlBrush = pygame.draw.rect(screen, "black", [10, 10, 50, 50])
    pygame.draw.circle(screen, "white", (35, 35), 20) #
    lBrush = pygame.draw.rect(screen, "black", [70, 10, 50, 50])
    pygame.draw.circle(screen, "white", (95, 35), 15) #
    mBrush = pygame.draw.rect(screen, "black", [130, 10, 50, 50])
    pygame.draw.circle(screen, "white", (155, 35), 10) #
    sBrush = pygame.draw.rect(screen, "black", [190, 10, 50, 50])
    pygame.draw.circle(screen, "white", (215, 35), 5)  #
    brushList = [xlBrush, lBrush, mBrush, sBrush]

    if activeSize == 20:
        pygame.draw.rect(screen, "dark gray", [10, 10, 50, 50], 3)
    elif activeSize == 15:
        pygame.draw.rect(screen, "dark gray", [70, 10, 50, 50], 3)
    elif activeSize == 10:
        pygame.draw.rect(screen, "dark gray", [130, 10, 50, 50], 3)
    elif activeSize == 5:
        pygame.draw.rect(screen, "dark gray", [190, 10, 50, 50], 3)


    pygame.draw.circle(screen, activeColor, (400, 35), 30)
    pygame.draw.circle(screen, "dark gray", (400, 35), 30, 3)

    blue = pygame.draw.rect(screen, "blue", [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, "red", [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, "green", [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, "yellow", [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, "teal", [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, "purple", [WIDTH - 85, 35, 25, 25])
    white = pygame.draw.rect(screen, "white", [WIDTH - 110, 10, 25, 25])
    black = pygame.draw.rect(screen, "black", [WIDTH - 110, 35, 25, 25])

    colorRect = [blue, red, green, yellow, teal, purple, white, black]

    rgbList = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255),
               (255, 0, 255), (255, 255, 255), (0, 0, 0)]

    return brushList, colorRect, rgbList

def drawPainting(pList):
    for i in range(len(pList)):
        pygame.draw.circle(screen, pList[i][0], pList[i][1], pList[i][2])

def check():
    path = os.path.abspath("D:\ZBrush 2020.1.4\Prop_stock")
    currDate = datetime.now()
    day = currDate.day
    month = currDate.month

    fileList = os.listdir(path)
    fileList = [x for x in fileList if x[-1].isdigit()]
    fileList = sorted(fileList)
    with open(f"listOfTasks{day}_{month}.txt", "w") as file:
        for item in fileList:
            file.writelines(item + "\n")

check()

while run:
    timer.tick(fps)

    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    leftClick = pygame.mouse.get_pressed()[0]
    brushes, colors, rgbs = drawMenu(activeSize, activeColor)

    if leftClick and mouse[1] > 70:
        paintingList.append((activeColor, mouse, activeSize))

    drawPainting(paintingList)

    if mouse[1] > 70:
        pygame.draw.circle(screen, activeColor, mouse, activeSize)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    activeSize = 20 - (i * 5)

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    activeColor = rgbs[i]


    pygame.display.flip()


pygame.quit()

