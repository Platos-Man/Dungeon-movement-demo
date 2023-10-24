import pygame
from floor import Floor
from player import Player
from settings import MAP, TILESIZE
from wall import Wall


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_idx, row in enumerate(MAP):
            for col_idx, col in enumerate(row):
                x = col_idx * TILESIZE
                y = row_idx * TILESIZE
                if col == "x":
                    Wall([self.visible_sprites, self.obstacle_sprites], (x, y))
                elif col == " ":
                    Floor([self.visible_sprites], (x, y))
                elif col == "p":
                    Floor([self.visible_sprites], (x, y))
                    Player([self.visible_sprites], (x, y))

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
