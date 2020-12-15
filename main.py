import pygame
from game import Game
from map import redactor_map, load_map, sozdanie_maps
from player import create_characters, sozdanie_vragov, udalenie_vragov
from objects import sozdanie_objectov, vinoslivost
from text import sozdanie_textov1, sozdanie_textov2, sozdanie_textov_questa, udalenie_textov
from images import create_pictures
from os import path

# Объявление папки с картинками
img_dir = path.join(path.dirname(__file__), 'img')
# Инициализация пайгейма
pygame.init()
pygame.mixer.init()
g = Game()
screen = g.screen

# Перенос картинок в главный цикл
(player_img, main_menu_pict, skelet_anim_up, skelet_anim_down, skelet_anim_left, skelet_anim_right, player_anim_up,
 player_anim_down, player_anim_left, player_anim_right, player_udar_up, player_udar_down, player_udar_left,
 player_udar_right, death_screen) = create_pictures(img_dir)

# Создание групп спрайтов
(active_sprites, player_sprite, player, mobs) = create_characters(player_img)

# Создание объектов
(objects, health_bar, dialog_box, npc, stamina_bar, stamina_bar0, svitok) = sozdanie_objectov(active_sprites, img_dir)

# Создание карт и фона
(map1, map2, map3) = sozdanie_maps()
current_map = redactor_map(map1, player)
(background, background_rect) = load_map(current_map.img_dir, img_dir)

# Загрузка музыки
pygame.mixer.music.load(path.join(img_dir, 'TownTheme.mp3'))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)
clock = pygame.time.Clock()
while not g.finished:
    player.next_x = player.rect.x + int(player.speedx)
    player.next_y = player.rect.y + int(player.speedy)
    if current_map.trigger(player.next_x, player.next_y) > 1:
        id = current_map.trigger(player.next_x, player.next_y)
        if current_map == map1:
            if id == 2:
                sozdanie_vragov(mobs, active_sprites)
                current_map = redactor_map(map2, player)
            if id == 3:
                active_sprites.add(npc)
                current_map = redactor_map(map3, player)
        if current_map == map2:
            if id == 4:
                udalenie_vragov(mobs, active_sprites)
                map1.spawn_center = (760, 250)
                current_map = redactor_map(map1, player)
        if current_map == map3:
            if id == 5:
                active_sprites.remove(npc)
                map1.spawn_center = (690, 520)
                current_map = redactor_map(map1, player)
        (background, background_rect) = load_map(current_map.img_dir, img_dir)
    vinoslivost(player, active_sprites, stamina_bar, stamina_bar0)
    g.step(active_sprites, background, background_rect, main_menu_pict, img_dir, current_map, map1, map2, map3,
           health_bar, mobs, player_anim_up, player_anim_down, player_anim_left, player_anim_right, player_udar_up,
           player_udar_down, player_udar_left, player_udar_right, objects, player_sprite, skelet_anim_up,
           skelet_anim_down, skelet_anim_right,
           skelet_anim_left, player)
    if current_map == map1:
        if player.rect.x < 100 and player.rect.y > 760:
            sozdanie_textov1(screen)
            active_sprites.add(dialog_box)
            active_sprites.add(svitok)
        else:
            udalenie_textov()
            active_sprites.remove(dialog_box)
            active_sprites.remove(svitok)
    if current_map == map3:
        if player.rect.x < 100 and player.rect.y > 600:
            sozdanie_textov2(screen)
            active_sprites.add(dialog_box)
            active_sprites.add(svitok)
        elif player.rect.x < 250 and 450 < player.rect.y < 550:
            sozdanie_textov_questa(screen)
            active_sprites.add(dialog_box)
            active_sprites.add(svitok)
        else:
            udalenie_textov()
            active_sprites.remove(dialog_box)
            active_sprites.remove(svitok)
    if player.health_points == 0:
        g.screen.blit(death_screen, (0, 0))
        pygame.display.update()
        pygame.time.wait(1000)
        g.playing_game = False
pygame.quit()
