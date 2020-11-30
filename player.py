import pygame

WIDTH = 1000
HEIGHT = 650
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
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

    def update(self):
        """
        Обновляет положение игрока на экране
        :return: None
        """
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.animation("up")
            self.speedy = -3
        if keystate[pygame.K_DOWN]:
            self.animation("down")
            self.speedy = 3
        if keystate[pygame.K_LEFT]:
            self.animation("left")
            self.fix_scorosti()
        if keystate[pygame.K_RIGHT]:
            self.animation("right")
            self.fix_scorosti()
        self.rect.x += int(self.speedx)
        self.rect.y += int(self.speedy)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        self.stolknovenia()

    def stolknovenia(self):
        hits = pygame.sprite.spritecollide(self, objects, False)
        if hits:
            if self.speedx<0:
                self.rect.left = hits[0].rect.right
            elif self.speedx>0:
                self.rect.right = hits[0].rect.left
            elif self.speedy<0:
                self.rect.top = hits[0].rect.bottom
            elif self.speedy>0:
                self.rect.bottom = hits[0].rect.top

    def animation(self, move):
        time = pygame.time.get_ticks()
        if time - self.last_update > self.frame_rate:
            self.last_update = time
            self.frame += 1
            if self.frame == len(eval('player_anim_{}'.format(move))):
                self.frame = 0
            self.image = pygame.image.load(
                path.join(img_dir, eval('player_anim_{}'.format(move))[self.frame])).convert()
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
