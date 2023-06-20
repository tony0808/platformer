import pygame

class Tile(pygame.sprite.Sprite):
    
    TILESIZE = 64
    
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((97, 156, 250))
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shift):
        self.rect.x += x_shift