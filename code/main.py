import sys

import pygame
from level import Level
from settings import FPS, HEIGTH, WIDTH
from battle import Battle


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

        self.state = "dungeon"

        self.battle = Battle(self.change_state)
        self.level = Level(self.change_state)

    def change_state(self, state):
        self.state = state

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.state == "dungeon":
                self.screen.fill("black")
                self.level.run()
            else:
                self.screen.fill("grey")
                self.battle.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
