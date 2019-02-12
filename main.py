import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.image.load("data/single_bullet.png")
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
f
    def update(self, *keys):
        self.rect = self.rect.move(0, -10)


class Plane(pygame.sprite.Sprite):

    def __init__(self, group, start, finish):
        self.start = start
        self.finish = finish
        super().__init__(group)
        self.frames = []
        self.cut_sheet(pygame.image.load("data/player.png"), 3, 1)
        self.cur_frame = 0
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (66, 60))
        self.rect = self.rect.move(220, 600)
        self.size = 0.5
        self.autopilot_start = None

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        '''Заскриптованное движение и управление'''
        if self.start >= args[0]:  ##Взлет
            self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(66 * self.size), int(60 * self.size)))
            self.size = 0.5 + args[0] / (2 * self.start)
        if not (args[0] % 5) and args[0]<self.finish:  ##Анимация турбулентности и движения пропеллеров
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(66 * self.size), int(60 * self.size)))

        if self.start < args[0] < self.finish - 50:  ##Управление
            keys = args[1]
            csen = [(273, (0, -5)), (274, (0, 5)), (275, (5, 0)), (276, (-5, 0))]
            for i in csen:
                if keys[i[0]] and 0 <= self.rect.x + i[1][0] <= 450 and 0 <= self.rect.y + i[1][1] <= 760:
                    self.rect = self.rect.move(*i[1])
        if self.finish - 50 == args[0]:  ## Заход на посадку
            self.autopilot_start = (self.rect.x, self.rect.y)
        if self.finish - 50 < args[0] <= self.finish :
            self.rect = self.rect.move(round((220 - self.autopilot_start[0]) / 50), round((600 - self.autopilot_start[1]) / 50))
        if self.finish < args[0] <= self.finish+200:
            self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(66 * self.size), int(60 * self.size)))
            self.size = 1- (args[0]-self.finish) / 400



class Background(pygame.sprite.Sprite):
    def __init__(self, group, img_path, y,finish):
        super().__init__(group)
        self.finish = finish
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = y

    def update(self,*args):
        if args[0]<self.finish+300:
            self.rect = self.rect.move(0, 2)
        if self.rect.y >= 800:
            self.kill()


def inmenu(screen, clock):
    screen.fill((0, 0, 0))
    info = [("PLANE'S", 100, 250, 25, True), ("PLANS", 100, 250, 125, True), ("LEVEL        SCORE", 25, 275, 225, True),
            ("1. FIRST BLOOD        000000", 25, 225, 250, True),
            ("1. FIRST BLOOD        000000", 25, 225, 275, True),
            ("1. FIRST BLOOD        000000", 25, 225, 300, True), ["PRESS F TO START", 25, 275, 700, True]]
    selector_s = pygame.sprite.Group()
    selector = pygame.sprite.Sprite(selector_s)
    selector.image = pygame.image.load("data/arrow.png")
    selector.rect = selector.image.get_rect()
    selector.rect.x = 10
    selector.rect.y = 250
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                if event.key == 102:
                    print(selector.rect.y - 250)
                    print((selector.rect.y - 250) // 25)
                    return [True, (selector.rect.y - 250) // 25]
                if event.key == 274 and selector.rect.y <= 200 + sum(map(lambda x: 25 if x[-1] else 0, info[3:-1])):
                    print(info[2:-1])
                    selector.rect.y += 25
                if event.key == 273 and selector.rect.y > 250:
                    selector.rect.y -= 25

        for i in info:
            if i[-1]:
                font = pygame.font.SysFont("Chava", i[1], False, True)
                text = font.render(i[0], 1, (100, 100, 255))
                text_x = i[2] - text.get_width() // 2
                text_y = i[3]
                screen.blit(text, (text_x, text_y))
        clock.tick(30)
        info[-1][-1] = not (info[-1][-1])
        selector_s.draw(screen)
        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 800))
    frames = 0
    clock = pygame.time.Clock()
    data = inmenu(screen, clock)
    running = data[0]
    lvl_map = {"0": ["data/ship.png", -214],
               "300": ["data/island.png", -3266],
               "2300": ["data/ship.png", -1014]}
    score = 0

    all_sprites = pygame.sprite.Group()
    plane = pygame.sprite.Group()
    Plane(plane, 200, 2400)
    bg_sprites = pygame.sprite.Group()
    Background(bg_sprites, 'data/see.jpg', -16420,2400)
    font = pygame.font.SysFont("Chava", 25, False, True)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == 32:
                    for i in plane:
                        Bullet(all_sprites, i.rect.x, i.rect.y)
                if event.key == 102:
                    running = False
        if str(frames) in lvl_map.keys():
            Background(bg_sprites, lvl_map.get(str(frames))[0], lvl_map.get(str(frames))[1],2400)

        bg_sprites.update(frames)

        bg_sprites.draw(screen)
        all_sprites.draw(screen)
        plane.draw(screen)
        all_sprites.update(frames, pygame.key.get_pressed())

        plane.update(frames, pygame.key.get_pressed())
        clock.tick(30)

        text = font.render("SCORE:" + str(score).rjust(6, '0'), 1, (215, 165, 255))
        text_x = 5
        text_y = 5
        screen.blit(text, (text_x, text_y))
        score += 1

        
        pygame.display.flip()
        frames += 1


if __name__ == '__main__':
    main()
