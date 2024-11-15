import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space invaders V2.0')

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
# player
player_img = pygame.image.load('Pygame/Space ship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
# Enemy
enemy_img = pygame.image.load('Pygame/Space invader.png')
enemyX = 350
enemyY = 100
enemyX_change = 0.3
enemyY_change = 40

# bullet
bullet_img = pygame.image.load('Pygame/Bullet Icon.png')
bulletX = 0
bulletY = 480
bullety_change = 0.5
bullet_status = 'ready'


def player_coord(x,y):
    screen.blit(player_img,(x,y))
    # screen.blit("-")

def enemy_coord(x,y):
    screen.blit(enemy_img,(x,y))

def bullet_coord(x,y):
    screen.blit(bullet_img,(x,y))
    bullet_status = 'fire'


running = True
while running:
    screen.fill(BLACK)
    player_coord(playerX,playerY)
    enemy_coord(enemyX,enemyY)
    bullet_coord(playerX,bulletY)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
                

            if event.key == pygame.K_RIGHT:
                 playerX_change = 0.4
            
            if event.key == pygame.K_UP:
             playerY_change = -0.4
            
            if event.key == pygame.K_DOWN:
                playerY_change = 0.4
            if event.key == pygame.K_SPACE:
                playerX = bulletX
                bullet_coord(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0
# x barriar
    if playerX <= 0:
        playerX =0
    if playerX >= 736:
        playerX = 736
# y barriar
    if playerY <= 0:
        playerY =0
    if playerY >= 536:
        playerY = 536
# Barrier
    if enemyX >= 736:
        enemyX = 736
    if enemyX <= 0:
        enemyX = 0
    #change in direction 
    if enemyX == 736 or enemyX == 0:
        enemyX_change *= -1
        enemyY += enemyY_change
    #edge
    if playerY <= 400:
        playerY = 400

    if bullet_status == 'fire':
        enemyY+= enemyY_change


    playerX += playerX_change
    playerY += playerY_change
    enemyX += enemyX_change
    pygame.display.update()    
    

pygame.quit()