import pygame
import drawing
import map


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

    def in_main_menu(self):
        drawing.draw_main_menu(self.screen)
        for event in pygame.event.get():
            if body.click_start_game == True:
                pass

    def in_esc_menu(self):
        pass

    def game_step(self):


    def step(self):
        self.clock.tick(self.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # проверка для закрытия окна
                self.finished = True
        if self.main_menu == True:
            in_main_menu()

        if self.playing_game == True:
            # события игры
            # не забыть про open_inventory
            # во время открытого инвенторя игра продолжается
            loading()
            game_step()
            draw_all()

        if self.esc_menu == True:
            pass
        # события меню паузы

    pygame.quit()
