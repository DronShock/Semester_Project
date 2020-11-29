import pygame
from in_playing_game import playing

class Game:
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 650
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.main_menu = True
        self.esc_menu = False
        self.playing_game = False
        self.open_inventory = False
        self.finished = False
        self.FPS = 40
    def step(self):
        self.clock.tick(self.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # проверка для закрытия окна
                self.finished = True
        if self.main_menu == True:
            pass
                #подлкючить сюда файл in_main_menu
        if self.playing_game == True:
            # события игры
            # не забыть про open_inventory
            # во время открытого инвенторя игра продолжается
            play()


        if self.esc_menu == True:
            pass
        # события меню паузы
    pygame.quit()