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
        self.move = "up"
        self.uron = None
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
            self.animation(self.move)
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
        self.udar()

    def stolknovenia(self):
        hits = pygame.sprite.spritecollide(self, elementi_karti, False)
        if hits:
            if self.speedx < 0:
                self.rect.left = hits[0].rect.right
            elif self.speedx > 0:
                self.rect.right = hits[0].rect.left
            elif self.speedy < 0:
                self.rect.top = hits[0].rect.bottom
            elif self.speedy > 0:
                self.rect.bottom = hits[0].rect.top

    def udar(self):
        self.uron = None
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            time = pygame.time.get_ticks()
            self.image = eval("player_udar_{}".format(self.move)).convert()
            self.uron = self.move
            #self.image = pygame.image.load(path.join(img_dir, eval('player_anim_{}'.format(self.move))[0])).convert()
            #self.image = pygame.transform.scale(self.image, (35, 43))
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def animation(self, move):
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
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.health_points = 15
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.speedy = 0
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 200

    def update(self):
        if self.rect.centery > player.rect.centery:
            self.speedy = -1
            self.animation("up")
        elif self.rect.centery < player.rect.centery:
            self.speedy = 1
            self.animation("down")
        else:
            self.speedy = 0
            if self.rect.centerx > player.rect.centerx:
                self.speedx = -1
                self.animation("left")
            else:
                self.speedx = 1
                self.animation("right")
        if self.rect.centerx >= player.rect.centerx:
            self.speedx = -1
            self.animation("left")
        else:
            self.speedx = 1
            self.animation("right")

        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        self.poluchenie_urona()

    def poluchenie_urona(self):
        active_sprites.remove(self)
        hits = pygame.sprite.spritecollide(self, active_sprites, False,pygame.sprite.collide_rect_ratio(0.8))
        active_sprites.add(self)
        if player.uron is not None:
            if hits:
                self.health_points -= 1
                self.rect.centerx -= 20 * self.speedx // abs(self.speedx)
        if self.health_points == 0:
            self.kill()

    def animation(self, move):
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