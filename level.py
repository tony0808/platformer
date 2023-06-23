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
        self.tiles.draw(self.window)
        self.tiles.update(self.world_shift)
        
    def update_player(self):
        self.draw_player() 
        self.handle_player_animation()      
        self.update_player_movement()
        self.update_player_speed_and_shift_world()

    def handle_player_animation(self):
        self.player.sprite.set_movement_status()
        self.player.sprite.animate()

    def update_player_movement(self):
        self.update_player_horizontal_movement()
        self.update_player_vertical_movement()

    def update_player_horizontal_movement(self):
        self.player.sprite.update_horizontal_direction()
        self.player.sprite.update_horizontal_movement()
        self.check_player_horizontal_collisions()
    
    def update_player_vertical_movement(self):
        self.player.sprite.check_for_jump_movement()
        self.player.sprite.apply_gravity()
        self.check_player_vertical_collisions()

    def check_player_horizontal_collisions(self):
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(self.player.sprite.rect):
                if self.player.sprite.direction.x < 0:
                    self.player.sprite.rect.left = sprite.rect.right
                elif self.player.sprite.direction.x > 0:
                    self.player.sprite.rect.right = sprite.rect.left

    def check_player_vertical_collisions(self):
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(self.player.sprite.rect):
                if self.player.sprite.direction.y < 0:
                    self.player.sprite.direction.y = 0
                    self.player.sprite.rect.top = sprite.rect.bottom
                elif self.player.sprite.direction.y > 0:
                    self.player.sprite.direction.y = 0
                    self.player.sprite.rect.bottom = sprite.rect.top

    def draw_player(self):
        self.player.draw(self.window)

    def update_player_speed_and_shift_world(self):
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