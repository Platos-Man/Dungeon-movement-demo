import pygame
from pygame.sprite import _Group


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(*groups)
        self.image = pygame.image.load("../graphics/player.png")
        self.rect = self.image.get_rect(topleft=pos)
