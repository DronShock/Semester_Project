import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

# какой то текст
# считывание размеров экрана
# import ctypes
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

WIDTH = 1000
HEIGHT = 650
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.move = "up"
        self.uron = None
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 200

    def update(self):
        """
        Обновляет положение игрока на экране
        :return: None
        """
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.move = "up"
            self.speedy = -3
        if keystate[pygame.K_DOWN]:
            self.move = "down"
            self.speedy = 3
        if keystate[pygame.K_LEFT]:
            self.move = "left"
            self.fix_scorosti()
        if keystate[pygame.K_RIGHT]:
            self.move = "right"
            self.fix_scorosti()
        if self.speedx != 0 or self.speedy != 0:
            self.animation(self.move)
        self.rect.x += int(self.speedx)
        self.rect.y += int(self.speedy)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        self.stolknovenia()
        self.udar()

    def stolknovenia(self):
        hits = pygame.sprite.spritecollide(self, elementi_karti, False)
        if hits:
            if self.speedx < 0:
                self.rect.left = hits[0].rect.right
            elif self.speedx > 0:
                self.rect.right = hits[0].rect.left
            elif self.speedy < 0:
                self.rect.top = hits[0].rect.bottom
            elif self.speedy > 0:
                self.rect.bottom = hits[0].rect.top

    def udar(self):
        self.uron = None
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            time = pygame.time.get_ticks()
            self.image = eval("player_udar_{}".format(self.move)).convert()
            self.uron = self.move
            #self.image = pygame.image.load(path.join(img_dir, eval('player_anim_{}'.format(self.move))[0])).convert()
            #self.image = pygame.transform.scale(self.image, (35, 43))
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def animation(self, move):
        time = pygame.time.get_ticks()
        if time - self.last_update > self.frame_rate:
            self.last_update = time
            self.frame += 1
            if self.frame == len(eval('player_anim_{}'.format(move))):
                self.frame = 0
            self.image = pygame.image.load(
                path.join(img_dir, eval('player_anim_{}'.format(move))[self.frame])).convert()
            self.image = pygame.transform.scale(self.image, (35, 43))
            self.image.set_colorkey(BLACK)
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def fix_scorosti(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            if keystate[pygame.K_UP]:
                self.speedx = -3 / (2 ** (1 / 2))
                self.speedy = -3 / (2 ** (1 / 2))
            elif keystate[pygame.K_DOWN]:
                self.speedx = -3 / (2 ** (1 / 2))
                self.speedy = 3 / (2 ** (1 / 2))
            else:
                self.speedx = -3
        if keystate[pygame.K_RIGHT]:
            if keystate[pygame.K_UP]:
                self.speedx = 3 / (2 ** (1 / 2))
                self.speedy = -3 / (2 ** (1 / 2))
            elif keystate[pygame.K_DOWN]:
                self.speedx = 3 / (2 ** (1 / 2))
                self.speedy = 3 / (2 ** (1 / 2))
            else:
                self.speedx = 3


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.health_points = 15
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 200

    def update(self):
        if self.rect.centery > player.rect.centery:
            self.speedy = -1
            self.animation("up")
        elif self.rect.centery < player.rect.centery:
            self.speedy = 1
            self.animation("down")
        else:
            self.speedy = 0
            if self.rect.centerx > player.rect.centerx:
                self.speedx = -1
                self.animation("left")
            else:
                self.speedx = 1
                self.animation("right")
        if self.rect.centerx >= player.rect.centerx:
            self.speedx = -1
            self.animation("left")
        else:
            self.speedx = 1
            self.animation("right")

        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        self.poluchenie_urona()

    def poluchenie_urona(self):
        active_sprites.remove(self)
        hits = pygame.sprite.spritecollide(self, active_sprites, False,pygame.sprite.collide_rect_ratio(0.8))
        active_sprites.add(self)
        if player.uron is not None:
            if hits:
                self.health_points -= 1
                self.rect.centerx -= 20 * self.speedx // abs(self.speedx)
        if self.health_points == 0:
            self.kill()

    def animation(self, move):
        time = pygame.time.get_ticks()
        if time - self.last_update > self.frame_rate:
            self.last_update = time
            self.frame += 1
            if self.frame == len(eval('skelet_anim_{}'.format(move))):
                self.frame = 0
            self.image = pygame.image.load(
                path.join(img_dir, eval('skelet_anim_{}'.format(move))[self.frame])).convert()
            self.image.set_colorkey(BLACK)
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center


def change_item(self):
    """
    функция меняет предмет в руке
    """


def change_armor(self):
    """
    функция меняет броню
    """


class ElementiKarti(pygame.sprite.Sprite):
    items = []

    def __init__(self, image, position, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.position = position
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        ElementiKarti.items.append(self)


class Objects(pygame.sprite.Sprite):
    items = []

    def __init__(self, image, position, x, y, text=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.position = position
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.text = text
        Objects.items.append(self)


class Text:
    """
    Создаёт текст для отображения на экране
    """
    items = []
    active_text = []

    def __init__(self, surf, name, text, size, x, y, sprite=None, reading=False):
        self.font_name = pygame.font.match_font(name)
        self.font = pygame.font.Font(self.font_name, size)
        self.text_surface = self.font.render(text, True, WHITE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (x, y)
        self.reading = reading
        self.surf = surf
        self.sprite = sprite
        Text.items.append(self)


class Creature():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def go_to(self, x, y):
        """
        функция должна заставлять идти объект к точке (x,y)
        желательно еще связать это со скоростью
        функция будет использоваться восновном для MPC
        """

    def go_button(self, w, a, s, d):
        """
        функция перемещения для игрока
        w,a,s,d -- булевские переменные соответствующие нажатию на такие же кнопки
        true -- кнопка
        не забыть про одновременное нажатие на кнопок и постоянную скорость
        """


class NPC():
    pass


class peaceful(NPC):
    pass


class enemy(NPC):
    def attack(self):
        pass


def click_start_game(x, y):
    if x >= 314 and x <= 688 and y >= 90 and y <= 178:
        return True
    else:
        return False


# Загрузка изображений объектов
background = pygame.image.load(path.join(img_dir, 'DB32RecolorEx.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "Down_0.png")).convert()
player_img = pygame.transform.scale(player_img, (35, 43))
main_menu_pict = pygame.image.load('main_menu1.png')
derevo1 = pygame.image.load(path.join(img_dir, 'Derevo 1.png')).convert()
Svitok = pygame.image.load(path.join(img_dir, 'Svitok.png')).convert()
Svitok = pygame.transform.scale(Svitok, (20, 30))

# Создание массивов с анимациями
skelet_anim_up = ['Up 0.png', 'Up 1.png', 'Up 0.png', 'Up 2.png']
skelet_anim_down = ['Down 0.png', 'Down 1.png', 'Down 0.png', 'Down 2.png']
skelet_anim_left = ['Left 0.png', 'Left 1.png', 'Left 0.png', 'Left 2.png']
skelet_anim_right = ['Right 0.png', 'Right 1.png', 'Right 0.png', 'Right 2.png']

player_anim_up = ['Up_0.png', 'Up_1.png', 'Up_0.png', 'Up_2.png']
player_anim_down = ['Down_0.png', 'Down_1.png', 'Down_0.png', 'Down_2.png']
player_anim_left = ['Left_0.png', 'Left_1.png', 'Left_0.png', 'Left_2.png']
player_anim_right = ['Right_0.png', 'Right_1.png', 'Right_0.png', 'Right_2.png']

player_udar_up = pygame.image.load(path.join(img_dir, "Udar_Up.png")).convert()
player_udar_down = pygame.image.load(path.join(img_dir, "Udar_Down.png")).convert()
player_udar_left = pygame.image.load(path.join(img_dir, "Udar_Left.png")).convert()
player_udar_right = pygame.image.load(path.join(img_dir, "Udar_Right.png")).convert()
player_udar_up = pygame.transform.scale(player_udar_up, (30, 75))
player_udar_down = pygame.transform.scale(player_udar_down, (30, 75))
player_udar_left = pygame.transform.scale(player_udar_left, (75, 46))
player_udar_right = pygame.transform.scale(player_udar_right, (75, 46))

# Добавления спрайтов в группу для отрисовки
active_sprites = pygame.sprite.Group()
elementi_karti = pygame.sprite.Group()
objects = pygame.sprite.Group()
player = Player()

# Создание врагов
skelet1 = Enemy(100,100)
skelet2 = Enemy(200,200)
skelet3 = Enemy(300,300)
skelet4 = Enemy(400,400)
skelet5 = Enemy(500,500)

# Создание текстов для игры
Podskazka = Text(screen, 'arial', "Press 'f' to start reading", 18, 0, 0)
Svitok1 = Text(screen, 'arial', "You are reading a scroll", 18, 500, 500, Svitok)
Privetstvie1 = Text(screen, 'arial',
                    "Приветсвуем Вас в ранней версии нашего игрового проекта,",
                    25, 500, 100)
Privetstvie2 = Text(screen, 'arial',
                    "совсем скоро Вы сможете испытать его в действии!",
                    25, 500, 150)
Text.active_text.append(Privetstvie1)
Text.active_text.append(Privetstvie2)

# Добавление объектов на карту
derevo1 = ElementiKarti(derevo1, 0, 100, 100)
svitok = Objects(Svitok, 0, 500, 500, Podskazka)


def draw_text():
    for text in Text.active_text:
        text.surf.blit(text.text_surface, text.text_rect)


Podskazka.text_rect.midtop = (svitok.rect.centerx, svitok.rect.bottom)
hits = pygame.sprite.spritecollide(player, objects, False)
if hits:
    Text.active_text.append(Podskazka)

active_sprites.add(player)
active_sprites.add(skelet1)
active_sprites.add(skelet2)
active_sprites.add(skelet3)
active_sprites.add(skelet4)
active_sprites.add(skelet5)
for smth in ElementiKarti.items:
    elementi_karti.add(smth)
    active_sprites.add(smth)
for smth in Objects.items:
    objects.add(smth)
    active_sprites.add(smth)

main_menu = True
esc_menu = False
playing_game = False
open_inventory = False
finished = False

# Цикл игры
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # проверка для закрытия окна
            finished = True
    if main_menu == True:
        screen.blit(main_menu_pict, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            click_x, click_y = event.pos
            screen.blit(main_menu_pict, (0, 0))
            pygame.display.update()
            if click_start_game(click_x, click_y) == True:
                main_menu = False
                playing_game = True
                screen.fill(BLACK)
                pygame.display.update()

    # события в главном меню
    if playing_game == True:
        # события игры
        # не забыть про open_inventory
        # во время открытого инвенторя игра продолжается

        # Обновление
        active_sprites.update()

        # Рендеринг
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        active_sprites.draw(screen)
        draw_text()
        # Переворачиваем экран после отрисовки
        pygame.display.flip()

    if esc_menu == True:
        pass
    # события меню паузы
pygame.quit()
