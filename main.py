import pygame
import game
pygame.init()
g = Game()
finished = False
clock = pygame.time.Clock()
FPS = 60
while not finished:
    g.step()
pygame.quit()