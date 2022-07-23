import pygame
import os

# init
pygame.init()

# create window
width, height = 1280, 720

# display
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("GUI")

# FPS init
fps = 30
clock = pygame.time.Clock()

#images
imgBackground = pygame.image.load("Project - GUI/background.png").convert()
imgDesign = pygame.image.load("Project - GUI/design.png").convert_alpha()
imgIcon1 = pygame.image.load("Project - GUI/icon1.png").convert_alpha()
imgIcon2 = pygame.image.load("Project - GUI/icon2.png").convert_alpha()
imgIcon3 = pygame.image.load("Project - GUI/icon3.png").convert_alpha()
imgIcon4 = pygame.image.load("Project - GUI/icon4.png").convert_alpha()
imgIcon5 = pygame.image.load("Project - GUI/icon5.png").convert_alpha()
toggleOn = pygame.image.load("Project - GUI/toggleOn.png").convert()
toggleOff = pygame.image.load("Project - GUI/toggleOff.png").convert()
imgShadow = pygame.image.load("Project - GUI/shadow.png").convert_alpha()

# Colors
colors = {"lightGreen": (189, 209, 197),
     "lightOrange": (238, 204, 140),
     "lightPink": (232, 178, 152),
     "darkPink": (211, 162, 157),
     "darkGreen": (158, 171, 162),
     "darkGray": (128, 126, 126),
     "lightGray": (204, 204, 204),
     "darkBrown": (89, 61, 61),
     "white": (255, 255, 255),
     "black": (0, 0, 0),
     }

#pads
pads = [{"no" : 1, "color" : colors["lightGreen"], "text" : "Original", "icon" : imgIcon2},
    {"no" : 2, "color" : colors["lightOrange"], "text" : "Grayscale", "icon" : imgIcon3},
    {"no" : 3, "color" : colors["lightPink"], "text" : "Edges", "icon" : imgIcon4},
    {"no" : 4, "color" : colors["darkGreen"], "text" : "Contours", "icon" : imgIcon5}]




#draw functions
def drawWindowPad(pos, color, text, icon):

    x0, y0, w, h = pos
    #shadow
    window.blit(imgShadow, (x0, y0 + h - 66))
    #header area
    topH = 64
    pygame.draw.rect(window, color, (x0, y0, w, topH),
                     border_top_left_radius=10, border_top_right_radius=10)
    #main window area
    pygame.draw.rect(window, colors["white"], (x0, y0 + topH, w, h - 87),
                     border_bottom_left_radius=10, border_bottom_right_radius=10)
    window.blit(icon, (x0 + 20, y0 + 12))

    #icon
    window.blit(icon, (x0 +20, y0 + 12))
    #text
    font = pygame.font.Font("Project - GUI/Marcellus-Regular.ttf", 20)
    text = font.render(text, True, colors["darkBrown"])
    window.blit(text, (x0 + 82, y0 + 20))

def drawAll():
    w, h = 312, 301
    coordList = [[484, 57], [868, 57], [484, 433], [868, 433]]
    for i, j in enumerate(coordList):
        drawWindowPad((j[0], j[1], w, h), pads[i]["color"], pads[i]["text"], pads[i]["icon"])
    drawFilterPad()

def drawFilterPad():
    drawWindowPad((75, 57, 312, 602,), colors["darkGreen"], "Filter", imgIcon1)

    font = pygame.font.Font("Project - GUI/Marcellus-Regular.ttf", 20)
    #1
    textDisp1 = font.render("Gray Scale", True, colors["darkBrown"])
    window.blit(textDisp1, (106, 165))
    window.blit(toggleOn, (283, 164))
    #2
    textDisp2 = font.render("Edges", True, colors["darkBrown"])
    window.blit(textDisp2, (106, 165 + 60))
    window.blit(toggleOn, (283, 164 + 60))
    #3
    textDisp3 = font.render("Contours", True, colors["darkBrown"])
    window.blit(textDisp3, (106, 165 + 60 * 2))
    window.blit(toggleOff, (283, 164 + 60 * 2))
    #4
    textDisp4 = font.render("Blur", True, colors["darkBrown"])
    window.blit(textDisp4, (106, 165 + 60 * 3))
    window.blit(toggleOff, (283, 164 + 60 * 3))
    #Sliders
    font = pygame.font.Font("Project - GUI/Marcellus-Regular.ttf", 25)
    for y in range(0, 4):
        h = 447 + y * 55
        sliderPos = 105 + 50 * y + 30
        pygame.draw.line(window, colors["lightGray"], (105, h), (260, h), 5)
        pygame.draw.line(window, colors["darkGray"], (105, h), (sliderPos, h), 5)
        pygame.draw.rect(window, colors["darkGray"], (sliderPos, h - 15, 12, 30))
        textDisp = font.render(str(y * 50 + 30), True, colors["darkBrown"])
        window.blit(textDisp, (286, h - 18))



# main loop
start = True

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    #window.fill((66, 66, 66))

    window.blit(imgBackground, (0, 0))
    # imgDesign.set_alpha(20)

    #window.blit(imgDesign, (0, 0))

    drawAll()


    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
