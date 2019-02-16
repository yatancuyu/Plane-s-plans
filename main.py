import pygame
import json
import math
import random

score = [0]
class EnemyKnight(pygame.sprite.Sprite):
    def __init__(self, x,stop_y):
        super().__init__(enemy_pawns)
        self.add(enemy_planes, all_sprites)
        self.frames = []
        print(5)
        self.frame = 5
        self.cur_frame = 0
        self.cut_sheet(pygame.image.load("data/sprites/planes/KnightPlane.png"), 4, 1)
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(18 * 2), int(14*2)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = -20
        self.started = False
        self.stop_y = stop_y
        self.cooldown = 20
        rand = random.randint(2,5)
        self.speeds = ((0,rand),(rand,rand),(-rand,0),(-rand,rand),(0,-rand),(rand,-rand),(rand,0),(rand,rand))

        self.speed_x = 0
        self.speed_y = rand
        self.change_time = 0


    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


    def change_speed(self,cur_speed):
        new_speed = self.speeds[(self.speeds.index(cur_speed)+1)%len(self.speeds)]
        self.speed_x,self.speed_y = new_speed

    def update(self, *args):
        if self.rect.y >= self.stop_y and not(self.started):
            self.change_speed((self.speed_x,self.speed_y))
            self.started = True
        if self.started and not(self.change_time):
            print(random.random())
            self.change_speed((self.speed_x, self.speed_y))
            self.change_time = 50
        self.change_time -= 1 if self.change_time else 0
        self.rect = self.rect.move(self.speed_x, self.speed_y)

        if self.rect.x > 480 and self.speed_x > 0:
            self.change_speed((self.speed_x, self.speed_y))
        if self.rect.x < 0 and self.speed_x < 0:
            self.change_speed((self.speed_x, self.speed_y))
        if self.rect.y < 0 and self.speed_y < 0:
            self.change_speed((self.speed_x, self.speed_y))
        if self.rect.y > 780 and self.speed_y > 0:
            self.change_speed((self.speed_x, self.speed_y))


        if not (self.cooldown):
            Bullet(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, 2)
            self.cooldown = 60
        self.cooldown -= 1 if self.cooldown else 0
        self.mask = pygame.mask.from_surface(self.image)


        if not (self.frame):
            self.cur_frame = (self.cur_frame + 1) % 2
            self.image = pygame.transform.scale(self.frames[2:][self.cur_frame], (int(18 * 2), int(14* 2)))
            self.frame = 5
        self.frame -= 1 if self.frame else 0




