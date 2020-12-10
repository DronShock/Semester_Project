import pygame
from colors import BLACK
from os import path


class Objects(pygame.sprite.Sprite):
    items = []

    def __init__(self, position, x, y, image, text=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.position = position
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.text = text
        Objects.items.append(self)


class HealthBar(Objects):
    def __init__(self, position, x, y, img_dir):
        super().__init__(position, x, y,image=pygame.image.load(path.join(img_dir, 'HealthBar_5.png')).convert())
        self.image = pygame.image.load(path.join(img_dir, 'HealthBar_5.png')).convert()

    def umenshenie_hp(self, player, img_dir):
        self.image = pygame.image.load(
            path.join(img_dir, 'HealthBar_{}.png'.format(player.health_points // 5))).convert()
        self.image.set_colorkey(BLACK)


def sozdanie_objectov(active_sprites, img_dir):
    health_bar = HealthBar(0, 120, 50, img_dir)
    objects = pygame.sprite.Group()
    for smth in Objects.items:
        objects.add(smth)
        active_sprites.add(smth)
    return objects, health_bar
