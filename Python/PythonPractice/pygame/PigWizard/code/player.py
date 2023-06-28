import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft = pos)

        # player movement 
        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.gravity = 0.2
        self.jump_speed = 9
        self.collision_sprites = collision_sprites
        self.is_on_floor = False

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_z]:
            print("PIGWIZARD FIRE BALL ATTACK!")

        if keys[pygame.K_SPACE] and self.is_on_floor: # and self.is_on_floor
            self.direction.y = -self.jump_speed



    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0: 
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0: 
                    self.rect.right = sprite.rect.left

    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.is_on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
                    
        if self.is_on_floor and self.direction.y != 0:
            self.is_on_floor = False


    def add_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.player_input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.add_gravity()
        self.vertical_collisions()
