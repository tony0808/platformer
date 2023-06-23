from os import walk
import pygame

def get_list_of_image_surfaces_from_folder(dir_path):
    image_surfaces = []
    for _, __, files in walk(dir_path):
        for relative_file_name in files:
            full_file_name = dir_path + '/' + relative_file_name
            image_surface = pygame.image.load(full_file_name).convert_alpha()
            image_surfaces.append(image_surface)
    return image_surfaces
