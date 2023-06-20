import pygame
from tiles import Tile
from player import Player

class Level:

    def __init__(self, map, window):
        self.window = window
        self.map = map
        self.world_shift = 0
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.setup_tile_positions_and_player()
    
    def setup_tile_positions_and_player(self):
        for i, row in enumerate(self.map):
            for j, charItem in enumerate(row):
                pos = (j * Tile.TILESIZE, i * Tile.TILESIZE)
                if charItem == 'X':
                    self.setup_tile_positions(pos)
                if charItem == 'P':
                    self.setup_player(pos)

    def setup_tile_positions(self, pos):
        tile = Tile(pos, Tile.TILESIZE)
        self.tiles.add(tile)
    
    def setup_player(self, pos):
        player = Player(pos)
        self.player.add(player) 

    def draw(self):
        self.update_and_draw_tiles()
        self.update_and_draw_player()

    def update_and_draw_tiles(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.window)
        
    def update_and_draw_player(self):
        self.player.update()
        self.player.draw(self.window)