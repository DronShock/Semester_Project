import pygame
from game import *
pygame.init()
g = game.Game()
finished = False
clock = pygame.time.Clock()
FPS = 60
while not finished:
    g.step()