import pygame

#какой то текст
# считывание размеров экрана
# import ctypes
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.init()
screen = pygame.display.set_mode((1000, 650))

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


class obj():
    class creature():
        def __init__(self, x, y, speed):
            self.x = x
            self.y = y
            self.speed = speed

        def go_to(self, x, y):
            '''
            функция должна заставлять идти объект к точке (x,y)
            желательно еще связать это со скоростью
            функция будет использоваться восновном для MPC
            '''

        def go_button(self, w, a, s, d):
            '''
            функция перемещения для игрока
            w,a,s,d -- булевские переменные соответствующие нажатию на такие же кнопки
            true -- кнопка
            не забыть про одновременное нажатие на кнопок и постоянную скорость
            '''

        class MPC():
            class peaceful():
                pass

            class enemy():
                def attack(self):
                    pass

        class player():
            def change_item(self):
                '''
                функция меняет предмет в руке
                '''

            def change_armor(self):
                '''
                функция меняет броню
                '''


clock = pygame.time.Clock()
finished = False
FPS = 40
screen.fill(BLACK)
pygame.display.update()
main_menu = True
esc_menu = False
playing_game = False
open_inventory = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if main_menu == True:
            pass
            # события в главном меню
        if playing_game == True:
            pass
            # события игры
            # не забыть про open_inventory
            # во время открытого инвенторя игра продолжается
        if esc_menu == True:
            pass
            # события меню паузы
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
#
