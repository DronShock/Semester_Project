import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

# какой то текст
# считывание размеров экрана
# import ctypes
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

WIDTH = 1000
HEIGHT = 800
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
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 500

    def update(self):
        """
        Обновляет положение игрока на экране
        :return: None
        """
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.animation("left")
            self.speedx = -3
        if keystate[pygame.K_RIGHT]:
            self.speedx = 3
            self.animation("right")
        if keystate[pygame.K_UP]:
            self.animation("up")
            self.speedy = -3
        if keystate[pygame.K_DOWN]:
            self.animation("down")
            self.speedy = 3
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def animation(self, move):
        time = pygame.time.get_ticks()
        if time - self.last_update < self.frame_rate:
            self.last_update = time
            if move == "up":
                for anim in player_anim_up:
                    self.frame += 1
                    if self.frame == len(player_anim_up):
                        anim in player_anim_up[0]
                    else:
                        self.image = pygame.image.load(path.join(img_dir, anim)).convert()
                        self.image.set_colorkey(BLACK)

    def change_item(self):
        """
        функция меняет предмет в руке
        """

    def change_armor(self):
        """
        функция меняет броню
        """


class Camera():
    pass


class obj():
    pass


class creature(obj):
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


class NPC(obj):
    pass


class peaceful(NPC):
    pass


class enemy(NPC):
    def attack(self):
        pass


# Загрузка изображений объектов
background = pygame.image.load(path.join(img_dir, 'DB32RecolorEx.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "player.png")).convert()

# Создание массивов с анимациями
player_anim_up = ['Up 0.png', 'Up 1.png', 'Up 0.png', 'Up 2.png']
player_anim_down = [('Down 0.png'), ('Down 1.png'), ('Down 0.png'), ('Down 2.png')]
player_anim_left = [('Left 0.png'), ('Left 1.png'), ('Left 0.png'), ('Left 2.png')]
player_anim_right = [('Right 0.png'), ('Right 1.png'), ('Right 0.png'), ('Right 2.png')]

# Добавления спрайтов в группу для отрисовки
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

main_menu = False
esc_menu = False
playing_game = True
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
        pass
    # события в главном меню
    if playing_game == True:
        # события игры
        # не забыть про open_inventory
        # во время открытого инвенторя игра продолжается

        # Обновление
        all_sprites.update()

        # Рендеринг
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        # Переворачиваем экран после отрисовки
        pygame.display.flip()

    if esc_menu == True:
        pass
    # события меню паузы
pygame.quit()
