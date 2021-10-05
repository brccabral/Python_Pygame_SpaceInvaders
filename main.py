
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

# Background
backgroundImg = pygame.image.load("assets/background.png")

# Player
playerImg = pygame.image.load("assets/player.png")
playerX = SCREEN_WIDTH/2-playerImg.get_width()/2
playerY = 480
playerX_change = 0
playerX_speed = 5

# Bullet
bulletImg = pygame.image.load("assets/bullet.png")
bulletX = playerX+playerImg.get_width()/2
bulletY = playerY+10
bulletY_speed = 6
# ready = invisible
# fire = moving
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+playerImg.get_width()/2,y+10))


# Enemy
enemyImg = pygame.image.load("assets/enemy.png")
enemyX = random.randint(0,SCREEN_WIDTH-enemyImg.get_width())
enemyY = random.randint(0, 150)
enemyX_speed = 4
enemyX_change = 0
while enemyX_change==0:
    enemyX_change = random.randint(-1,2)
enemyX_change *= enemyX_speed
enemyY_speed = 40 # pixels

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

# Game loop
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(backgroundImg,(0,0))

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
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change
    # border limit on X
    if playerX <= 0:
        playerX = 0
    elif playerX >= SCREEN_WIDTH-playerImg.get_width():
        playerX = SCREEN_WIDTH-playerImg.get_width()
    
    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_speed
    if bulletY <= 0:
        bulletY = playerY+10
        bullet_state = "ready"

    # Enemy boundary X
    if enemyX <= 0:
        enemyX_change = enemyX_speed
        enemyY += enemyY_speed
    elif enemyX >= SCREEN_WIDTH-enemyImg.get_width():
        enemyX_change = -enemyX_speed
        enemyY += enemyY_speed
    # Enemy moviment
    enemyX += enemyX_change
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()