class EnemyBishop(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__(enemy_bishops)
        self.add(enemy_planes, all_sprites)
        self.frames = []
        self.lifes = 2
        self.frame = 5
        self.cur_frame = 0
        self.cut_sheet(pygame.image.load("data/sprites/planes/BishPlane.png"), 2, 1)
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(32 * 2.5), int(23 * 2.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 800
        self.cooldown = 60
        self.strafed = False

        self.speed_x = 0
        self.speed_y = -3

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        if not (self.frame):
            self.cur_frame = (self.cur_frame + 1) % 2
            self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(32 * 2.5), int(23 * 2.5)))
            self.frame = 5
        self.frame -= 1 if self.frame else 0
        if self.lifes == 1 and not (self.strafed):
            self.speed_x = random.randint(-4, 3)
            self.strafed = True
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if not (self.cooldown):
            Bullet(self.rect.x + self.rect.w // 2, self.rect.y + self.rect.h, 2)
            self.cooldown = 50
        self.cooldown -= 1 if self.cooldown else 0
        self.mask = pygame.mask.from_surface(self.image)
        for i in bullets:
            if pygame.sprite.collide_mask(self, i) and i.code == 1:
                self.lifes -= 1
                print(self.lifes, end="")
                i.kill()
                score[0] += 3000
        if self.lifes == 0:
            self.kill()
            Implosion(self.rect.x, self.rect.y, self.rect.w, self.rect.h, 1)


class EnemyKing(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(enemy_king)
        self.add(enemy_planes, all_sprites)

        self.frames = []
        self.lifes = 20
        self.frame = 5
        self.phase_change = [False, False, True]
        self.cur_frame = 0
        self.cut_sheet(pygame.image.load("data/KingPlane.png"), 15, 1)
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(67 * 3), int(48 * 3)))

        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = -200

        self.cooldowns = [[15, "self.rect.x+5,self.rect.y+self.rect.h-45", 30],
                          [20, "self.rect.x+self.rect.w-20,self.rect.y+self.rect.h-45", 30],
                          [0, "self.rect.x+self.rect.w//2-10,self.rect.y+self.rect.h-25", 30]]
        self.speed_x = 0
        self.speed_y = 5

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        if not (self.frame) and self.lifes > 10:
            self.cur_frame = (self.cur_frame + 1) % 2
            self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(67 * 3), int(48 * 3)))
            self.frame = 5
        if self.lifes == 10 and not (self.phase_change[0]):
            self.phase_change[1] = True
            self.phase_change[0] = True
            self.cur_frame = 0
            self.cooldowns = [[15, "self.rect.x+5,self.rect.y+self.rect.h-45", 30],
                              [20, "self.rect.x+self.rect.w-50,self.rect.y+self.rect.h-45", 30]]
        if self.lifes == 10 and self.phase_change[1] and not (self.frame):
            self.image = pygame.transform.scale(self.frames[2:8][self.cur_frame], (int(67 * 3), int(48 * 3)))
            self.frame = 20

            if self.cur_frame == 5:
                self.phase_change[1] = False
            else:
                self.cur_frame += 1

        if 0 <= self.lifes <= 10 and not (self.phase_change[1]):
            self.cur_frame = (self.cur_frame + 1) % 2
            self.image = pygame.transform.scale(self.frames[8:10][self.cur_frame], (int(67 * 3), int(48 * 3)))
            self.frame = 5
        if self.lifes == 0 and self.phase_change[2]:
            self.phase_change[2] = False
            self.phase_change[1] = True
            self.cur_frame = 0
        if self.lifes == 0 and self.phase_change[1] and not (self.frame):

            try:
                self.image = pygame.transform.scale(self.frames[10:][self.cur_frame], (int(67 * 3), int(48 * 3)))
                self.frame = 20
                self.cur_frame += 1
            except Exception:
                score[0] += 20000
                self.kill()

        self.frame -= 1 if self.frame else 0
        if not (self.phase_change[1]):
            for i in range(len(self.cooldowns)):
                if not (self.cooldowns[i][0]):
                    eval("Bullet({},2)".format(self.cooldowns[i][1]))
                    self.cooldowns[i][0] = self.cooldowns[i][2]
                    self.cooldowns[i][2] = random.randrange(20, 30)
                self.cooldowns[i][0] -= 1 if self.cooldowns else 0
        self.mask = pygame.mask.from_surface(self.image)
        for i in bullets:
            if pygame.sprite.collide_mask(self, i) and i.code == 1 and not (self.phase_change[1]):
                self.lifes -= 1
                print(self.lifes, end="")
                i.kill()
        if self.rect.y >= 50 and self.speed_y:
            self.speed_y = 0
            self.speed_x = -3
        if self.rect.x <= 10:
            self.speed_x = 3
        if self.rect.x >= 500 - self.rect.w + 50:
            self.speed_x = -3
        if not(self.phase_change[1]):
            self.rect = self.rect.move(self.speed_x, self.speed_y)


class Implosion(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, code):
        super().__init__(implosions)
        self.add(all_sprites)
        self.frames = []
        self.cur_frame = 0
        if code == 1:
            self.cut_sheet(pygame.image.load("data/sprites/booms/boom_sheet.png"), 6, 1)
            self.size_x = w
            self.size_y = h
        if code == 2:
            self.cut_sheet(pygame.image.load("data/sprites/booms/selfboom_sheet.png"), 6, 1)
            self.size_x = 64
            self.size_y = 62
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        print(self.frames)
        self.rect.x = x
        self.rect.y = y
        self.frame = 5

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *args):
        if not (self.frame):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = pygame.transform.scale(self.frames[self.cur_frame], (self.size_x, self.size_y))
            self.frame = 5
        self.frame -= 1 if self.frame else 0
        if self.cur_frame == 5:
            self.kill()


