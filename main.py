
import random
# import math
import pygame
from pygame import Surface, mixer
import os
from sys import exit

# Initialize the pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")
# .convert_alpha() loads the image into memory keeping transparency from PNG
icon = pygame.image.load(os.path.join('assets','ufo.png')).convert_alpha()
pygame.display.set_icon(icon)

# Background
# convert() loads the image into memory, but removes transparency from PNG
backgroundImg = pygame.image.load(os.path.join('assets','background.png')).convert()

# Background Sound
mixer.music.load("assets/background.wav")
mixer.music.play(-1)

# Player
playerImg = pygame.image.load(os.path.join('assets','player.png')).convert_alpha()
playerX = SCREEN_WIDTH/2-playerImg.get_width()/2
playerY = 480
playerX_change = 0
playerX_speed = 0.5

# Score
score = 0
font = pygame.font.Font(os.path.join('.','FreeSansBold.ttf'), 32)
textX = 10
textY = 10

def show_score():
    render = font.render("Score: "+ str(score), True, (255,255,255))
    screen.blit(render, (textX, textY))

def game_over_text():
    over_font = pygame.font.Font(os.path.join('.','FreeSansBold.ttf'), 70)
    over_text: Surface = over_font.render("GAME OVER", True, (255,0,0))
    screen.blit(over_text, (SCREEN_WIDTH/2-over_text.get_width()/2, SCREEN_HEIGHT/2-over_text.get_height()/2))

# Bullet
bulletImg = pygame.image.load(os.path.join('assets','bullet.png')).convert_alpha()
bulletX = playerX+playerImg.get_width()/2
bulletY = playerY+10
bulletY_speed = 0.4
# ready = invisible
# fire = moving
bullet_state = "ready"
bullet_sound = mixer.Sound("assets/laser.wav")

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
enemyX_speed = 0.2
enemyY_speed = 40 # pixels
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemy_explosion = mixer.Sound("assets/explosion.wav")

change = 0
while change == 0:
    change = random.randint(-1,2)
change *= enemyX_speed

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load(os.path.join('assets','enemy.png')).convert_alpha())
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
                bullet_sound.play()
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
                enemy_explosion.play()
    if bulletY <= 0:
        bulletY = playerY+10
        bullet_state = "ready"

    # Enemy boundary X
    for i in range(number_of_enemies):

        # Game Over
        if enemyY[i] > SCREEN_HEIGHT - playerImg.get_height():
            # hide enemies from screen
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH-enemyImg[i].get_width():
            enemyX_change[i] = -enemyX_change[i]
            enemyY[i] += enemyY_speed
        # Enemy moviment
        enemyX[i] += enemyX_change[i]
        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    show_score()
    pygame.display.update()