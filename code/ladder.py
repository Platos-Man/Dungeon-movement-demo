import pygame


class Ladder(pygame.sprite.Sprite):
    def __init__(self, groups, pos, direction):
        super().__init__(groups)
        self.direction = direction
        if self.direction == "up":
            image = pygame.image.load("./graphics/ladder_up.png")
            self.image = pygame.transform.scale2x(image)
        else:
            image = pygame.image.load("./graphics/ladder_down.png")
            self.image = pygame.transform.scale2x(image)
        self.rect = self.image.get_rect(topleft=pos)
