import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 62))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
    
    def check_keys_and_update_direction(self):
        self.check_keys()
        self.update_direction()
        
    def check_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def update_direction(self):
        self.rect.x += self.direction.x * self.speed
        
    def update(self):
        self.check_keys_and_update_direction()
        
        