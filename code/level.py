import pygame
from floor import Floor
from player import Player
from settings import LEVELS, TILESIZE
from wall import Wall
from ladder import Ladder
from enemy import Enemy


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()

        self.enemy_sprites = pygame.sprite.Group()
        self.ladder_sprites = pygame.sprite.Group()

        self.current_level = 0
        self.create_map()

    def create_map(self):
        for row_idx, row in enumerate(LEVELS[self.current_level]):
            for col_idx, col in enumerate(row):
                pos = (col_idx * TILESIZE, row_idx * TILESIZE)
                if col == "x":
                    Wall([self.visible_sprites, self.obstacle_sprites], pos)
                elif col == " ":
                    Floor([self.visible_sprites], pos)
                elif col == "u":
                    Ladder([self.visible_sprites, self.ladder_sprites], pos, "up")
                elif col == "d":
                    Ladder([self.visible_sprites, self.ladder_sprites], pos, "down")
                elif col == "e":
                    Enemy([self.visible_sprites, self.enemy_sprites], pos)
                elif col == "p":
                    Floor([self.visible_sprites], pos)
                    Player(
                        [self.player_sprite],
                        pos,
                        self.obstacle_sprites,
                        self.current_level,
                        self.ladder_sprites,
                        self.enemy_sprites,
                    )

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.player_sprite.draw(self.display_surface)
        self.visible_sprites.update()
        self.player_sprite.update()
