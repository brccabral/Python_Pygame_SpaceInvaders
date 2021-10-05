import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("assets/player.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
    
    screen.fill((0,0,0))
    
    player()
    pygame.display.update()