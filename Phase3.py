import pygame
from pygame import mixer
# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('D:\\Coding\\Python\\Space Invaders Game\\background.png').convert()

#Background Music
mixer.music.load("D:\\Coding\\Python\\Space Invaders Game\\background.wav")
mixer.music.play(-1)

#Caption and Icon
pygame.display.set_caption("Space Invader Game")
icon = pygame.image.load('D:\\Coding\\Python\\Space Invaders Game\\ufo.png').convert()
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('D:\\Coding\\Python\\Space Invaders Game\\player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Image
enemy = pygame.image.load('D:\Coding\Python\Space Invaders Game\\enemy.png')

def player(x,y):
    screen.blit(playerImg, (x,y))

a = b = c = d = 1

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
 
    # Background Image
    screen.blit(background, (0, 0))

    screen.blit(enemy, (a,100))
    a += 1
    screen.blit(enemy, (b,10))
    b += 2
    screen.blit(enemy, (c,200))
    c += 3
    screen.blit(enemy, (d,140))
    d += 4
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    player(playerX, playerY)
    pygame.display.update()

