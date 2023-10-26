import pygame
from settings import TILESIZE
from ladder import Ladder


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos, obstacles, ladders, enemies, create_map, change_state, clear_enemy):
        super().__init__(groups)
        image = pygame.transform.scale2x(pygame.image.load("./graphics/player.png").convert_alpha())
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, -1)
        self.input_flag = True

        self.obstacle_sprites = obstacles
        self.ladder_sprites = ladders
        self.enemy_sprites = enemies

        self.current_level = 1

        # Level methods
        self.create_map = create_map
        self.change_state = change_state
        self.clear_enemy = clear_enemy

    def input(self):
        keys = pygame.key.get_pressed()
        current_pos = self.rect.center
        if self.input_flag:
            self.input_flag = False
            if keys[pygame.K_UP]:
                self.rect.y += self.direction.y * TILESIZE
                self.rect.x += self.direction.x * TILESIZE
                self.check_obstacle_collisions(current_pos)
                self.check_enemy_collisions()

            elif keys[pygame.K_DOWN]:
                self.rect.y -= self.direction.y * TILESIZE
                self.rect.x -= self.direction.x * TILESIZE
                self.check_obstacle_collisions(current_pos)
                self.check_enemy_collisions()

            elif keys[pygame.K_LEFT]:
                self.direction = self.direction.rotate(-90)
                self.image = pygame.transform.rotate(self.image, 90)

            elif keys[pygame.K_RIGHT]:
                self.direction = self.direction.rotate(90)
                self.image = pygame.transform.rotate(self.image, -90)

            elif keys[pygame.K_e]:
                self.check_ladder_collisions()

        if not True in keys:
            self.input_flag = True

    def check_obstacle_collisions(self, current_pos):
        for obstacle in self.obstacle_sprites:
            if obstacle.rect.colliderect(self.rect):
                self.rect.center = current_pos

    def check_ladder_collisions(self):
        for ladder in self.ladder_sprites:
            if ladder.rect.colliderect(self.rect):
                self.obstacle_sprites.empty()
                self.ladder_sprites.empty()
                self.enemy_sprites.empty()
                if ladder.direction == "up":
                    self.current_level += 1
                    self.create_map(self.current_level)
                else:
                    self.current_level += -1
                    self.create_map(self.current_level)

    def check_enemy_collisions(self):
        for enemy in self.enemy_sprites:
            if enemy.rect.colliderect(self.rect):
                self.clear_enemy((enemy.rect.x, enemy.rect.y))
                enemy.kill()
                self.change_state("battle")

    def update(self):
        self.input()
