import pygame
import random

running = True
pygame.init()
size = width, height = 500, 800
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
pygame.display.flip()
sky = pygame.sprite.Group()


class Background(pygame.sprite.Sprite):
    def __init__(self, group, inputed):
        super().__init__(group)
        self.image = pygame.image.load('data/see.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = inputed

    def update(self):
        if self.rect.y == 800:
            self.rect.y = -800
        self.rect = self.rect.move(0, 1)


class Clouds(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load('data/cloud.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 350)
        self.rect.y = random.randrange(-800, -75)

    def update(self):
        if self.rect.y == 801:
            self.rect.x = random.randrange(-50, 375)
            self.rect.y = random.randrange(-1500, -75)
        self.rect = self.rect.move(0, 1)


bg_1 = Background(sky, -800)
bg_2 = Background(sky, 0)
cds = []
for i in range(9):
    cds.append(Clouds(sky))

while running:
    screen.fill((0, 0, 0))
    bg_1.update()
    bg_2.update()
    for i in cds:
        i.update()
    sky.draw(screen)
    pygame.display.flip()
