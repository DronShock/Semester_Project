import pygame as pg

# from game_objects import *

# какой то текст
# считывание размеров экрана
# import ctypes
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

screen_width = 1000
screen_height = 650
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
FPS = 40
active_buttons = []  # Массив с активными кнопками клавиатуры
characters = []

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
screen.fill(BLACK)
pg.display.update()
clock = pg.time.Clock()

finished = False
main_menu = True
esc_menu = False
playing_game = False
open_inventory = False


class player():
    def __init__(self, x, y, speed, image):
        self.width = 50
        self.height = 50
        self.x = 0
        self.y = 0
        self.speed = speed
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))

    def go_to(self, x, y):
        '''
        функция должна заставлять идти объект к точке (x,y)
        желательно еще связать это со скоростью
        функция будет использоваться восновном для MPC
        '''
        x += ((self.x - x) * self.speed) / (((y - self.y) ** 2 + (x - self.x) ** 2) ** 0.5 * FPS)
        y += ((self.y - y) * self.speed) / (((y - self.y) ** 2 + (x - self.x) ** 2) ** 0.5 * FPS)

    def go_button(self, button):
        '''
        функция перемещения для игрока
        w,a,s,d -- булевские переменные соответствующие нажатию на такие же кнопки
        true -- кнопка
        не забыть про одновременное нажатие на кнопок и постоянную скорость
        '''
        if button == "w":
            self.y += self.speed / FPS
        if button == "a":
            self.x -= self.speed / FPS
        if button == "s":
            self.y -= self.speed / FPS
        if button == "d":
            self.x += self.speed / FPS

        if button == "wd":
            self.y += self.speed * 0.71 / FPS
            self.x += self.speed * 0.71 / FPS
        if button == "wa":
            self.y += self.speed * 0.71 / FPS
            self.x -= self.speed * 0.71 / FPS
        if button == "sa":
            self.y -= self.speed * 0.71 / FPS
            self.x -= self.speed * 0.71 / FPS
        if button == "sd":
            self.y -= self.speed * 0.71 / FPS
            self.x += self.speed * 0.71 / FPS


characters.append(player)


def check_keyboard_buttons(event):
    """Функция записывает нажатые кенопки в массив active_buttons"""
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_w:
            active_buttons.append("w")
        if event.key == pg.K_a:
            active_buttons.append("a")
        if event.key == pg.K_s:
            active_buttons.append("s")
        if event.key == pg.K_d:
            active_buttons.append("d")

    if event.type == pg.KEYUP:
        if event.key == pg.K_w:
            active_buttons.remove("w")
        if event.key == pg.K_a:
            active_buttons.remove("a")
        if event.key == pg.K_s:
            active_buttons.remove("s")
        if event.key == pg.K_d:
            active_buttons.remove("d")


def do_command():
    """Выполняет команды исходя из нажатых кнопок"""
    global esc_menu
    global open_inventory

    if "w" in active_buttons:
        player.go_button("w")
    if "a" in active_buttons:
        player.go_button("a")
    if "s" in active_buttons:
        player.go_button("s")
    if "d" in active_buttons:
        player.go_button("d")
    if "w" in active_buttons and "d" in active_buttons:
        player.go_button("wd")
    if "w" in active_buttons and "a" in active_buttons:
        player.go_button("wa")
    if "s" in active_buttons and "a" in active_buttons:
        player.go_button("sa")
    if "s" in active_buttons and "d" in active_buttons:
        player.go_button("sd")


# def update_characters_image():
#    for character in characters:
#        character.image.blit(screen, (character.x,character.y))
#        pg.display.update()

def button_start_game(x, y):
    if (x >= 314) and (x <= 688) and (y >= 90) and (y <= 178):
        return True
    else:
        return False


menu_pict = pg.image.load('main_menu1.png')

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        # update_characters_image()
        if main_menu == True:
            # события в главном меню
            screen.blit(menu_pict, (0, 0))
            pg.display.update()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                click_x, click_y = event.pos
                if button_start_game(click_x, click_y) == True:
                    main_menu = False
                    playing_game = True
                    screen.fill(BLACK)
                    pg.display.update()
        if playing_game == True:
            check_keyboard_buttons(event)
            do_command()

            # события игры
            # не забыть про open_inventory
            # во время открытого инвенторя игра продолжается
        if esc_menu == True:
            pass
            # события меню паузы

pg.quit()
