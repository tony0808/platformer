import pygame
from window import Window
from level import Level
from map import Map

class Platformer:

    def __init__(self):
        self.window = Window()
        self.level = Level(Map.map_0, self.window.window)
        self.running = True
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def start(self):
        pygame.init()
        self.run_game_loop()
        pygame.quit()

    def run_game_loop(self):
        while self.running:
            self.handle_events()
            self.update_and_draw_window()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update_and_draw_window(self):
        self.draw_window()
        self.update_window()

    def update_window(self):
        pygame.display.update()
        self.clock.tick(self.FPS)
    
    def draw_window(self):
        self.fill_window_color()
        self.draw_level()
    
    def fill_window_color(self):
        self.window.window.fill(self.window.COLOR)

    def draw_level(self):
        self.level.draw()