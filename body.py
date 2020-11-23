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
            self.animation("up")
            self.speedy = -3
        if keystate[pygame.K_DOWN]:
            self.animation("down")
            self.speedy = 3
        if keystate[pygame.K_LEFT]:
            self.animation("left")
            self.fix_scorosti()
        if keystate[pygame.K_RIGHT]:
            self.animation("right")
            self.fix_scorosti()
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

    def animation(self, move):
        time = pygame.time.get_ticks()
        if time - self.last_update > self.frame_rate:
            self.last_update = time
            self.frame += 1
            if self.frame == len(eval('player_anim_{}'.format(move))):
                self.frame = 0
            self.image = pygame.image.load(path.join(img_dir,eval('player_anim_{}'.format(move))[self.frame])).convert()
            self.image.set_colorkey(BLACK)

    def fix_scorosti(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            if keystate[pygame.K_UP]:
                self.speedx = -3/(2**(1/2))
                self.speedy = -3/(2**(1/2))
            elif keystate[pygame.K_DOWN]:
                self.speedx = -3/(2**(1/2))
                self.speedy = 3/(2**(1/2))
            else:
                self.speedx= -3
        if keystate[pygame.K_RIGHT]:
            if keystate[pygame.K_UP]:
                self.speedx = 3/(2**(1/2))
                self.speedy = -3/(2**(1/2))
            elif keystate[pygame.K_DOWN]:
                self.speedx = 3/(2**(1/2))
                self.speedy = 3/(2**(1/2))
            else:
                self.speedx= 3


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


def click_start_game(x, y):
    if x >= 314 and x <= 688 and y >= 90 and y <= 178:
        return True
    else:
        return False


# Загрузка изображений объектов
background = pygame.image.load(path.join(img_dir, 'DB32RecolorEx.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "player.png")).convert()
main_menu_pict = pygame.image.load('main_menu1.png')
# Создание массивов с анимациями
player_anim_up = ['Up 0.png', 'Up 1.png', 'Up 0.png', 'Up 2.png']
player_anim_down = ['Down 0.png', 'Down 1.png', 'Down 0.png', 'Down 2.png']
player_anim_left = ['Left 0.png', 'Left 1.png', 'Left 0.png', 'Left 2.png']
player_anim_right = ['Right 0.png', 'Right 1.png', 'Right 0.png', 'Right 2.png']

# Добавления спрайтов в группу для отрисовки
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
