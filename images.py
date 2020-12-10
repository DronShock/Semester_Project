import pygame
from os import path


def create_pictures(img_dir):
    player_img = pygame.image.load(path.join(img_dir, "Down_0.png")).convert()
    player_img = pygame.transform.scale(player_img, (35, 43))
    main_menu_pict = pygame.image.load('main_menu1.png')
    main_menu_pict = pygame.transform.scale(main_menu_pict, (860, 860))
    derevo1 = pygame.image.load(path.join(img_dir, 'Derevo 1.png')).convert()
    Svitok = pygame.image.load(path.join(img_dir, 'Svitok.png')).convert()
    Svitok = pygame.transform.scale(Svitok, (20, 30))

    # Создание массивов с анимациями
    skelet_anim_up = ['Up 0.png', 'Up 1.png', 'Up 0.png', 'Up 2.png']
    skelet_anim_down = ['Down 0.png', 'Down 1.png', 'Down 0.png', 'Down 2.png']
    skelet_anim_left = ['Left 0.png', 'Left 1.png', 'Left 0.png', 'Left 2.png']
    skelet_anim_right = ['Right 0.png', 'Right 1.png', 'Right 0.png', 'Right 2.png']

    player_anim_up = ['Up_0.png', 'Up_1.png', 'Up_0.png', 'Up_2.png']
    player_anim_down = ['Down_0.png', 'Down_1.png', 'Down_0.png', 'Down_2.png']
    player_anim_left = ['Left_0.png', 'Left_1.png', 'Left_0.png', 'Left_2.png']
    player_anim_right = ['Right_0.png', 'Right_1.png', 'Right_0.png', 'Right_2.png']

    player_udar_up = pygame.image.load(path.join(img_dir, "Udar_Up.png")).convert()
    player_udar_down = pygame.image.load(path.join(img_dir, "Udar_Down.png")).convert()
    player_udar_left = pygame.image.load(path.join(img_dir, "Udar_Left.png")).convert()
    player_udar_right = pygame.image.load(path.join(img_dir, "Udar_Right.png")).convert()
    player_udar_up = pygame.transform.scale(player_udar_up, (30, 75))
    player_udar_down = pygame.transform.scale(player_udar_down, (30, 75))
    player_udar_left = pygame.transform.scale(player_udar_left, (75, 46))
    player_udar_right = pygame.transform.scale(player_udar_right, (75, 46))
    return (
        player_img, main_menu_pict, skelet_anim_up, skelet_anim_down, skelet_anim_left, skelet_anim_right,
        player_anim_up,
        player_anim_down, player_anim_left, player_anim_right, player_udar_up, player_udar_down, player_udar_left,
        player_udar_right)
