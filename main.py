import pygame
import game
pygame.init()
g = Game()
finished = False
clock = pygame.time.Clock()
while not finished:
    g.step()
pygame.quit()