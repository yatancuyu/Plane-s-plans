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


class Island(pygame.sprite.Sprite):
    def __init__(self, group, inputed):
        super().__init__(group)
        self.image = pygame.image.load('data/island.png')
        self.rect = self.image.get_rect()
        self.rect.x = inputed[0]
        self.rect.y = inputed[1]

    def update(self, ind):
        if self.rect.y >= 801:
            self.rect.x = random.randrange(10, 400)
            self.rect.y = random.randrange(-1500, -75)
        else:
            self.rect = self.rect.move(0, 1)


bg_1 = Background(sky, -800)
bg_2 = Background(sky, 0)
isl_1 = Island(sky, (200, -300))
isl_2 = Island(sky, (400, -800))
isls = [isl_1, isl_2]
cds = []
for i in range(9):
    cds.append(Clouds(sky))

while running:
    screen.fill((0, 0, 0))
    bg_1.update()
    bg_2.update()
    for i in cds:
        i.update()
    for i in isls:
        i.update(isls.index(i))
    sky.draw(screen)
    pygame.display.flip()
