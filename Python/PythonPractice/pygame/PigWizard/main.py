import pygame, sys, time
from levels.levels import Level
from settings import *

class Game:
    def __init__(self):

        # General Pygame Setup
        pygame.init()
        pygame.display.set_caption("Epic Pig-Wizard Adventure")
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        # Game Setup
        self.level = Level()
        

    def run(self):
        last_time = time.time()
        while True:
            # delta time 
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # game logic
            self.display_surface.fill(BG_COLOR)
            self.level.update()

            pygame.display.update()
            self.clock.tick(FRAMERATE)

if __name__ == '__main__':
    game = Game()
    game.run()