import pygame
from game import Game
from map import redactor_map, load_map, sozdanie_maps
from player import create_characters, sozdanie_vragov
from objects import sozdanie_objectov, HealthBar
from text import sozdanie_textov
from images import create_pictures
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
pygame.init()
pygame.mixer.init()
g = Game()
screen = g.screen

(player_img, main_menu_pict, skelet_anim_up, skelet_anim_down, skelet_anim_left, skelet_anim_right, player_anim_up,
 player_anim_down, player_anim_left, player_anim_right, player_udar_up, player_udar_down, player_udar_left,
 player_udar_right) = create_pictures(img_dir)

sozdanie_vragov(player_img)
(active_sprites, player_sprite, player, mobs) = create_characters(player_img)
(objects, health_bar) = sozdanie_objectov(active_sprites, img_dir)
(map1, map2, map3) = sozdanie_maps()
current_map = redactor_map(map1, player)
(background, background_rect) = load_map(current_map.img_dir, img_dir)
sozdanie_textov(g.screen)

finished = False
clock = pygame.time.Clock()
while not finished:
    g.step(active_sprites, background, background_rect, main_menu_pict, img_dir, current_map, map1, map2, map3,
           health_bar, mobs, player_anim_up, player_anim_down, player_anim_left, player_anim_right, player_udar_up,
           player_udar_down, player_udar_left, player_udar_right,player_sprite,objects,skelet_anim_up, skelet_anim_down, skelet_anim_right,
               skelet_anim_left,player)
pygame.quit()
