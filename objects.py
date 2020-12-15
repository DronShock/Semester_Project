import pygame
from colors import BLACK
from os import path


class Objects(pygame.sprite.Sprite):
    items = []

    def __init__(self, x, y, image, text=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.text = text
        Objects.items.append(self)


class HealthBar(Objects):
    def __init__(self, x, y, img_dir):
        super().__init__(x, y, image=pygame.image.load(path.join(img_dir, 'HealthBar_5.png')).convert())
        self.image = pygame.image.load(path.join(img_dir, 'HealthBar_5.png')).convert()
        self.image.set_colorkey(BLACK)

    def umenshenie_hp(self, player, img_dir):
        self.image = pygame.image.load(
            path.join(img_dir, 'HealthBar_{}.png'.format(player.health_points // 5))).convert()
        self.image.set_colorkey(BLACK)


class NPS(Objects):
    pass


def sozdanie_objectov(active_sprites, img_dir):
    health_bar = HealthBar(120, 50, img_dir)
    svitok_image = pygame.image.load(path.join(img_dir, 'Svitok.png')).convert()
    svitok_image = pygame.transform.scale(svitok_image, (40, 34))
    svitok = Objects(460,350,svitok_image)
    stamina_bar = Objects(120, 80, pygame.image.load(path.join(img_dir, 'GreenBar.png')).convert())
    stamina_bar0 = Objects(120, 80, pygame.image.load(path.join(img_dir, 'EmptyBar.png')).convert())
    npc_image = pygame.image.load(path.join(img_dir, 'NPC_down.png')).convert()
    npc_image = pygame.transform.scale(npc_image, (25, 50))
    npc = Objects(195, 510, npc_image)
    dialog_box = Objects(450, 300, pygame.image.load(path.join(img_dir, 'dialog_box.png')).convert())
    objects = pygame.sprite.Group()
    for smth in Objects.items:
        objects.add(smth)
    active_sprites.add(health_bar)
    active_sprites.add(stamina_bar)
    active_sprites.add(dialog_box)
    active_sprites.add(svitok)
    return objects, health_bar, dialog_box, npc, stamina_bar, stamina_bar0,svitok


def vinoslivost(player, active_sprites, stamina_bar, stamina_bar0):
    if player.udar_flag != 0:
        active_sprites.remove(stamina_bar)
        active_sprites.add(stamina_bar0)
    else:
        active_sprites.remove(stamina_bar0)
        active_sprites.add(stamina_bar)
