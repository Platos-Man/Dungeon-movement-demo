import pygame
from settings import TILESIZE
from ladder import Ladder


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos, obstacles, current_level, ladders, enemies):
        super().__init__(groups)
        image = pygame.transform.scale2x(pygame.image.load("./graphics/player.png").convert_alpha())
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, -1)
        self.input_flag = True

        self.obstacle_sprites = obstacles
        self.ladder_sprites = ladders
        self.enemy_sprites = enemies

        self.current_level = current_level

    def input(self):
        keys = pygame.key.get_pressed()
        current_pos = self.rect.center
        if self.input_flag:
            self.input_flag = False
            if keys[pygame.K_UP]:
                self.rect.y += self.direction.y * TILESIZE
                self.rect.x += self.direction.x * TILESIZE

            elif keys[pygame.K_DOWN]:
                self.rect.y -= self.direction.y * TILESIZE
                self.rect.x -= self.direction.x * TILESIZE

            elif keys[pygame.K_LEFT] and pygame.KEYDOWN:
                self.direction = self.direction.rotate(-90)
                self.image = pygame.transform.rotate(self.image, 90)

            elif keys[pygame.K_RIGHT] and pygame.KEYDOWN:
                self.direction = self.direction.rotate(90)
                self.image = pygame.transform.rotate(self.image, -90)

        self.check_collisions(current_pos)

        if not True in keys:
            self.input_flag = True

    def check_collisions(self, current_pos):
        for obstacle in self.obstacle_sprites:
            if obstacle.rect.colliderect(self.rect):
                self.rect.center = current_pos

        for ladder in self.ladder_sprites:
            if ladder.rect.colliderect(self.rect):
                if ladder.direction == "up":
                    print("up")
                else:
                    print("down")

    def update(self):
        self.input()
