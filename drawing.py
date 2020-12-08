import pygame
import settings
def draw_main_menu(screen):
    main_menu_pict = pygame.image.load('main_menu1.png')
    screen.blit(main_menu_pict, (0, 0))
    pygame.display.update()