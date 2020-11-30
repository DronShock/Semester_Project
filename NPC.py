import pygame as pg

class NPC:
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 200