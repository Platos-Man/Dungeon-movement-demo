import pygame
from settings import MAP


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

    def create_map(self):
        for row in MAP:
            print(row)
            for col in row:
                pass

    def run(self):
        self.create_map()
