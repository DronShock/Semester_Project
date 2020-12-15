import pygame
from os import path


class Map:
    def __init__(self):
        """
        Информация об объектах карты (стены и триггеры) хранится в ввиде двумерного массива, где 1 означает стену,
        а элементы большие 1 хранят в себе индекс триггера, которые они вызывают
        """
        self.spawn_center = (0, 0)
        self.map = []
        self.img_dir = None
        self.peremeshenie = None
        self.map_width = 860
        self.map_height = 860

    def collision(self, x, y):
        """
        принимает на вход  координаты объекта и возвращает True если объект упирается в стену,
        False - если нет

        :param x: координата объекта по х
        :param y: координата объекта по у
        :return: True or False
        """
        object_square = [round(x * 20 / self.map_width), round(y * 20 / self.map_height)]
        if self.map[object_square[1]][object_square[0]] == "1":
            return True
        else:
            return False

    def trigger(self, x, y):
        """
        :param x: координата объекта по х
        :param y: координата объекта по y
        :return: Индекс триггера, если нажат триггер
        """
        object_square = [round(x * 20 / self.map_width), round(y * 20 / self.map_height)]
        if int(self.map[object_square[1]][object_square[0]]) > 1:
            return int(self.map[object_square[1]][object_square[0]])
        else:
            return False


def load_map(name, img_dir):
    """
    :param name: имя файла
    :param img_dir: путь к файлу
    :return:
    """
    background = pygame.image.load(path.join(img_dir, name)).convert()
    background_rect = background.get_rect()
    return (background, background_rect)


def sozdanie_maps():
    map1 = Map()
    map1.img_dir = "main_map.png"
    map1.spawn_center = (60, 800)
    map1.map = [
        "11111111100000111111",
        "11111111100000111111",
        "11111111000000111111",
        "00000000000000111111",
        "00000000000000001221",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000111100",
        "00000010000111111100",
        "00000000000111111100",
        "00000000000111111100",
        "00000000000000030000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000000000000000000",
        "00000001111111111111",
        "00000001111111111111",
        "00000001111111111111"
    ]

    map2 = Map()
    map2.img_dir = "map2.png"
    map2.spawn_center = (430, 760)
    map2.map = [
        "11111111111111111111",
        "11111111111111111111",
        "11011010011001011011",
        "10000000000000000001",
        "11000000000000000011",
        "11000000000000000011",
        "10000000000000000001",
        "10000000000000000001",
        "10000000000000000001",
        "10000000000000000001",
        "11000000000000000011",
        "11000000000000000011",
        "10000000000000000001",
        "10000000000000000001",
        "10000000000000000001",
        "10000000000000000001",
        "10000000000000000001",
        "10000000000000000001",
        "11111111144111111111",
        "11111111111111111111"
    ]

    map3 = Map()
    map3.img_dir = "map3.png"
    map3.spawn_center = (90, 660)
    map3.map = [
        "00000000000000000000",
        "01111111111111111110",
        "01111111111111111110",
        "01111111111111111110",
        "01110100111111111110",
        "01000000000000111110",
        "01000000000000000010",
        "01000000000000000010",
        "01000000000000000010",
        "01111111110000000010",
        "01111111110000000010",
        "01111000000000000010",
        "01000000000000000010",
        "01000000000000110010",
        "01000000000000111010",
        "05000000000001110010",
        "01000000000000000010",
        "01001100000000000010",
        "01111111111111111110",
        "00000000000000000000"
    ]
    return map1, map2, map3


def redactor_map(active_map, player):
    """
    :param active_map: действующая в данный момент карта
    :param player: координаты центра для игрока
    :return:
    """
    current_map = active_map
    player.rect.centerx = current_map.spawn_center[0]
    player.rect.centery = current_map.spawn_center[1]
    return current_map
