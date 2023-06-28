import pygame
from code.tiles import Tile
from code.player import Player
from settings import *

class Level:
    # level setup
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.visable_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.level_setup()

    def level_setup(self):
        for row_index, row in enumerate(LEVEL1_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if col == 'X':
                    Tile((x, y), [self.visable_sprites, self.collision_sprites])
                if col == 'P':
                    self.player = Player((x, y), [self.visable_sprites], self.collision_sprites)

    def update(self):
        self.visable_sprites.draw(self.display_surface)
        self.visable_sprites.update()

