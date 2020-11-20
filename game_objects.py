"""Классы игровых объектов"""
# import pygame as pg
#from body import *

characters = []
FPS = 40

class player():
    def __init__(self, x, y, speed, image):
        self.width = 50
        self.height = 50
        self.x = 0
        self.y = 0
        self.speed = speed
        self.image = None



    def create_image(self, place):
        self.img = pg.Surface((self.width, self.height))
        self.img.fill((255,255,255))
        characters.append(self.img)


    def go_to(self, x, y):
        '''
        функция должна заставлять идти объект к точке (x,y)
        желательно еще связать это со скоростью
        функция будет использоваться восновном для MPC
        '''
        x += ((self.x - x) * self.speed) / (((y - self.y) ** 2 + (x - self.x) ** 2) ** 0.5 * FPS)
        y += ((self.y - y) * self.speed) / (((y - self.y) ** 2 + (x - self.x) ** 2) ** 0.5 * FPS)

    def go_button(self, button):
        '''
        функция перемещения для игрока
        w,a,s,d -- булевские переменные соответствующие нажатию на такие же кнопки
        true -- кнопка
        не забыть про одновременное нажатие на кнопок и постоянную скорость
        '''
        if button == "w":
            self.y += self.speed / FPS
        if button == "a":
            self.x -= self.speed / FPS
        if button == "s":
            self.y -= self.speed / FPS
        if button == "d":
            self.x += self.speed / FPS

        if button == "wd":
            self.y += self.speed * 0.71 / FPS
            self.x += self.speed * 0.71 / FPS
        if button == "wa":
            self.y += self.speed * 0.71 / FPS
            self.x -= self.speed * 0.71 / FPS
        if button == "sa":
            self.y -= self.speed * 0.71 / FPS
            self.x -= self.speed * 0.71 / FPS
        if button == "sd":
            self.y -= self.speed * 0.71 / FPS
            self.x += self.speed * 0.71 / FPS

characters.append(player)

# class NPC(player):
#     def __init__(self):
#         self.peaceful = True

# class player():
#     def change_item(self):
#         '''
#         функция меняет предмет в руке
#         '''
#
#     def change_armor(self):
#         '''
#         функция меняет броню
#         '''
