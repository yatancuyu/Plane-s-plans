import pygame

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
        if self.rect.y == 801:
            self.rect.y = -800
        self.rect = self.rect.move(0, 1)


bk_1 = Background(sky, -800)
bk_2 = Background(sky, 0)

while running:
    screen.fill((0, 0, 0))
    bk_1.update()
    bk_2.update()
    sky.draw(screen)
    pygame.display.flip()
