
import random
import math
import pygame
from pygame import mixer

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

# Background Sound
mixer.music.load("assets/background.wav")
mixer.music.play(-1)

# Player
playerImg = pygame.image.load("assets/player.png")
playerX = SCREEN_WIDTH/2-playerImg.get_width()/2
playerY = 480
playerX_change = 0
playerX_speed = 5

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

def show_score():
    render = font.render("Score: "+ str(score), True, (255,255,255))
    screen.blit(render, (textX, textY))

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

def isCollision(eX, eY, bulletX, bulletY, i):
    #distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    #return distance < 27
    
    if eX <= bulletX+bulletImg.get_width()/2 <= eX+enemyImg[i].get_width():
        if eY <= bulletY <= eY+enemyImg[i].get_height():
            return True
    return False

# Enemy
def enemy_position(i):
    return random.randint(0,SCREEN_WIDTH-enemyImg[i].get_width()), random.randint(0, 150)

number_of_enemies = 6
enemyX_speed = 4
enemyY_speed = 40 # pixels
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []

change = 0
while change == 0:
    change = random.randint(-1,2)
change *= enemyX_speed

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load("assets/enemy.png"))
    x, y = enemy_position(i)
    enemyX.append(x)
    enemyY.append(y)
    enemyX_change.append(change)

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))

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
            if event.key == pygame.K_SPACE and bullet_state == "ready":
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
        for i in range(number_of_enemies):
            if isCollision(enemyX[i], enemyY[i], bulletX, bulletY, i):
                bulletY = playerY+10
                bullet_state = "ready"
                score += 1
                enemyX[i], enemyY[i] = enemy_position(i)
    if bulletY <= 0:
        bulletY = playerY+10
        bullet_state = "ready"

    # Enemy boundary X
    for i in range(number_of_enemies):
        if enemyX[i] <= 0:
            enemyX_change[i] = enemyX_speed
            enemyY[i] += enemyY_speed
        elif enemyX[i] >= SCREEN_WIDTH-enemyImg[i].get_width():
            enemyX_change[i] = -enemyX_speed
            enemyY[i] += enemyY_speed
        # Enemy moviment
        enemyX[i] += enemyX_change[i]
        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    show_score()
    pygame.display.update()