class Box:
    ''' просто класс прямоугольник'''

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def box_near_box(a, b):
    '''
    a,b - объекты классса Box или его детей
    функция возвращает True, если объекты соприкасаются
    # можно все менять
    '''
    # TODO: сделать во время работы с движением игрока
    pass


class Wall(Box):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)


class Item_map(Wall):
    def __init__(self, x1, y1, x2, y2):
        super(Wall).__init__(x1, y1, x2, y2)
        # TODO: 1)прикрепить картинку предмета
        #       2)создать координаты центра объекта (для правильного порядка отрисовки)

    def drow(self):
        pass

    def destroy(self):
        # на светлое будущее
        pass

# TODO: создать классы деревьевб камней и т.д. наследуемые от Item_map
