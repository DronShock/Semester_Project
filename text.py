import pygame
from colors import WHITE
from settings import WIDTH, HEIGHT

class Text:
    """
    Создаёт текст для отображения на экране
    """
    items = []
    active_text = []

    def __init__(self, surf, name, text, size, x, y, sprite=None, reading=False):
        self.font_name = pygame.font.match_font(name)
        self.font = pygame.font.Font(self.font_name, size)
        self.text_surface = self.font.render(text, True, WHITE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (x, y)
        self.reading = reading
        self.surf = surf
        self.sprite = sprite
        Text.items.append(self)

def draw_text():
    for text in Text.active_text:
        text.surf.blit(text.text_surface, text.text_rect)


# Создание текстов для игры
def sozdanie_textov(screen):
    Podskazka = Text(screen, 'arial', "Press 'f' to start reading", 18, 0, 0)
    Privetstvie1 = Text(screen, 'arial',
                        "Приветсвуем Вас в ранней версии нашего игрового проекта,",
                        25, 500, 100)
    Privetstvie2 = Text(screen, 'arial',
                        "совсем скоро Вы сможете испытать его в действии!",
                        25, 500, 150)
    Text.active_text.append(Privetstvie1)
    Text.active_text.append(Privetstvie2)
