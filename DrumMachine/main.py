#Original design by LeMaster Tech
import pygame
from pygame import mixer

pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)
darkGray = (99, 99, 99)
lightGray = (170, 170, 170)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Drum Maker")
labelFont = pygame.font.Font("freesansbold.ttf", 30)
mediumFont = pygame.font.Font("freesansbold.ttf", 20)

#variables
index = 100
fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
run = True
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
activeList = [1 for _ in range(instruments)]
bpm = 240
playing = True
activeLength = 0
activeBeat = 1
beatChanged = True
saveMenu = False
loadMenu = False
savedBeats = []
beatName = ""
typing = False
try:
    file = open("savedBeats.txt", "r")
    for line in file:
        if not line.isspace():
            savedBeats.append(line)
except :
    file = open("savedBeats.txt", "w")

#load sounds
hiHat = mixer.Sound("sounds/hi hat.WAV")
snare = mixer.Sound("sounds/snare.WAV")
kick = mixer.Sound("sounds/kick.WAV")
crash = mixer.Sound("sounds/crash.WAV")
clap = mixer.Sound("sounds/clap.WAV")
tom = mixer.Sound("sounds/tom.WAV")
pygame.mixer.set_num_channels(instruments * 3)

def playNotes():
    for i in range(len(clicked)):
        if clicked[i][activeBeat] == 1 and activeList[i] == 1:
            if i == 0:
                hiHat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()



