import pygame
from tiles import Tile
from map import Map

class Window:

    WIDTH = 1000
    HEIGHT = len(Map.map_0) * Tile.TILESIZE
    COLOR = (48, 48, 48)
    TITLE = 'PLATFORMER'

    def __init__(self):
        self.window = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
        pygame.display.set_caption(Window.TITLE)