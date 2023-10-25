import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        image = pygame.image.load("./graphics/wall.png")
        self.image = pygame.transform.scale2x(image)
        self.rect = self.image.get_rect(topleft=pos)
