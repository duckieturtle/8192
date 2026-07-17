# Example file showing a basic pygame "game loop"
import pygame
pygame.init()

# configuration
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
TILE_SIZE = SCREEN_HEIGHT/4

TILE_FONT = pygame.font.SysFont("Arial", 35)

# pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

tiles = [
    0,1,0,1,
    2,1,7,3,
    4,1,1,2,
    0,0,0,3
]

tiles = [
    1,0,1,0,
    2,1,7,3,
    4,2,2,0,
    0,0,3,0
]

colors = [
    "#FFEBCD", # 0
    "green", # 2
    "darkgreen", # 4
    "orangered", # 8
    "orangered3", # 16
    "orangered4", # 32
    "olive", # 64
    "olivedrab", # 128
    "olivedrab1", # 256
    "olivedrab3", # 512
    "aqua", # 1024
]

def get_index(x, y):
    return y*4+x

def get_x(index):
    return index % 4

def get_y(index):
    return index // 4

def move_tiles_right():
    global tiles
    for x in range(3, -1, -1):
        for y in range(3, -1, -1):
            if x == 3 or tiles[get_index(x, y)] == 0:
                continue
            new_index = get_index(x + 1, y)
            if tiles[new_index] == tiles[get_index(x, y)]:
                tiles[new_index] = tiles[get_index(x, y)] + 1
                tiles[get_index(x, y)] = 0
            elif tiles[new_index] != 0:
                continue
            else:
                tiles[new_index] = tiles[get_index(x, y)]
                tiles[get_index(x, y)] = 0

def move_tiles_down():
    global tiles
    for x in range(3, -1, -1):
        for y in range(3, -1, -1):
            if y == 3 or tiles[get_index(x, y)] == 0:
                continue
            new_index = get_index(x, y + 1)
            if tiles[new_index] == tiles[get_index(x, y)]:
                tiles[new_index] = tiles[get_index(x, y)] + 1
                tiles[get_index(x, y)] = 0
            elif tiles[new_index] != 0:
                continue
            else:
                tiles[new_index] = tiles[get_index(x, y)]
                tiles[get_index(x, y)] = 0

def move_tiles_left():
    global tiles
    for x in range(4):
        for y in range(4):
            if x == 0 or tiles[get_index(x, y)] == 0:
                continue
            new_index = get_index(x - 1, y)
            if tiles[new_index] == tiles[get_index(x, y)]:
                tiles[new_index] = tiles[get_index(x, y)] + 1
                tiles[get_index(x, y)] = 0
            elif tiles[new_index] != 0:
                continue
            else:
                tiles[new_index] = tiles[get_index(x, y)]
                tiles[get_index(x, y)] = 0

def move_tiles_up():
    global tiles
    for x in range(4):
        for y in range(4):
            if y == 0 or tiles[get_index(x, y)] == 0:
                continue
            new_index = get_index(x, y - 1)
            if tiles[new_index] == tiles[get_index(x, y)]:
                tiles[new_index] = tiles[get_index(x, y)] + 1
                tiles[get_index(x, y)] = 0
            elif tiles[new_index] != 0:
                continue
            else:
                tiles[new_index] = tiles[get_index(x, y)]
                tiles[get_index(x, y)] = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            move_tiles_right()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            move_tiles_down()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            move_tiles_left()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            move_tiles_up()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#FFEBCD")

    # RENDER YOUR GAME HERE
    for x in range(4):
        for y in range(4):
            value = tiles[get_index(x, y)]
            
            pygame.draw.rect(screen, colors[value], (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

            if value != 0:
                number_image = TILE_FONT.render(str(2**value),True,"black")
                screen.blit(number_image, (
                    x*SCREEN_WIDTH/4 + TILE_SIZE / 2 - number_image.get_width() / 2,
                    y*SCREEN_WIDTH/4 + TILE_SIZE / 2 - number_image.get_height() / 2
                ))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
