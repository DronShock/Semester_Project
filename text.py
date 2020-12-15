import pygame
from colors import BLACK
from settings import WIDTH, HEIGHT


class Text:
    """
    Создаёт текст для отображения на экране
    """
    items = []
    active_text = []

    def __init__(self, surf, name, text, size, x, y, reading=False):
        self.font_name = pygame.font.match_font(name)
        self.font = pygame.font.Font(self.font_name, size)
        self.text_surface = self.font.render(text, True, BLACK)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (x, y)
        self.reading = reading
        self.surf = surf
        Text.items.append(self)


def draw_text():
    for text in Text.active_text:
        text.surf.blit(text.text_surface, text.text_rect)


# Создание текстов для игры
def sozdanie_textov1(screen):
    Message1 = Text(screen, 'arial', "Что происходит? Где я оказался? Я же готовился к экзамену по матану.", 18, 450,
                      220)
    Message2 = Text(screen, 'arial', "Наверное, это лишь сон, но мне всё же стоит осмотреться вокруг.", 18, 450, 245)
    Message3 = Text(screen, 'arial', "(Используйте стрелочки для перемещения и пробел для удара.)", 18, 450, 275)
    Text.active_text.append(Message1)
    Text.active_text.append(Message2)
    Text.active_text.append(Message3)

def sozdanie_textov2(screen):
    Message1 = Text(screen, 'arial', "Похоже, что не стоило всю ночь зубрить теоремы. От такого количества кофе мне", 18, 450,
                      220)
    Message2 = Text(screen, 'arial', "мерещится толпа народа. Хмм, кажется, что этот старец сидит", 18, 450, 245)
    Message3 = Text(screen, 'arial', "здесь не просто так. Надо спросить у него, что тут к чему", 18, 450, 275)
    Text.active_text.append(Message1)
    Text.active_text.append(Message2)
    Text.active_text.append(Message3)
def sozdanie_textov_questa(screen):
    Quest1 = Text(screen, 'arial', "Приветствую тебя, юный первокур. Ты, наверное, растерян и не понимаешь, что происходит?", 18, 450,
                      220)
    Quest2 = Text(screen, 'arial', " Не буду тратить твоё время и рассказывать утомительную, но поучительную притчу об учёбе на Физтехе.", 18, 450, 245)
    Quest3 = Text(screen, 'arial', " Скажу лишь, что для того, чтобы выбраться тебе потребуется покончить с 'долгами' в соседнем замке. Удачи!", 18, 450, 275)
    Text.active_text.append(Quest1)
    Text.active_text.append(Quest2)
    Text.active_text.append(Quest3)

def udalenie_textov():
    Text.active_text.clear()
