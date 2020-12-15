import pygame
from colors import BLACK
from settings import WIDTH, HEIGHT
from os import path
from objects import HealthBar


class Player(pygame.sprite.Sprite):
    def __init__(self, player_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.health_points = 20
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.move = "up"
        self.uron = None
        self.udar_flag = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 200

    def update(self, img_dir, current_map, map1, map2, map3, health_bar, mobs, player_anim_up,
               player_anim_down, player_anim_left, player_anim_right, player_udar_up, player_udar_down,
               player_udar_left, player_udar_right):
        """
        Обновляет положение игрока на экране
        :return: None
        """
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.move = "up"
            self.speedy = -3
        if keystate[pygame.K_DOWN]:
            self.move = "down"
            self.speedy = 3
        if keystate[pygame.K_LEFT]:
            self.move = "left"
            self.fix_scorosti()
        if keystate[pygame.K_RIGHT]:
            self.move = "right"
            self.fix_scorosti()
        if self.speedx != 0 or self.speedy != 0:
            self.animation(self.move, img_dir, player_anim_up, player_anim_down, player_anim_left, player_anim_right)

        # Обновление координат
        self.next_x = self.rect.x + int(self.speedx)
        self.next_y = self.rect.y + int(self.speedy)
        if not current_map.collision(self.next_x, self.next_y):
            self.rect.x += int(self.speedx)
            self.rect.y += int(self.speedy)
            self.next_x = self.rect.x
            self.next_y = self.rect.y

        # Проверка границ экрана
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        self.udar(player_udar_up, player_udar_down, player_udar_left, player_udar_right)
        self.bitva(mobs, health_bar)



    def udar(self, player_udar_up, player_udar_down, player_udar_left, player_udar_right):
        self.uron = None
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and self.udar_flag == 0:
            self.udar_flag = 30
            self.image = eval("player_udar_{}".format(self.move)).convert()
            self.uron = self.move
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        if self.udar_flag > 0:
            self.udar_flag -= 1

    def bitva(self, mobs, health_bar):
        hits = pygame.sprite.spritecollide(self, mobs, False, pygame.sprite.collide_rect_ratio(0.2))
        if hits:
            self.health_points -= 1
            HealthBar.umenshenie_hp(health_bar, self, img_dir=path.join(path.dirname(__file__), 'img'))

    def animation(self, move, img_dir, player_anim_up, player_anim_down, player_anim_left, player_anim_right):
        time = pygame.time.get_ticks()
        if time - self.last_update > self.frame_rate:
            self.last_update = time
            self.frame += 1
            if self.frame == len(eval('player_anim_{}'.format(move))):
                self.frame = 0
            self.image = pygame.image.load(
                path.join(img_dir, eval('player_anim_{}'.format(move))[self.frame])).convert()
            self.image = pygame.transform.scale(self.image, (35, 43))
            self.image.set_colorkey(BLACK)
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def fix_scorosti(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            if keystate[pygame.K_UP]:
                self.speedx = -3 / (2 ** (1 / 2))
                self.speedy = -3 / (2 ** (1 / 2))
            elif keystate[pygame.K_DOWN]:
                self.speedx = -3 / (2 ** (1 / 2))
                self.speedy = 3 / (2 ** (1 / 2))
            else:
                self.speedx = -3
        if keystate[pygame.K_RIGHT]:
            if keystate[pygame.K_UP]:
                self.speedx = 3 / (2 ** (1 / 2))
                self.speedy = -3 / (2 ** (1 / 2))
            elif keystate[pygame.K_DOWN]:
                self.speedx = 3 / (2 ** (1 / 2))
                self.speedy = 3 / (2 ** (1 / 2))
            else:
                self.speedx = 3


class Enemy(pygame.sprite.Sprite):
    items = []

    def __init__(self, x, y, player_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.health_points = 5
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 200
        Enemy.items.append(self)

    def update(self, player, active_sprites, img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right,
               skelet_anim_left, player_sprite):
        if self.rect.centery > player.rect.centery:
            self.speedy = -1
            self.animation("up", img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right, skelet_anim_left)
        elif self.rect.centery < player.rect.centery:
            self.speedy = 1
            self.animation("down", img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right, skelet_anim_left)
        else:
            self.speedy = 0
            if self.rect.centerx > player.rect.centerx:
                self.speedx = -1
                self.animation("left", img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right,
                               skelet_anim_left)
            else:
                self.speedx = 1
                self.animation("right", img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right,
                               skelet_anim_left)
        if self.rect.centerx >= player.rect.centerx:
            self.speedx = -1
            self.animation("left", img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right, skelet_anim_left)
        else:
            self.speedx = 1
            self.animation("right", img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right,
                           skelet_anim_left)

        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        self.poluchenie_urona(player_sprite, player)

    def poluchenie_urona(self, player_sprite, player):
        hits = pygame.sprite.spritecollide(self, player_sprite, False, pygame.sprite.collide_rect_ratio(1.1))
        if player.uron is not None:
            if hits:
                self.health_points -= 1
                self.rect.centerx -= 20 * self.speedx // (abs(self.speedx)+0.1)
                self.rect.centery -= 20 * self.speedy // (abs(self.speedy)+0.1)
        if self.health_points == 0:
            self.kill()

    def animation(self, move, img_dir, skelet_anim_up, skelet_anim_down, skelet_anim_right, skelet_anim_left):
        time = pygame.time.get_ticks()
        if time - self.last_update > self.frame_rate:
            self.last_update = time
            self.frame += 1
            if self.frame == len(eval('skelet_anim_{}'.format(move))):
                self.frame = 0
            self.image = pygame.image.load(
                path.join(img_dir, eval('skelet_anim_{}'.format(move))[self.frame])).convert()
            self.image.set_colorkey(BLACK)
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center


def create_characters(player_img):
    active_sprites = pygame.sprite.Group()
    player_sprite = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    skelet1 = Enemy(100, 200, player_img)
    skelet3 = Enemy(300, 100, player_img)
    skelet2 = Enemy(200, 300, player_img)
    skelet4 = Enemy(400, 400, player_img)
    skelet5 = Enemy(500, 500, player_img)
    skelet6 = Enemy(500, 100, player_img)
    skelet7 = Enemy(700, 200, player_img)
    skelet8 = Enemy(200, 600, player_img)
    skelet9 = Enemy(600, 400, player_img)
    skelet10 = Enemy(100, 500, player_img)
    player = Player(player_img)
    active_sprites.add(player)
    player_sprite.add(player)
    return active_sprites, player_sprite, player, mobs


def sozdanie_vragov(player_img, mobs, active_sprites):
    for mob in Enemy.items:
        mobs.add(mob)
        active_sprites.add(mob)


def udalenie_vragov(mobs, active_sprites):
    for mob in Enemy.items:
        mobs.add(mob)
        active_sprites.remove(mob)

