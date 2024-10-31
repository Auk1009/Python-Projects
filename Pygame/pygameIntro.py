import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Introduction to Pygame')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([50,50])
        self.image.fill(GREEN)


        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 3
        if keys[pygame.K_RIGHT]:
            self.rect.x += 3
        if keys[pygame.K_UP]:
            self.rect.y -= 3
        if keys[pygame.K_DOWN]:
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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(WHITE)
    player.update()
    screen.blit(player.image, player.rect)
    pygame.display.update()

pygame.quit()