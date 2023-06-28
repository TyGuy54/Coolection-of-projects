import pygame, sys, time
from objects import Player, Floor, Coin
from settings import *

class Game:
    def __init__(self):

        # pygame setup
        pygame.init()
        pygame.display.set_caption('Collect Them COINS!!!!')
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()


        self.counter, self.text = 20, '20'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.SysFont('Consolas', 30)

        #sprite groups
        self.all_sprite = pygame.sprite.Group()
        self.collsion_sprite = pygame.sprite.Group()

        self.coin = Coin(self.all_sprite, self.display_surface)
        self.floors = Floor(self.all_sprite, self.display_surface)
        self.player = Player(self.all_sprite, self.display_surface)

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
                if event.type == pygame.USEREVENT:
                    self.counter -= 1
                    self.text = str(self.counter).rjust(3) if self.counter > 0 else f'High Scoure: {self.coin.score}'
                           
            # game logic
            self.display_surface.blit(self.font.render(self.text, True, (0, 0, 0)), (32, 48))
            self.player.update(self.floors)
            self.floors.update()
            self.coin.update(self.player, self.counter)

            pygame.display.update()
            self.display_surface.fill('#87CEFA')
            self.clock.tick(FRAMERATE)

if __name__ == '__main__':
    game = Game()
    game.run()

