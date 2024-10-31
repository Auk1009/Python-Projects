import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Block game')

BLUE = (0,0,255)
WHITE = (255,255,255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        self.image = pygame.Surface([40,40])
        self.image.fill(BLUE)
        
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 3
        if key[pygame.K_RIGHT]:
            self.rect.x += 3
        if key[pygame.K_UP]:
            self.rect.y -= 3
        if key[pygame.K_DOWN]:
            self.rect.y += 3

        if self.rect.right > SCREEN_WIDTH:  # Right boundary
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:  # Left boundary
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:  # Bottom boundary
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:  # Top boundary
            self.rect.top = 0

player = Player()

running  = True

while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    player.update()
    screen.blit(player.image,player.rect)
    pygame.display.update()


pygame.quit()