def drawGrid(clicks, beat, actives):
    leftBox = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottomBox = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []


    colors = [gray, white, gray]
    hiHatText = labelFont.render("Hi Hat", True, colors[actives[0]])
    screen.blit(hiHatText, (30, 30))
    snareText = labelFont.render("Snare", True, colors[actives[1]])
    screen.blit(snareText, (30, 130))
    kickText = labelFont.render("Bass Drum", True, colors[actives[2]])
    screen.blit(kickText, (30, 230))
    crashText = labelFont.render("Crash", True, colors[actives[3]])
    screen.blit(crashText, (30, 330))
    clapText = labelFont.render("Clap", True, colors[actives[4]])
    screen.blit(clapText, (30, 430))
    floorTomText = labelFont.render("Floor Tom", True, colors[actives[5]])
    screen.blit(floorTomText, (30, 530))

    for i in range(6):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)

    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = gray
            else:
                if actives[j] == 1:
                    color = green
                else:
                    color = darkGray

            rect = pygame.draw.rect(screen, color, [i * ((WIDTH - 200) // beats) + 205, (j * 100) + 5, ((WIDTH - 200)//beats) - 10,
                                                   ((HEIGHT - 200)//instruments) - 10], 0, 0)

            pygame.draw.rect(screen, gold,
                                    [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats),
                                     ((HEIGHT - 200) // instruments)], 6, 5)

            pygame.draw.rect(screen, black,
                             [i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats),
                              ((HEIGHT - 200) // instruments)], 2, 5)

            boxes.append((rect, (i, j)))

        active = pygame.draw.rect(screen, blue, [beat * ((WIDTH - 200) // beats) + 200, 0, ((WIDTH - 200) // beats), instruments * 100], 5, 3)

    return boxes

def drawSaveMenu(beatName, typing):
    pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT])
    menuText = labelFont.render("Save Menu : Enter a name for the current beat", True, white)
    savingBtn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 200, HEIGHT * 0.75, 400, 100], 0, 5)
    savingText = labelFont.render("Save Beat", True, white)
    screen.blit(savingText, (WIDTH // 2 - 70, HEIGHT * 0.75 + 30))
    screen.blit(menuText, (400, 40))
    exitBtn = pygame.draw.rect(screen, gray, [WIDTH - 200, HEIGHT - 100, 180, 90], 0, 5)
    exitText = labelFont.render("Close", True, white)
    screen.blit(exitText, (WIDTH - 160, HEIGHT - 70))
    if typing:
        pygame.draw.rect(screen, darkGray, [400, 200, 600, 200], 0, 5)
    entryRect = pygame.draw.rect(screen, gray, [400, 200, 600, 200], 5, 5)
    entryText = labelFont.render(f"{beatName}", True, white)
    screen.blit(entryText, (430, 250))
    return exitBtn, savingBtn, entryRect

def drawLoadMenu(index):
    loadedClicked = []
    loadedBeats = 0
    loadedBpm = 0

    pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT])


    menuText = labelFont.render("Load Menu : select a beat to load", True, white)
    loadingBtn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 200, HEIGHT * 0.87, 400, 100], 0, 5)
    loadingText = labelFont.render("Load Beat", True, white)
    screen.blit(loadingText, (WIDTH // 2 - 70, HEIGHT * 0.87 + 30))
    screen.blit(menuText, (400, 40))
    deleteBtn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 500, HEIGHT * 0.87, 200, 100], 0, 5)
    deleteTxt = labelFont.render("Delete beat", True, white)
    screen.blit(deleteTxt, ((WIDTH//2) - 485, HEIGHT * 0.87 + 30))

    exitBtn = pygame.draw.rect(screen, gray, [WIDTH - 200, HEIGHT - 100, 180, 90], 0, 5)
    exitText = labelFont.render("Close", True, white)
    screen.blit(exitText, (WIDTH - 160, HEIGHT - 70))
    loadedRect = pygame.draw.rect(screen, gray, [190, 90, 1000, 600], 5, 5)

    if 0 <= index < len(savedBeats):
        pygame.draw.rect(screen, lightGray, [190, 100 + index * 50, 1000, 50])

    for beat in range(len(savedBeats)):
        if i < 10 :
            beatClicked = []
            rowText = mediumFont.render(f"{beat + 1}", True, white)
            screen.blit(rowText, (200, 100 + beat * 50))
            nameIndexStart = savedBeats[beat].index("name: ") + 6

            nameIndexEnd = savedBeats[beat].index(", beats:")
            nameText = mediumFont.render(savedBeats[beat][nameIndexStart : nameIndexEnd], True, white)
            screen.blit(nameText, (240, 100 + beat * 50))

        if 0 <= index < len(savedBeats) and beat == index:
            beatsIndexEnd = savedBeats[beat].index(", bpm:")
            loadedBeats = int(savedBeats[beat][nameIndexEnd + 8 : beatsIndexEnd])
            bpmIndexEnd = savedBeats[beat].index(", selected:")
            loadedBpm = int(savedBeats[beat][beatsIndexEnd + 6 : bpmIndexEnd])

            loadedClicksStr = savedBeats[beat][bpmIndexEnd + 14 : -3]
            loadedClicksRows = list(loadedClicksStr.split("], ["))
            for row in range(len(loadedClicksRows)):
                loadedClicksRow = loadedClicksRows[row].split(", ")
                for item in range(len(loadedClicksRow)):
                    if loadedClicksRow[item] == "1" or loadedClicksRow[item] == "-1":
                        loadedClicksRow[item] = int(loadedClicksRow[item])
                beatClicked.append(loadedClicksRow)
                loadedClicked = beatClicked

    loadedInfo = [loadedBeats, loadedBpm, loadedClicked]
    entryRect = pygame.draw.rect(screen, gray, [190, 90, 1000, 600], 5, 5)
    return exitBtn, loadingBtn, entryRect, deleteBtn, loadedInfo



while run:
    timer.tick(fps)
    screen.fill(black)


    boxes = drawGrid(clicked, activeBeat, activeList)
    # lower menu buttons
    playPause = pygame.draw.rect(screen, gray, [50, HEIGHT - 150, 200, 100], 0, 5)
    playText = labelFont.render("Play/Pause", True, white)
    screen.blit(playText, (70, HEIGHT - 130))

    if playing:
        playText2 = mediumFont.render("Playing", True, darkGray)
    else:
        playText2 = mediumFont.render("Paused", True, darkGray)
    screen.blit(playText2, (70, HEIGHT - 100))

    #bpm adjust
    bpmRect = pygame.draw.rect(screen, gray, [300, HEIGHT - 150, 200, 100], 5, 5)
    bpmText = mediumFont.render("Beats per minute", True, white)
    screen.blit(bpmText, (308, HEIGHT - 130))
    bpmText2 = labelFont.render(f"{bpm}", True, white)
    screen.blit(bpmText2, (370, HEIGHT - 100))
    bpmAddRect = pygame.draw.rect(screen, gray, [510, HEIGHT - 150, 48, 48], 0, 5)
    bpmSubRect = pygame.draw.rect(screen, gray, [510, HEIGHT - 100, 48, 48], 0, 5)
    addText = mediumFont.render("+5", True, white)
    subText = mediumFont.render("-5", True, white)
    screen.blit(addText, (520, HEIGHT - 140))
    screen.blit(subText, (520, HEIGHT - 90))

    # bpm add/remove
    beatsRect = pygame.draw.rect(screen, gray, [600, HEIGHT - 150, 200, 100], 5, 5)
    beatsText = mediumFont.render("Beats in Loop", True, white)
    screen.blit(beatsText, (618, HEIGHT - 130))
    beatsText2 = labelFont.render(f"{beats}", True, white)
    screen.blit(beatsText2, (680, HEIGHT - 100))
    beatsAddRect = pygame.draw.rect(screen, gray, [810, HEIGHT - 150, 48, 48], 0, 5)
    beatsSubRect = pygame.draw.rect(screen, gray, [810, HEIGHT - 100, 48, 48], 0, 5)
    addText2 = mediumFont.render("+1", True, white)
    subText2 = mediumFont.render("-1", True, white)
    screen.blit(addText2, (820, HEIGHT - 140))
    screen.blit(subText2, (820, HEIGHT - 90))

    #instruments rects
    instrumentRects = []
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i * 100), (200, 100))
        instrumentRects.append(rect)


    # saving and loading
    saveButton = pygame.draw.rect(screen, gray, [900, HEIGHT - 150, 200, 48], 0, 5)
    saveText = labelFont.render("Save Beat", True, white)
    screen.blit(saveText, (920, HEIGHT - 140))
    loadButton = pygame.draw.rect(screen, gray, [900, HEIGHT - 100, 200, 48], 0, 5)
    loadText = labelFont.render("Load Beat", True, white)
    screen.blit(loadText, (920, HEIGHT - 90))

    # clear board
    clearButton = pygame.draw.rect(screen, gray, [1150, HEIGHT - 150, 200, 100], 0, 5)
    clearText = labelFont.render("Clear Board", True, white)
    screen.blit(clearText, (1160, HEIGHT - 115))

    if saveMenu:
        exitButton, savingButton, entryRectangle = drawSaveMenu(beatName, typing)

    if loadMenu:
        exitButton, loadingButton, entryRectangle, deleteButton, loadedInfo = drawLoadMenu(index)#
    if beatChanged:
        playNotes()
        beatChanged = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not saveMenu and not loadMenu:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1

        if event.type == pygame.MOUSEBUTTONUP and not saveMenu and not loadMenu:
            if playPause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:
                    playing = True

            elif bpmAddRect.collidepoint(event.pos):
                bpm += 5
            elif bpmSubRect.collidepoint(event.pos):
                bpm -= 5

            elif beatsAddRect.collidepoint(event.pos):
                beats += 1
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif beatsSubRect.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
            elif clearButton.collidepoint(event.pos):
                #RESET
                clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
            elif saveButton.collidepoint(event.pos):
                saveMenu = True
            elif loadButton.collidepoint(event.pos):
                loadMenu = True

            for i in range(len(instrumentRects)):
                if instrumentRects[i].collidepoint(event.pos):
                    activeList[i] *= -1
        elif event.type == pygame.MOUSEBUTTONUP:
            if exitButton.collidepoint(event.pos):
                saveMenu = False
                loadMenu = False
                playing = True
                beatName = ""
                typing = False

            if saveMenu:
                if entryRectangle.collidepoint(event.pos):
                    if typing:
                        typing = False
                    elif not typing:
                        typing = True

                if savingButton.collidepoint(event.pos):
                    file = open("savedBeats.txt", "w")
                    savedBeats.append(f"name: {beatName}, beats: {beats}, bpm: {bpm}, selected: {clicked}")
                    for i in range(len(savedBeats)):
                        if i == 0 and not savedBeats[i].isspace():
                            file.write(str(savedBeats[i]))
                        else:
                            if not savedBeats[i].isspace():
                                file.write("\n" + str(savedBeats[i]))
                    file.close()
                    print(savedBeats)

                    saveMenu = False
                    typing = False
                    beatName = ""

            if loadMenu:
                if deleteButton.collidepoint(event.pos):
                    print("del press")
                    if 0 <= index < len(savedBeats):
                        savedBeats.pop(index)

                        #Add
                        

                if entryRectangle.collidepoint(event.pos):
                    index = (event.pos[1] - 100) // 50

                if loadingButton.collidepoint(event.pos):
                    if 0 <= index < len(savedBeats):
                        beats = loadedInfo[0]
                        bpm = loadedInfo[1]
                        clicked = loadedInfo[2]
                        index = 100
                        save_menu = False
                        load_menu = False
                        playing = True
                        typing = False

        if event.type == pygame.TEXTINPUT and typing:
            beatName += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(beatName) > 0 and typing:
                beatName = beatName[:-1]

    beatLength = 3600 // bpm

    if playing:
        if activeLength < beatLength:
            activeLength += 1
        else:
            activeLength = 0
            if activeBeat < beats - 1:
                activeBeat += 1
                beatChanged = True
            else:
                activeBeat = 0
                beatChanged = True



    pygame.display.flip()

pygame.quit()