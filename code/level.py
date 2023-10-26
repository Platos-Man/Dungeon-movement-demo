import pygame
from floor import Floor
from player import Player
from settings import LEVELS, TILESIZE
from wall import Wall
from ladder import Ladder
from enemy import Enemy


class Level:
    def __init__(self, change_state):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()

        self.enemy_sprites = pygame.sprite.Group()
        self.cleared_enemies = []

        self.ladder_sprites = pygame.sprite.Group()

        self.change_state = change_state

        self.create_map()

    def create_map(self, level=1):
        for row_idx, row in enumerate(LEVELS[level]):
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
                    Floor([self.visible_sprites], pos)
                    if not pos in self.cleared_enemies:
                        Enemy([self.visible_sprites, self.enemy_sprites], pos)
                elif col == "p":
                    Floor([self.visible_sprites], pos)
                    if not self.player_sprite:
                        Player(
                            [self.player_sprite],
                            pos,
                            self.obstacle_sprites,
                            self.ladder_sprites,
                            self.enemy_sprites,
                            self.create_map,
                            self.change_state,
                            self.clear_enemy,
                        )

    def clear_enemy(self, enemy):
        self.cleared_enemies.append(enemy)

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.player_sprite.draw(self.display_surface)
        self.visible_sprites.update()
        self.player_sprite.update()
