import pygame
import rooms


class Unit:
    def __init__(self, i, j, x, y):
        '''
        i,j - положение юнита в массиве комнат
        x,y - координаты в комнате
        '''
        self.i = i
        self.j = j
        self.x = x
        self.y = y

    def