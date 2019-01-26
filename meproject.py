import pygame
class Bullet(pygame.sprite.Sprite):

    def __init__(self, group,x,y):
        super().__init__(group)
        self.image = pygame.image.load("data/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, keys):
        self.rect = self.rect.move(0,-10)

class Plane(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("data/art.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 250

    def update(self, keys):
        csen = [(273, (0, -5)), (274, (0, 5)), (275, (5, 0)), (276, (-5, 0))]
        for i in csen:
            if keys[i[0]] and 0 <= self.rect.x + i[1][0] <= 450 and 0 <= self.rect.y + i[1][1] <=760:
                self.rect = self.rect.move(*i[1])
                print(self.rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 800))
    all_sprites = pygame.sprite.Group()
    plane = pygame.sprite.Group()
    Plane(plane)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP and event.key == 32:
                for i in plane:
                    Bullet(all_sprites, i.rect.x, i.rect.y)
        screen.fill((250, 223, 173))
        all_sprites.draw(screen)
        plane.draw(screen)
        all_sprites.update(pygame.key.get_pressed())
        plane.update(pygame.key.get_pressed())
        clock.tick(30)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()