class EnemyPawn(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        super().__init__(enemy_pawns)
        self.add(enemy_planes, all_sprites)
        self.image = pygame.image.load("data/sprites/planes/PawnPlane.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cooldown = 40

        self.speed_x = vx
        self.speed_y = vy
        self.image = pygame.transform.rotate(self.image, math.degrees(math.atan(vx / vy)))

    def update(self, *args):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if not (self.cooldown):
            Bullet(self.rect.x + self.rect.w, self.rect.y + self.rect.h, 2)
            self.cooldown = 60
        self.cooldown -= 1 if self.cooldown else 0


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, code):
        super().__init__(bullets)
        self.add(all_sprites)
        if code == 1:
            self.image = pygame.image.load("data/sprites/bullets/single_bullet.png")
            self.speed_x = 0
            self.speed_y = -15
        if code == 2:
            self.image = pygame.image.load("data/sprites/bullets/enemy_bullet.png")
            self.speed_x = random.randrange(-2, 2)
            self.speed_y = 5
        self.code = code
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *keys):
        self.rect = self.rect.move(self.speed_x, self.speed_y)
        if self.rect.y < -12:
            self.kill()

        if pygame.sprite.spritecollideany(self, enemy_pawns) and self.code == 1:
            plane = pygame.sprite.spritecollideany(self, enemy_pawns)
            Implosion(plane.rect.x, plane.rect.y, plane.rect.w, plane.rect.h, 1)
            score[0] += 1000
            plane.kill()
            self.kill()


class Plane(pygame.sprite.Sprite):

    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        super().__init__(plane, all_sprites)
        self.add(all_sprites)
        self.frames = []
        self.cut_sheet(pygame.image.load("data/sprites/planes/player.png"), 3, 1)
        self.cur_frame = 0
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (66, 60))
        self.rect = self.rect.move(220, 600)
        self.size = 0.5
        self.autopilot_start = None
        self.cooldown = 0
        self.invinc = 60

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
        if not (args[0] % 5) and args[0] < self.finish:  ##Анимация турбулентности и движения пропеллеров
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(66 * self.size), int(60 * self.size)))
            if args[0] > self.start:
                self.size = 1
        if self.start < args[0] < self.finish - 200:  ##Управление
            keys = args[1]
            csen = [(273, (0, -5)), (274, (0, 5)), (275, (5, 0)), (276, (-5, 0))]
            for i in csen:
                if keys[i[0]] and 0 <= self.rect.x + i[1][0] <= 450 and 0 <= self.rect.y + i[1][1] <= 760:
                    self.rect = self.rect.move(*i[1])
            if keys[32] and not (self.cooldown):
                Bullet(self.rect.x + 26, self.rect.y, 1)
                self.cooldown = 25

        if self.finish - 50 == args[0]:  ## Заход на посадку
            self.autopilot_start = (self.rect.x, self.rect.y)
        if self.finish - 50 < args[0] <= self.finish:
            self.rect = self.rect.move(round((220 - self.autopilot_start[0]) / 50),
                                       round((600 - self.autopilot_start[1]) / 50))
        if self.finish < args[0] <= self.finish + 200:
            self.image = pygame.transform.scale(self.frames[self.cur_frame], (int(66 * self.size), int(60 * self.size)))
            self.size = 1 - (args[0] - self.finish) / 400
        self.cooldown -= 1 if self.cooldown else 0
        self.mask = pygame.mask.from_surface(self.image)
        self.invinc -= 1 if self.invinc else 0
        if not (self.invinc):
            for i in bullets:
                if pygame.sprite.collide_mask(self, i) and i.code == 2:
                    self.kill()
                    Implosion(self.rect.x, self.rect.y, 0, 0, 2)
                    score[0] = 0 if score[0] < 5000 else score[0] - 5000
                    i.kill()
            for i in enemy_planes:
                if pygame.sprite.collide_mask(self, i):
                    self.kill()
                    Implosion(self.rect.x, self.rect.y, 0, 0, 2)
                    score[0] = 0 if score[0] < 5000 else score[0] - 5000


class Background(pygame.sprite.Sprite):
    def __init__(self, img_path, y, finish):
        super().__init__(bg_sprites)
        self.add(all_sprites)
        self.finish = finish
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = y

    def update(self, *args):
        if args[0] < self.finish + 150:
            self.rect = self.rect.move(0, 2)
        if self.rect.y >= 800:
            self.kill()


