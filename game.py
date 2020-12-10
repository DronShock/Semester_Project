import pygame
from text import draw_text
from settings import WIDTH, HEIGHT, FPS
from colors import BLACK


class Game:
    def __init__(self):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.main_menu = True
        self.esc_menu = False
        self.playing_game = False
        self.open_inventory = False
        self.finished = False
        self.FPS = FPS

    def click_start_game(self, x, y):
        if x >= 314 and x <= 688 and y >= 90 and y <= 178:
            return True
        else:
            return False

    def step(self, active_sprites, background, background_rect, main_menu_pict, img_dir, current_map, map1, map2, map3,
             health_bar, mobs, player_anim_up, player_anim_down, player_anim_left, player_anim_right, player_udar_up,
             player_udar_down, player_udar_left, player_udar_right, objects, player_sprite, skelet_anim_up,
             skelet_anim_down, skelet_anim_right,
             skelet_anim_left, player):
        global event
        self.clock.tick(self.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # проверка для закрытия окна
                self.finished = True
        if self.main_menu:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_x, click_y = event.pos
                self.screen.blit(main_menu_pict, (0, 0))
                pygame.display.update()
                if self.click_start_game(click_x, click_y):
                    self.main_menu = False
                    self.playing_game = True
                    self.screen.fill(BLACK)
                    pygame.display.update()

        if self.playing_game:
            # Обновление
            player_sprite.update(img_dir, current_map, map1, map2, map3, health_bar, mobs, player_anim_up,
                                 player_anim_down, player_anim_left, player_anim_right, player_udar_up,
                                 player_udar_down, player_udar_left, player_udar_right)
            objects.update(img_dir, current_map, map1, map2, map3, health_bar, mobs, player_anim_up,
                           player_anim_down, player_anim_left, player_anim_right, player_udar_up,
                           player_udar_down, player_udar_left, player_udar_right)
            mobs.update(player, active_sprites, img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right,
                        skelet_anim_left)
            # Рендеринг
            self.screen.fill(BLACK)
            self.screen.blit(background, background_rect)
            active_sprites.draw(self.screen)
            draw_text()
            # Переворачиваем экран после отрисовки
            pygame.display.flip()

    pygame.quit()
