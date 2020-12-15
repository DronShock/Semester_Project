import pygame
from text import draw_text
from settings import WIDTH, HEIGHT, FPS
from colors import BLACK


# Определяют область нажатия
def click_new_game(x, y):
    return (x >= 250) and (x <= 610) and 249 <= y <= 336


def click_continue(x, y):
    return 250 <= x <= 610 and 412 <= y <= 499


# Объявление класса игры
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing_game = False
        self.finished = False
        self.FPS = FPS

    def in_main_menu(self, main_menu_pict):
        """
        Работа в меню
        :param main_menu_pict:
        :return: None
        """
        self.screen.blit(main_menu_pict, (0, 0))
        pygame.display.update()
        if self.event.type == pygame.MOUSEBUTTONDOWN and self.event.button == 1:
            click_x, click_y = self.event.pos
            if click_new_game(click_x, click_y) or click_continue(click_x, click_y):
                self.playing_game = True
                self.screen.fill(BLACK)
                pygame.display.update()

    # Рассчитывает один игровой шаг
    def step(self, active_sprites, background, background_rect, main_menu_pict, img_dir, current_map, map1, map2, map3,
             health_bar, mobs, player_anim_up, player_anim_down, player_anim_left, player_anim_right, player_udar_up,
             player_udar_down, player_udar_left, player_udar_right, objects, player_sprite, skelet_anim_up,
             skelet_anim_down, skelet_anim_right,
             skelet_anim_left, player):
        self.clock.tick(self.FPS)
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                # проверка для закрытия окна
                self.finished = True

        if self.playing_game:
            # Обновление
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                self.playing_game = False
            player_sprite.update(img_dir, current_map, map1, map2, map3, health_bar, mobs, player_anim_up,
                                 player_anim_down, player_anim_left, player_anim_right, player_udar_up,
                                 player_udar_down, player_udar_left, player_udar_right)
            objects.update(img_dir, current_map, map1, map2, map3, health_bar, mobs, player_anim_up,
                           player_anim_down, player_anim_left, player_anim_right, player_udar_up,
                           player_udar_down, player_udar_left, player_udar_right)
            mobs.update(player, active_sprites, img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right,
                        skelet_anim_left, player_sprite)

            # Рендеринг
            self.screen.fill(BLACK)
            self.screen.blit(background, background_rect)
            active_sprites.draw(self.screen)
            draw_text()
            # Переворачиваем экран после отрисовки
            pygame.display.flip()
        else:
            self.in_main_menu(main_menu_pict)

    pygame.quit()
