
import random
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
playerX_speed = 0.3

# Enemy
enemyImg = pygame.image.load("assets/enemy.png")
enemyX = random.randint(0,SCREEN_WIDTH-enemyImg.get_width())
enemyY = random.randint(0, 150)
enemyX_speed = 0.25
enemyX_change = enemyX_speed
enemyY_speed = 40 # pixels

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

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
                playerX_change = -playerX_speed
            if event.key == pygame.K_RIGHT:
                playerX_change = playerX_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change
    # border limit on X
    if playerX <= 0:
        playerX = 0
    elif playerX >= SCREEN_WIDTH-playerImg.get_width():
        playerX = SCREEN_WIDTH-playerImg.get_width()

    # Enemy boundary X
    if enemyX <= 0:
        enemyX_change = enemyX_speed
    elif enemyX >= SCREEN_WIDTH-enemyImg.get_width():
        enemyX_change = -enemyX_speed
    # Enemy moviment
    enemyX += enemyX_change
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()