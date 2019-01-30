import pygame
import random


class Parameter(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.image.load("data/param.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




class Bullet(pygame.sprite.Sprite):

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.image.load("data/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, keys):
        self.rect = self.rect.move(0, -10)


class Plane(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("data/art.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 250

    def update(self, *args):
        keys = args[0]
        csen = [(273, (0, -5)), (274, (0, 5)), (275, (5, 0)), (276, (-5, 0))]
        for i in csen:
            if keys[i[0]] and 0 <= self.rect.x + i[1][0] <= 450 and 0 <= self.rect.y + i[1][1] <= 760:
                self.rect = self.rect.move(*i[1])
                print(self.rect)




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
        self.rect = self.rect.move(0, 2)


def main():
    pygame.init()
    sky = pygame.sprite.Group()

    screen = pygame.display.set_mode((500, 800))
    all_sprites = pygame.sprite.Group()
    Parameter(all_sprites, 5, 50)
    plane = pygame.sprite.Group()
    Plane(plane)
    running = True
    bg_1 = Background(sky, -800)
    bg_2 = Background(sky, 0)
    cds = []
    for i in range(9):
        cds.append(Clouds(sky))
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP and event.key == 32:
                for i in plane:
                    Bullet(all_sprites, i.rect.x, i.rect.y)
        bg_1.update()
        bg_2.update()
        for i in cds:
            i.update()
        sky.draw(screen)
        pygame.draw.rect(screen,(0, 255, 0), (28, 76, 107, 23))
        all_sprites.draw(screen)
        plane.draw(screen)
        all_sprites.update(pygame.key.get_pressed())

        plane.update(pygame.key.get_pressed())
        clock.tick(30)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
