import pygame, sys, time
from settings import *
from sprites import BG, Ground, Plane, Obsicals

class Game:
    def __init__(self):
        # game setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Plane')
        self.clock = pygame.time.Clock()
        self.active = True

        #sprite groups
        self.all_sprite = pygame.sprite.Group()
        self.collsion_sprite = pygame.sprite.Group()

        # scale vector
        bg_height = pygame.image.load("./graphics/enviorment/background.png").get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height
        # prite setup
        BG(self.all_sprite, self.scale_factor)
        Ground([self.all_sprite, self.collsion_sprite], self.scale_factor)
        self.plane = Plane(self.all_sprite, self.scale_factor / 1.7)

        # timer 
        self.obsicals_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obsicals_timer, 1400)

        # text
        self.font = pygame.font.Font('./graphics/fonts/BD_Cartoon_Shout.ttf', 30)
        self.score = 0
        self.start_offset = 0

        # menu
        self.menu_surface = pygame.image.load('./graphics/ui/menu.png').convert_alpha()
        self.menu_rect = self.menu_surface.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # music
        self.bg_music = pygame.mixer.Sound('./sound/sounds_music.wav')
        self.bg_music.set_volume(0.3)
        self.bg_music.play(loops = -1)

    def collision_check(self):
        if pygame.sprite.spritecollide(self.plane, self.collsion_sprite, False, pygame.sprite.collide_mask) or self.plane.rect.top <=0:
            for sprite in self.collsion_sprite.sprites():
                if sprite.sprite_type == 'obstical':
                 sprite.kill()
            self.active = False
            self.plane.kill()

    def display_score(self):
        if self.active:
            self.score = (pygame.time.get_ticks() - self.start_offset) // 1000
            y =  WINDOW_HEIGHT / 10
        else:
            y = WINDOW_HEIGHT /2 + (self.menu_rect.height / 1.5)
        
        score_surface = self.font.render(str(self.score), True, 'black')
        score_rect = score_surface.get_rect(midtop = (WINDOW_WIDTH / 2,y))
        self.display_surface.blit(score_surface, score_rect)

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.active:
                        self.plane.jump()
                    else:
                        self.plane = Plane(self.all_sprite, self.scale_factor / 1.7)
                        self.active = True
                        self.start_offset = pygame.time.get_ticks()


                if event.type == self.obsicals_timer and self.active:
                    Obsicals([self.all_sprite, self.collsion_sprite], self.scale_factor * 1.1)

            # game logic
            self.all_sprite.update(dt)
            self.all_sprite.draw(self.display_surface)
            self.display_score()

            if self.active:
                self.collision_check()
            else:
                self.display_surface.blit(self.menu_surface, self.menu_rect)

            pygame.display.update()
            self.clock.tick(FRAMRATE)

if __name__ == '__main__':
    game = Game()
    game.run()