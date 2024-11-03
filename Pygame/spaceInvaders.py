import pygame
import random

pygame.init()

background = pygame.image.load('Pygame/Space Galaxy Background.jpg')
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Invaders')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Images
playerImg = pygame.image.load('Pygame/Space ship.png')
Enemy_Img = pygame.image.load('Pygame/Space invader.png')
bullet_Img = pygame.image.load('Pygame/Bullet Icon.png')

#Enemy
Enemy_X= random.randint(1,750)
Enemy_Y= random.randint(50,150)
EnemyX_change = 0.1
EnemyY_change = 40

#Player
playerX = 370
PlayerY = 480
playerX_change = 0

#bullet
bullet_X= 0
bullet_Y= 480

bullet_Xchange = 0
bullet_Ychange = 0.4
bullet_status = "ready"

#Coordinates of entity
def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(Enemy_Img,(x,y))

def fireBullet(x,y):
    global bullet_status
    bullet_status = 'GO'
    screen.blit(bullet_Img,(x,y))

running  = True

while running:
    screen.blit(background,(0,0))
    player(playerX,PlayerY)
    enemy(Enemy_X,Enemy_Y)
    # print(f"Bullet X:{bullet_X}, Y:{bullet_Y}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: 
            # print('Pressed Keydown')

            if event.key == pygame.K_LEFT:
                playerX_change = -0.3

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

            if event.key == pygame.K_SPACE:
                # bullet_status = "GO"
                if  bullet_status is 'ready':
                    bullet_status == "GO"
                    bullet_X = playerX+16
                    fireBullet(bullet_X,bullet_Y)
                    bullet_Y = bullet_Y - bullet_Ychange

        if event.type == pygame.KEYUP:
            # print('Pressed Key up')
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change =0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    
    Enemy_X += EnemyX_change
    if Enemy_X <= 0:
        Enemy_X = 0
    if Enemy_X >= 736:
       Enemy_X= 736

    Enemy_X += EnemyX_change
    if Enemy_X <= 0 or Enemy_X >= 736:
        EnemyX_change = EnemyX_change * -1
        Enemy_Y += EnemyY_change

    if bullet_status is "GO":
        fireBullet(bullet_X,bullet_Y)
        bullet_Y = bullet_Y - bullet_Ychange
        if bullet_Y < 0:
            bullet_Y = 480
            bullet_status = 'ready' 
 
    # if bullet_status is "GO":
    #     fireBullet(playerX,bullet_Y)
    #     if bullet_Y < 0:
    #         bullet_Y = 480
    #         bullet_status = 'ready'  
    
    
    pygame.display.update()

pygame.quit()