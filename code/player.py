from typing import Any

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        image = pygame.transform.scale2x(
            pygame.image.load("../graphics/player.png").convert_alpha()
        )
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, -1)

    def input(self):
        keys = pygame.key.get_pressed()
        if not True in keys:
            if keys[pygame.K_UP]:
                pass
            elif keys[pygame.K_DOWN]:
                pass

            elif keys[pygame.K_LEFT] and pygame.KEYDOWN:
                self.direction = self.direction.rotate(-90)
                self.image = pygame.transform.rotate(self.image, 90)
                print(keys[pygame.K_LEFT])

            elif keys[pygame.K_RIGHT] and pygame.KEYDOWN:
                self.direction = self.direction.rotate(90)
                self.image = pygame.transform.rotate(self.image, -90)
                print(self.direction)

    def update(self):
        self.input()
