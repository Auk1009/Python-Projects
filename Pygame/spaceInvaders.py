import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Invaders')

BLUE = (0,0,255)
WHITE = (255,255,255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

playerImg = pygame.image.load('Pygame/Space ship.png')
Enemy_Img = pygame.image.load('Pygame/Space invader.png')
Enemy_X= 370
Enemy_Y= 50
EnemyX_change = 0
EnemyY_change = 0

playerX = 370
PlayerY = 480
playerX_change = 0
PlayerY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(Enemy_Img,(x,y))

running  = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change =0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    player(playerX,PlayerY)
    enemy(Enemy_X,Enemy_Y)
    # player.update()
    # screen.blit(player.image,player.rect)
    pygame.display.update()
playerX += playerX_change
pygame.quit()