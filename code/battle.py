import pygame


class Battle:
    def __init__(self, change_state) -> None:
        self.display_surface = pygame.display.get_surface()
        self.change_state = change_state

    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.change_state("dungeon")
