import pygame
import random
from settings import *

class Floor(pygame.sprite.Sprite):
    def __init__(self, groups, surface):
        super().__init__(groups)
        self.sprite_type = 'floor'
        self.surface = surface

        # drawing the floor
        self.rect = pygame.Rect((0, 700, 800, 100))

    def draw(self):
        self.floor = pygame.draw.rect(self.surface, '#228B22', self.rect)

    def update(self):
        self.draw()

class Coin(pygame.sprite.Sprite):
    def __init__(self, groups, surface):
        super().__init__(groups)
        self.sprite_type = 'coin'
        self.surface = surface
        self.score = 0
        self.random = random.randint(0, 700)
        self.rect = pygame.Rect((self.random, self.random, 30, 30))

    def collison_check(self, player):
        self.is_colliding = pygame.Rect.colliderect(player.rect, self.rect)
        if self.is_colliding:
            if self.rect.y > 0:
                self.rect.bottom = player.rect.top
                self.score += 1
                self.random = random.randint(0, 700)
                self.rect = pygame.Rect((self.random, self.random, 30, 30))

    def draw(self):
        self.coin = pygame.draw.rect(self.surface, 'yellow', self.rect)

    def update(self, player, counter):
        if counter == 0:
            self.rect = pygame.Rect((0, 0, 0, 0))
        else:
            self.collison_check(player)
            self.draw()

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, surface):
        super().__init__(groups)
        self.surface = surface

        # drawing the player
        self.rect = pygame.Rect((30, 30, 60, 60))

        # player physics
        self.gravity = 4

    def apply_gravity(self):
        self.rect.y += self.gravity

    def collison_check(self, floor):
        self.is_colliding = pygame.Rect.colliderect(floor.rect, self.rect)
        if self.is_colliding:
            if self.rect.y > 0:
                self.rect.bottom = floor.rect.top
            if self.rect.y < 0:
                self.rect.top = floor.rect.bottom
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 740:
            self.rect.x = 740


    def draw_player(self):
        self.player = pygame.draw.rect(self.surface, '#696969', self.rect)


    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-2, 0)
        if key[pygame.K_RIGHT]:
            self.rect.move_ip(2, 0)
        if key[pygame.K_UP]:
            self.rect.move_ip(0, -2)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, 2)
        if key[pygame.K_z]:
            self.gravity = -4
        if key[pygame.K_x]:
            self.gravity = 4


    def update(self, floor):
        self.collison_check(floor)
        self.apply_gravity()
        self.draw_player()
        self.handle_keys()
       
    
        