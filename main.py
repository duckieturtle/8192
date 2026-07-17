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

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#FFEBCD")

    # RENDER YOUR GAME HERE
    for x in range(4):
        for y in range(4):
            value = tiles[y*4+x]
            
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
