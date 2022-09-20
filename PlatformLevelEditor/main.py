# Original design by LeMasterTech
import pygame
pygame.init()

# set window
WIDTH = 1800
HEIGHT = 900
TILE_SIZE = 100
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 60
timer = pygame.time.Clock()
pygame.display.set_caption("Level Editor")

level = [[0 for _ in range(18)]for _ in range(7)]
level.append([2 for _ in range(18)])
level.append([1 for _ in range(18)])
active_level = 0
active_phase = 3

# load images

bg = pygame.image.load("assets/images/space bg.png")
rock = pygame.transform.scale(pygame.image.load("assets/images/tiles/rock.png"), (100, 100))
ground = pygame.transform.scale(pygame.image.load("assets/images/tiles/ground.png"), (100, 100))
platform = pygame.transform.scale(pygame.image.load("assets/images/tiles/platform.png"), (100, 50))
acid = pygame.transform.scale(pygame.image.load("assets/images/tiles/acid.png"), (100, 25))
# keys
blueKey = pygame.transform.scale(pygame.image.load("assets/images/keycards/key_blue.png"), (60, 100))
greenKey = pygame.transform.scale(pygame.image.load("assets/images/keycards/key_green.png"), (60, 100))
redKey = pygame.transform.scale(pygame.image.load("assets/images/keycards/key_red.png"), (60, 100))
yellowKey = pygame.transform.scale(pygame.image.load("assets/images/keycards/key_yellow.png"), (60, 100))
# doors
blueDoor = pygame.transform.scale(pygame.image.load("assets/images/portals/blue.png"), (100, 100))
greenDoor = pygame.transform.scale(pygame.image.load("assets/images/portals/green.png"), (100, 100))
redDoor = pygame.transform.scale(pygame.image.load("assets/images/portals/red.png"), (100, 100))
yellowDoor = pygame.transform.scale(pygame.image.load("assets/images/portals/yellow.png"), (100, 100))
tiles = ["", rock, ground, platform, acid]
keys = [blueKey, greenKey, redKey, yellowKey]
doors = [blueDoor, greenDoor, redDoor, yellowDoor]
frames = []
playerScale = 14
for _ in range(1, 5):
    frames.append(pygame.transform.scale(pygame.image.load(f"assets/images/astronaut/{_}.png"),
                                         (playerScale * 5, playerScale * 8)))

run = True

def drawInventory():
    font = pygame.font.Font('freesansbold.ttf', 20)
    colors = ['blue', 'green', 'red', 'yellow']
    pygame.draw.rect(screen, 'black', [5, HEIGHT - 120, WIDTH - 10, 110], 0, 5)
    pygame.draw.rect(screen, 'purple', [5, HEIGHT - 120, WIDTH - 10, 110], 3, 5)
    pygame.draw.rect(screen, 'white', [8, HEIGHT - 117, 340, 104], 3, 5)
    pygame.draw.rect(screen, 'white', [348, HEIGHT - 117, 532, 104], 3, 5)
    pygame.draw.rect(screen, 'white', [880, HEIGHT - 117, 910, 104], 3, 5)
    font.italic = True
    inst_text = font.render('Left/Right Click On Spaces', True, 'white')
    inst_text2 = font.render('Or Scroll Wheel', True, 'white')
    inst_text3 = font.render('Press Enter to Print to Console', True, 'white')
    inst_text4 = font.render('Then Copy to Levels.py', True, 'white')
    screen.blit(inst_text, (14, HEIGHT - 113))
    screen.blit(inst_text2, (14, HEIGHT - 88))
    screen.blit(inst_text3, (14, HEIGHT - 63))
    screen.blit(inst_text4, (14, HEIGHT - 38))
    font = pygame.font.Font('freesansbold.ttf', 32)
    level_text = font.render(f'Level: {active_level + 1}', True, 'white')
    screen.blit(level_text, (354, HEIGHT - 110))
    phase_strings = ['Blue', 'Green', 'Red', 'Gold']
    phase_text = font.render(f'Phase: {phase_strings[active_phase]}', True, colors[active_phase])
    screen.blit(phase_text, (354, HEIGHT - 50))
    plus_lvl = pygame.draw.rect(screen, 'gray', [600, HEIGHT - 110, 40, 40], 0, 5)
    minus_lvl = pygame.draw.rect(screen, 'gray', [660, HEIGHT - 110, 40, 40], 0, 5)
    plus_phase = pygame.draw.rect(screen, 'gray', [600, HEIGHT - 60, 40, 40], 0, 5)
    minus_phase = pygame.draw.rect(screen, 'gray', [660, HEIGHT - 60, 40, 40], 0, 5)
    plus_text = font.render('+', True, 'black')
    screen.blit(plus_text, (613, HEIGHT - 107))
    screen.blit(plus_text, (613, HEIGHT - 57))
    minus_text = font.render('-', True, 'black')
    screen.blit(minus_text, (675, HEIGHT - 107))
    screen.blit(minus_text, (675, HEIGHT - 57))

    font = pygame.font.Font('freesansbold.ttf', 44)
    enter_text = font.render('Use the mouse to design the levels', True, 'white')
    screen.blit(enter_text, (900, HEIGHT - 90))

    return [plus_lvl, minus_lvl, plus_phase, minus_phase]

def drawBoard(board):
    # below ground - 1, walkable ground - 2, platform - 3, acid - 4, 5 - spawn  point, 6-9 keys, 10-13 portals
    for q in range(len(board)):
        for j in range(len(board[q])):
            if board[q][j] != 0:
                value = board[q][j]
                if 0 < value < 4:
                    screen.blit(tiles[value], (j * TILE_SIZE, q * TILE_SIZE))
                elif value == 4:
                    screen.blit(tiles[value], (j * TILE_SIZE, q * TILE_SIZE + 75))
                elif value == 5:
                    screen.blit(frames[0], (j * TILE_SIZE, q * TILE_SIZE - 10))
                elif 6 <= value < 10:
                    screen.blit(keys[value - 6], (j * TILE_SIZE + 20, q * TILE_SIZE))
                elif 10 <= value <= 13:
                    screen.blit(doors[value - 10], (j * TILE_SIZE, q * TILE_SIZE))



while run:
    timer.tick(fps)
    screen.blit(bg, (0, 0))

    drawBoard(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                boardStr = "["
                for i in range(len(level)):
                    boardStr += str(level[i]) + ',\n'
                boardStr += "]"
                print(boardStr)
        # event handling for changing tiles with the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # convert mouse pos into tiles pos
            coords = pygame.mouse.get_pos()[0] // 100, pygame.mouse.get_pos()[1] // 100
            if event.button == 1 or event.button == 4:
                # +1
                if level[coords[1]][coords[0]] < 13:
                    level[coords[1]][coords[0]] += 1
                else:
                    level[coords[1]][coords[0]] = 0

            elif event.button == 3 or event.button == 5:
                # -1
                if level[coords[1]][coords[0]] > 0:
                    level[coords[1]][coords[0]] -= 1
                else:
                    level[coords[1]][coords[0]] = 13


    pygame.display.flip()

pygame.quit()
