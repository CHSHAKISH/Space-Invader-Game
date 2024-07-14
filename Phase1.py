import pygame
from pygame import mixer
# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('D:\\Coding\\Python\\Space Invaders Game\\background.png').convert()


# Image
enemy = pygame.image.load('D:\Coding\Python\Space Invaders Game\\enemy.png')

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
