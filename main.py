import pygame

# Initialize the pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("assets/player.png")
playerX = SCREEN_WIDTH/2-playerImg.get_width()/2
playerY = 480
playerX_change = 0
speed = 0.3

def player(x,y):
    screen.blit(playerImg, (x, y))

# Game loop
running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        
        # move player left and right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -speed
            if event.key == pygame.K_RIGHT:
                playerX_change = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change
    # border limit on X
    if playerX <= 0:
        playerX = 0
    elif playerX >= SCREEN_WIDTH-playerImg.get_width():
        playerX = SCREEN_WIDTH-playerImg.get_width()
    
    player(playerX, playerY)
    pygame.display.update()