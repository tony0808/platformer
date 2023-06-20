import pygame
from tiles import Tile
from player import Player
from window import Window

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
        self.update_tiles()
        self.update_player()

    def update_tiles(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.window)
        
    def update_player(self):
        self.player.update()
        self.player.draw(self.window)
        self.update_player_movement()
    
    def update_player_movement(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 100 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > Window.WIDTH - 100 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8