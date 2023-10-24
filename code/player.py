import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        image = pygame.image.load("../graphics/player.png").convert_alpha()
        self.image = pygame.transform.scale2x(image)
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = 0

    def input(self):
        pass
