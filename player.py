import pygame
from utils import get_list_of_image_surfaces_from_folder

class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.import_player_images()

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.movement_status = 'idle'
        self.facing_right = True
        
    def import_player_images(self):
        self.images_path = './images/player/'
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}
        for animation in self.animations.keys():
            animation_folder_path = self.images_path + animation
            self.animations[animation] = get_list_of_image_surfaces_from_folder(animation_folder_path)

    def update_horizontal_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
    
    def update_horizontal_movement(self):
        self.rect.x += self.direction.x * self.speed
        
    def check_for_jump_movement(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
    
    def animate(self):
        self.update_frame()
        self.flip_frame()
    
    def update_frame(self):
        animation = self.animations[self.movement_status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]

    def flip_frame(self):
        animation = self.animations[self.movement_status]
        current_animation = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = current_animation
        else:
            flipped_animation = pygame.transform.flip(current_animation, True, False)
            self.image = flipped_animation

    def set_movement_status(self):
        if self.direction.y < 0:
            self.movement_status = 'jump'
        elif self.direction.y > self.gravity + 0.1:
            self.movement_status = 'fall'
        else:
            if self.direction.x == 0:
                self.movement_status = 'idle'
            else:
                self.movement_status = 'run'