def inmenu(screen, clock):
    global info
    screen.fill((0, 0, 0))
    with open("data/menu_list.json") as file:
        info = json.load(file)
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
                return [False, 0]
            if event.type == pygame.KEYUP:
                if event.key == 102:
                    print(selector.rect.y - 250)
                    print((selector.rect.y - 250) // 25)
                    return [True, (selector.rect.y - 250) // 25, info]
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
    with open("data/lvls_info.json") as fileone:
        lvls_info = json.load(fileone)
    global all_sprites, bullets, enemy_planes, implosions, plane, bg_sprites, enemy_pawns, enemy_king, enemy_bishops, enemy_knights
    pygame.init()
    screen = pygame.display.set_mode((500, 800))
    clock = pygame.time.Clock()
    data = inmenu(screen, clock)
    running = data[0]
    lvl_map = lvls_info[data[1]][1]
    finish = lvls_info[data[1]][0]

    all_sprites = pygame.sprite.Group()
    plane = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    enemy_planes = pygame.sprite.Group()
    enemy_knights = pygame.sprite.Group()
    enemy_bishops = pygame.sprite.Group()
    enemy_king = pygame.sprite.Group()
    enemy_pawns = pygame.sprite.Group()

    implosions = pygame.sprite.Group()
    bg_sprites = pygame.sprite.Group()

    Plane(200, finish)

    lifes = 5
    respawntime = 0
    frames = 0

    font = pygame.font.SysFont("Chava", 25, False, True)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if str(frames) in lvl_map.keys():
            eval(lvl_map.get(str(frames)))
        if not (plane.sprites()) and not (respawntime):
            respawntime = 60
        bg_sprites.update(frames)
        respawntime -= 1 if respawntime else 0
        if lifes != 0 and respawntime == 1:
            respawntime = 0
            lifes -= 1
            Plane(200,finish)



        all_sprites.update(frames, pygame.key.get_pressed())
        all_sprites.draw(screen)
        plane.draw(screen)
        enemy_planes.draw(screen)

        clock.tick(30)

        text = font.render("SCORE: " + str(score[0]).rjust(6, '0'), 1, (215, 165, 255))
        screen.blit(text, (5, 5))
        lifes_text = font.render("LIFES: " + str(lifes), 1, (255, 0, 0))
        screen.blit(lifes_text, (380, 750))

        score[0] += 1

        pygame.display.flip()
        frames += 1
        if lifes == 0 and respawntime == 1:
            running = False
            gameover(screen, clock, 0, data[1], data[2])
        if frames == finish + 205:
            running = False
            gameover(screen, clock,1, data[1], data[2])
    pygame.quit()


def gameover(screen, clock, code, lvl_num, info):
    running = True
    if code:
        with open("data\menu_list.json", "w") as file:
            try:
                info[lvl_num + 4][-1] = True
                rewrite = info[lvl_num+3][0].split()
                rewrite[-1] = str(score[0]).rjust(6, '0')
                info[lvl_num + 3][0] = rewrite[0]+" "+rewrite[1]+"        "+rewrite[-1]
                json.dump(info, file)
            except Exception:
                pass

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == 102:
                    running = False
                    main()
        color = (0, 255, 0) if code else (255, 0, 0)
        info = [("GAME", 100, 250, 25, True), ("OVER!", 100, 250, 125, True), ("YOU LOST!", 25, 275, 225, True),
                ["PRESS F TO BACK TO MENU", 25, 275, 700, True]] if not (code) else [("GOOD", 100, 250, 25, True),
                                                                                     ("JOB!", 100, 250, 125, True),
                                                                                     ("YOUR SCORE:" + str(
                                                                                         score[0]).rjust(6, '0'), 25,
                                                                                      275, 225, True),
                                                                                     ["PRESS F TO BACK TO MENU", 25,
                                                                                      275, 700, True]]

        for i in info:
            if i[-1]:
                font = pygame.font.SysFont("Chava", i[1], False, True)
                text = font.render(i[0], 1, color)
                text_x = i[2] - text.get_width() // 2
                text_y = i[3]
                screen.blit(text, (text_x, text_y))
        clock.tick(30)
        info[-1][-1] = not (info[-1][-1])
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
