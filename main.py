import pygame
import sys
import os

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
fps = 120
deads = int(open('data/deads.txt', 'r').read())


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        elif colorkey == -2:
            colorkey = image.get_at((0, 4))
        elif colorkey == -3:
            colorkey = image.get_at((5, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class BorderVertical(pygame.sprite.Sprite):
    image = load_image('borderVer.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = y


class BackButton(pygame.sprite.Sprite):
    image = load_image('back.png', -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = y


class Restartbutton(pygame.sprite.Sprite):
    image = load_image('restart.png', -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = y


class borderToNext(pygame.sprite.Sprite):
    image = load_image('bordN.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Next(pygame.sprite.Sprite):
    image = load_image('next.png', -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Spike(pygame.sprite.Sprite):
    image = load_image('spike.png', -1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)


class flippedSpike(pygame.sprite.Sprite):
    image = load_image('flippedSpike.png', -2)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)


class BorderHorysontal(pygame.sprite.Sprite):
    image = load_image('border.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Platform(pygame.sprite.Sprite):
    image = load_image('platform.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def goToLevel(lvl):
    try:
        global gameopen
    except Exception:
        pass
    global deads
    running = True
    back = BackButton(width - 110, 30, platforms)
    res = Restartbutton(width - 200, 30, platforms)
    clock = pygame.time.Clock()
    BorderHorysontal(0, 0, platforms)
    BorderHorysontal(0, 690, platforms)
    BorderVertical(width - 30, 0, platforms)
    BorderVertical(0, 0, platforms)
    if lvl != 8:
        pl = Player(64, 380, lvl, Players)
        Platform(400, 390, platforms)
        Platform(537, 390, platforms)
        Platform(30, 540, platforms)
        Platform(150, 540, platforms)
        Platform(30, 250, platforms)
        Platform(955, 544, platforms)
        Platform(width - 230, 544, platforms)
        Platform(width - 230, 338, platforms)
        Spike(555, 650, killing_sprites)
        Spike(430, 350, killing_sprites)
        Spike(670, 350, killing_sprites)
        flippedSpike(430, 420, killing_sprites)
        flippedSpike(189, 280, killing_sprites)
        flippedSpike(670, 420, killing_sprites)
        nx = Next(1248, 420, tonext)
        btnTopres = ButnTopress(485, 380, platforms)
    if lvl == 1 or lvl == 4 or lvl == 3 or lvl == 5 or lvl == 6:
        bord = borderToNext(1063, 368, platforms)
    if lvl == 6:
        for i in range(15):
            MiniBtn('b', 30 + 20 * i, 530, platforms)
        for i in range(12):
            MiniBtn('l', 30, 505 - 20 * i, platforms)
        for i in range(7):
            MiniBtn('t', 45 + 20 * i, 280, platforms)
        for i in range(26):
            MiniBtn('b', 30 + 20 * i, 680, platforms)
        for i in range(10):
            MiniBtn('b', 30 + 20 * i, 240, platforms)
        for i in range(32):
            MiniBtn('b', 600 + 20 * i, 680, platforms)
        for i in range(10):
            MiniBtn('b', 1050 + 20 * i, 329, platforms)
        for i in range(16):
            MiniBtn('t', 30 + 20 * i, 570, platforms)
        for i in range(44):
            MiniBtn('t', 30 + 20 * i, 30, platforms)
        MiniBtn('r', 945, 550, platforms)
        MiniBtn('r', 390, 395, platforms)
        truebtn = MiniBtn('t', 910, 30, platforms)
        for i in range(7):
            MiniBtn('t', 930 + 20 * i, 30, platforms)
        MiniBtn('b', 405, 380, platforms)
        MiniBtn('b', 715, 380, platforms)
        MiniBtn('t', 405, 420, platforms)
        MiniBtn('t', 715, 420, platforms)
        MiniBtn('l', 737, 393, platforms)
        MiniBtn('l', 229, 249, platforms)
        for i in range(10):
            MiniBtn('l', 30, 221 - 20 * i, platforms)
        for i in range(5):
            MiniBtn('b', 956 + 20 * i, 535, platforms)
            MiniBtn('l', 30, 659 - 20 * i, platforms)
            MiniBtn('r', 1240, 668 - 20 * i, platforms)
            MiniBtn('r', 1240, 300 - 20 * i, platforms)
    if lvl == 8:
        nx = Next(48, 514, tonext)
        pl = Player(80, 160, lvl, Players)
        revPl = ReversedPlayer(pl, platforms)
        Platform(30, height / 2 + 30, platforms)
        Platform(120, height / 2 + 30, platforms)
        Platform(width - 200 - 120, height - 60 - height / 2, platforms)
        Platform(width - 200 - 30, height - 60 - height / 2, platforms)
        btnTopres = reversedButnTopress(revPl, 42, 30, platforms)
        reversedbtnTopres = ButnTopress(width - 170 - 42, height - 10 - 30, platforms)
        bords = []
        for i in range(10):
            flippedSpike(330 + 40 * i, 30, killing_sprites)
            Spike(width - 370 - 40 * i, height - 70, killing_sprites)
        bords.append(borderToNext(292, 420, platforms))
        bords.append(borderToNext(width - 292 - 28, height - 176 - 420, platforms))
        bords.append(borderToNext(width - 292 - 28, 30, platforms))
        bords.append(borderToNext(292, height - 30 - 176, platforms))
    if lvl == 7:
        borderToNext(1063, 368, blanks)
    kd = False
    ka = False
    go = False
    font = pygame.font.Font(None, 80)
    while running:
        screen.fill((0, 0, 0))
        if lvl == 1:
            text = font.render("1: Жми на кнопку", True, (255, 255, 255))
            screen.blit(text, (100, 100))
            if pygame.sprite.spritecollide(pl, tonext, False):
                if not str(lvl + 1) in open('data/levels.txt', 'r').read():
                    open('data/levels.txt', 'a').write(' ' + str(lvl + 1))
                clear()
                goToLevel(lvl + 1)
                clear()
                return None
            if pygame.sprite.spritecollide(btnTopres, Players, False):
                bord.kill()
        elif lvl == 2:
            text1 = pygame.font.Font(None, 15).render("не", True, (255, 255, 255))
            text = pygame.font.Font(None, 80).render("2: Жми на кнопку", True, (255, 255, 255))
            screen.blit(text, (100, 100))
            screen.blit(text1, (150, 135))
            if pygame.sprite.spritecollide(pl, tonext, False):
                if not str(lvl + 1) in open('data/levels.txt', 'r').read():
                    open('data/levels.txt', 'a').write(' ' + str(lvl + 1))
                clear()
                goToLevel(lvl + 1)
                clear()
                return None
            if pygame.sprite.spritecollide(btnTopres, Players, False):
                borderToNext(1063, 368, platforms)
        elif lvl == 3:
            text = font.render("3: Наоборот", True, (255, 255, 255))
            screen.blit(text, (100, 100))
            if pygame.sprite.spritecollide(bord, Players, False):
                btnTopres.images = [load_image('BlankPressedbutn.png', -1), load_image('BlankPressedbutn.png', -1)]
                go = True
            if pygame.sprite.spritecollide(btnTopres, Players, False):
                if go:
                    if not str(lvl + 1) in open('data/levels.txt', 'r').read():
                        open('data/levels.txt', 'a').write(' ' + str(lvl + 1))
                    clear()
                    goToLevel(lvl + 1)
                    clear()
                    return None
        elif lvl == 4:
            font = pygame.font.Font(None, 80)
            text = font.render("4: Наоборот v2", True, (255, 255, 255))
            screen.blit(text, (100, 100))
            if pygame.sprite.spritecollide(pl, tonext, False):
                if not str(lvl + 1) in open('data/levels.txt', 'r').read():
                    open('data/levels.txt', 'a').write(' ' + str(lvl + 1))
                clear()
                goToLevel(lvl + 1)
                clear()
                return None
            if pygame.sprite.spritecollide(btnTopres, Players, False):
                bord.kill()
        elif lvl == 5:
            font = pygame.font.Font(None, 80)
            text = font.render("5: Сделай перерыв", True, (255, 255, 255))
            screen.blit(text, (100, 100))
            gameopen = True
            if 'True' in open('data/data.txt', 'r').read():
                bord.kill()
                open('data/data.txt', 'w').write('')
            if pygame.sprite.spritecollide(pl, tonext, False):
                if not str(lvl + 1) in open('data/levels.txt', 'r').read():
                    open('data/levels.txt', 'a').write(' ' + str(lvl + 1))
                clear()
                goToLevel(lvl + 1)
                clear()
                return None
        elif lvl == 6:
            text = font.render("6: где кнопка?", True, (255, 255, 255))
            screen.blit(text, (100, 100))
            if pygame.sprite.spritecollide(pl, tonext, False):
                if not str(lvl + 1) in open('data/levels.txt', 'r').read():
                    open('data/levels.txt', 'a').write(' ' + str(lvl + 1))
                clear()
                goToLevel(lvl + 1)
                clear()
                return None
            if pygame.sprite.spritecollide(truebtn, Players, False):
                bord.kill()
        elif lvl == 7:
            text = font.render("7: двери нет, ты её придумал", True, (255, 255, 255))
            screen.blit(text, (160, 150))
            if pygame.sprite.spritecollide(pl, tonext, False):
                if not str(lvl + 1) in open('data/levels.txt', 'r').read():
                    open('data/levels.txt', 'a').write(' ' + str(lvl + 1))
                clear()
                goToLevel(lvl + 1)
                clear()
                return None
        elif lvl == 8:
            text = font.render("8: один хорошо,", True, (255, 255, 255))
            text1 = font.render("a два ещё лучше", True, (255, 255, 255))
            screen.blit(text1, (160, 150))
            screen.blit(text, (100, 100))
            if btnTopres.pressed:
                if killing_sprites:
                    killing_sprites.empty()
                    for i in bords:
                        i.kill()
            if pygame.sprite.spritecollide(pl, tonext, False):
                clear()
                lvls()
                clear()
                return None
        tonext.draw(screen)
        platforms.update()
        platforms.draw(screen)
        blanks.draw(screen)
        Players.update()
        killing_sprites.draw(screen)
        Players.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    gameopen = not(gameopen)
                    open('data/data.txt', 'w').write('True')
                except Exception:
                    pass
                sys.exit()
            elif event.type == pygame.KEYDOWN and lvl != 4:
                if event.key == pygame.K_d:
                    kd = True
                elif event.key == pygame.K_a:
                    ka = True
                if event.key == pygame.K_SPACE:
                    pl.jump(-750)
            elif event.type == pygame.KEYDOWN and lvl == 4:
                if event.key == pygame.K_SPACE:
                    kd = True
                elif event.key == pygame.K_d:
                    ka = True
                if event.key == pygame.K_a:
                    pl.jump(-750)
            elif event.type == pygame.KEYUP and lvl != 4:
                if event.key == pygame.K_d:
                    kd = False
                if event.key == pygame.K_a:
                    ka = False
            elif event.type == pygame.KEYUP and lvl == 4:
                if event.key == pygame.K_SPACE:
                    kd = False
                if event.key == pygame.K_d:
                    ka = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if width - 100 < event.pos[0] < width - 20 and 20 < event.pos[1] < 100:
                    clear()
                    return None
                elif width - 200 < event.pos[0] < width - 120 and 20 < event.pos[1] < 100:
                    clear()
                    goToLevel(lvl)
                    clear()
                    return None
        if pygame.sprite.spritecollide(back, Players, False):
                    clear()
                    return None
        elif pygame.sprite.spritecollide(res, Players, False):
                    clear()
                    goToLevel(lvl)
                    clear()
                    return None
        else:
            for i in killing_sprites:
                if pygame.sprite.collide_mask(pl, i):
                    deads += 1
                    open('data/deads.txt', 'w').write(str(deads))
                    clear()
                    goToLevel(lvl)
                    clear()
                    return None
        if ka:
            pl.move(-240)
        if kd:
            pl.move(240)
        if not ka and not kd:
            pl.move(0)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


class MiniBtn(pygame.sprite.Sprite):
    images = {'b': [load_image('minibtnbot.png', -1), load_image('pressedminibtnbot.png', -1)],
              't': [load_image('minibtntop.png', -2), load_image('pressedminibtntop.png', -2)],
              'l': [load_image('minibtnleft.png', -3), load_image('pressedminibtnleft.png', -3)],
              'r': [load_image('minibtnright.png', -1), load_image('pressedminibtnright.png', -1)]}

    def __init__(self, pol, x, y, *group):
        super().__init__(*group)
        self.pol = pol
        self.image = self.images[pol][1]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def update(self):
        if self.pol == 'b':
            if pygame.sprite.spritecollide(self, Players, False):
                self.image = self.images[self.pol][-1]
                self.rect.y = self.y + 3
            else:
                self.image = self.images[self.pol][0]
                self.rect.y = self.y
        elif self.pol == 't':
            if pygame.sprite.spritecollide(self, Players, False):
                self.image = self.images[self.pol][-1]
                self.rect.y = self.y
            else:
                self.image = self.images[self.pol][0]
                self.rect.y = self.y
        elif self.pol == 'l':
            if pygame.sprite.spritecollide(self, Players, False):
                self.image = self.images[self.pol][-1]
                self.rect.x = self.x
            else:
                self.image = self.images[self.pol][0]
                self.rect.x = self.x
        elif self.pol == 'r':
            if pygame.sprite.spritecollide(self, Players, False):
                self.image = self.images[self.pol][-1]
                self.rect.x = self.x + 3
            else:
                self.image = self.images[self.pol][0]
                self.rect.x = self.x


class Levels(pygame.sprite.Sprite):
    image = load_image('levels.png', -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = (width - 300) / 2
        self.rect.y = (height - 90) / 2 - 30

    def click(self):
        lvls()


def lvls():
    try:
        global gameopen
    except Exception:
        pass
    runing = True
    lvlImages = lvL1, lvL2, lvL3, lvL4, lvL5, \
                lvL6, lvL7, lvL8 = [load_image('lvl1.png'), load_image('lvl2.png'), \
                                                 load_image('lvl3.png'), load_image('lvl4.png'), \
                                                 load_image('lvl5.png'), load_image('lvl6.png'), \
                                                 load_image('lvl7.png'), load_image('lvl8.png')]
    clock = pygame.time.Clock()
    while runing:
        screen.blit(load_image('background.jpg'), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    gameopen = not(gameopen)
                    open('data/data.txt', 'w').write('True')
                except Exception:
                    pass
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(int(open('data/levels.txt', 'r').read()[-1][-1])):
                    if 250 + 20 * (i + 1) + 80 * i < event.pos[0] < 250 + 20 * (i + 1) + 80 * i + 80\
                            and 200 < event.pos[1] < 280:
                        goToLevel(i + 1)
                        clear()
                        return None

        if open('data/levels.txt', 'r').read():
            for i in range(8):
                if str(i + 1) in open('data/levels.txt', 'r').read():
                    screen.blit(lvlImages[i], (250 + 20 * (i + 1) + 80 * i, 200))
                else:
                    screen.blit(load_image('none.png'), (250 + 20 * (i + 1) + 80 * i, 200))
                    lvlImages[i] = False
        text = pygame.font.Font(None, 80).render("Уровни", True, (0, 0, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = text.get_height() // 2
        screen.blit(text, (text_x, text_y))
        clock.tick(fps)
        pygame.display.flip()


class reversedButnTopress(pygame.sprite.Sprite):
    images = [load_image('reversedButn.png', -2), load_image('ReversedPressedbutn.png', -2)]
    image = images[0]

    def __init__(self, RevPl, x, y, *group):
        super().__init__(*group)
        self.rect = self.images[1].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.RevPl = RevPl
        self.pressed = False

    def update(self):
        if self.rect.left < self.RevPl.rect.left < self.rect.right + 30 \
                and self.RevPl.rect.top - 10 < self.rect.bottom:
            self.image = self.images[1]
            self.pressed = True
        else:
            self.image = self.images[0]
            self.pressed = False


class ButnTopress(pygame.sprite.Sprite):
    images = [load_image('butn.png', -1), load_image('Pressedbutn.png', -1)]
    image = images[0]

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = self.images[1].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.pressed = True

    def update(self):
        if self.rect.left < Players.sprites()[0].rect.left < self.rect.right + 30 \
                and self.rect.top < Players.sprites()[0].rect.bottom + 10 < self.rect.bottom + 30 :
            self.image = self.images[1]
            self.rect.y = self.y + 4
            self.pressed = True
        else:
            self.image = self.images[0]
            self.rect.y = self.y
            self.pressed = False


class PlayBtn(pygame.sprite.Sprite):
    image = load_image('Play.png', -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = (width - 300) / 2

        self.rect.y = (height - 90) / 2 - 150

    def play(self):
        goToLevel(int(open('data/levels.txt', 'r').read()[-1]))


class ReversedPlayer(pygame.sprite.Sprite):
    image = load_image('reversedPlayer.png', -1)

    def __init__(self, mainPl, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.mainPl = mainPl
        self.rev = True

    def update(self):
        self.rect.x = width - self.mainPl.rect.x - 60
        self.rect.y = height - self.mainPl.rect.y - 100


class Player(pygame.sprite.Sprite):
    image = load_image('player.png', -1)

    def __init__(self, x, y, lvl, *group):
        super().__init__(*group)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        self.lvl = lvl
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.vy > 400:
            self.vy = 400
        self.a = 10
        if pygame.sprite.spritecollide(self, platforms, False):
            mass = pygame.sprite.spritecollide(self, platforms, False)
            for i in mass:
                if i.rect.top * -1 + self.rect.bottom < 6:
                    self.rect.bottom = i.rect.top + 1
                    if self.vy > 0:
                        self.vy = 0
                    if self.a > 0:
                        self.a = 0
                elif i.rect.bottom - self.rect.top < 6:
                    self.rect.top = i.rect.bottom + 1
                    if self.vy < 0:
                        self.a = 10
                        self.vy = 1
                elif i.rect.top + 2 < self.rect.bottom:
                    if self.rect.right >= 1 + i.rect.left and self.rect.left + 5 < i.rect.left:
                        self.rect.right = i.rect.left + 1
                        if self.vx > 0:
                            self.vx = 0
                    else:
                        self.rect.left = i.rect.right - 2
                        if self.vx < 0:
                            self.vx = 0

        self.rect.x += int(self.vx / fps)
        self.rect.y += int(self.vy / fps)
        self.vy += self.a

    def move(self, v):
        self.vx = v

    def jump(self, v):
        if pygame.sprite.spritecollideany(self, platforms):
            self.vy = v


def mainMenu():
    try:
        global gameopen
    except Exception:
        pass
    levls = Levels(btns)
    Play = PlayBtn(btns)
    runing = True
    clock = pygame.time.Clock()
    while runing:
        screen.blit(load_image('background.jpg'), (0, 0))
        btns.draw(screen)
        btns.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    gameopen = not(gameopen)
                    open('data/data.txt', 'w').write('True')
                except Exception:
                    pass
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Play.rect.left < event.pos[0] < Play.rect.right and Play.rect.top < event.pos[1] < Play.rect.bottom:
                    Play.play()
                if levls.rect.left < event.pos[0] < levls.rect.right and\
                        levls.rect.top < event.pos[1] < levls.rect.bottom:
                    levls.click()

        clock.tick(fps)
        pygame.display.flip()


def clear():
    wall.empty()
    Players.empty()
    killing_sprites.empty()
    platforms.empty()
    top_borders.empty()
    btnToPress.empty()
    tonext.empty()
    blanks.empty()


if __name__ == '__main__':
    blanks = pygame.sprite.Group()
    tonext = pygame.sprite.Group()
    wall = pygame.sprite.Group()
    btnToPress = pygame.sprite.Group()
    Players = pygame.sprite.Group()
    killing_sprites = pygame.sprite.Group()
    btns = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    top_borders = pygame.sprite.Group()
    mainMenu()
