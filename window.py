import pygame

class Window:

    WIDTH = 1000
    HEIGHT = 700
    COLOR = (48, 48, 48)
    TITLE = 'PLATFORMER'

    def __init__(self):
        self.window = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
        pygame.display.set_caption(Window.TITLE)