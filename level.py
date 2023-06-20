import pygame
from tiles import Tile

class Level:

    def __init__(self, map, window):
        self.window = window
        self.map = map
        self.world_shift = 0
        self.tiles = pygame.sprite.Group()
        self.setup_tile_positions()
    
    def setup_tile_positions(self):
        for i, row in enumerate(self.map):
            for j, charItem in enumerate(row):
                if charItem == 'X':
                    x = j * Tile.TILESIZE
                    y = i * Tile.TILESIZE
                    tile = Tile((x, y), Tile.TILESIZE)
                    self.tiles.add(tile)

    def update_and_draw_tiles(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.window)