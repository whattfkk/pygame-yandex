import pygame
import sys
from random import randrange
import os


class main:
    def __init__(self):
        pygame.init()
        size = 500, 500
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.walk_right = ["Texas/right_go_0.png", "Texas/right_go_1.png", "Texas/right_go_2.png", "Texas/right_go_3.png", "Texas/right_go_4.png", "Texas/right_go_5.png", "Texas/right_go_6.png", "Texas/right_go_7.png", "Texas/right_go_8.png", "Texas/right_go_9.png", "Texas/right_go_10.png", "Texas/right_go_11.png"]
        self.walk = 0
        self.hit_anim = ["Texas_hit/Texas_hit_1.png", "Texas_hit/Texas_hit_2.png", "Texas_hit/Texas_hit_3.png", "Texas_hit/Texas_hit_4.png", "Texas_hit/Texas_hit_5.png"]
        self.hit = 0
        self.slime_anim = ["images/Slime/slime_go_1.png", "images/Slime/slime_go_2.png", "images/Slime/slime_go_3.png", "images/Slime/slime_go_4.png","images/Slime/slime_go_5.png", "images/Slime/slime_go_6.png"]
        self.slime_go = 0
        self.flower = ["images/flower/flower_go_1.png", "images/flower/flower_go_2.png", "images/flower/flower_go_3.png", "images/flower/flower_go_4.png"]
        self.flower_go = 0

    def run(self):
        while True:
            self.screen.fill((0, 125, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(pygame.image.load(self.walk_right[self.walk]).convert_alpha(), (50, 250))
            if self.walk < 11:
                self.walk += 1
            else:
                self.walk = 0


            if self.hit == 0:
                self.screen.blit(
                    pygame.image.load(self.hit_anim[self.hit]).convert_alpha(),
                    (50, 200))
            elif self.hit < 3:
                self.screen.blit(
                    pygame.image.load(self.hit_anim[self.hit]).convert_alpha(),
                    (34, 200))
            elif self.hit == 3:
                self.screen.blit(
                    pygame.image.load(self.hit_anim[self.hit]).convert_alpha(),
                    (34, 201))
            else:
                self.screen.blit(
                    pygame.image.load(self.hit_anim[self.hit]).convert_alpha(),
                    (39, 201))
            if self.hit < 4:
                self.hit += 1
            else:
                self.hit = 0



            if self.slime_go == 0:
                self.screen.blit(
                    pygame.image.load(self.slime_anim[self.slime_go]).convert_alpha(),
                    (50, 150))
            elif self.slime_go == 1 or self.slime_go == 5:
                self.screen.blit(
                    pygame.image.load(self.slime_anim[self.slime_go]).convert_alpha(),
                    (50, 152))
            elif self.slime_go == 2 or self.slime_go == 4:
                self.screen.blit(
                    pygame.image.load(self.slime_anim[self.slime_go]).convert_alpha(),
                    (50, 112))
            elif self.slime_go == 3:
                self.screen.blit(
                    pygame.image.load(self.slime_anim[self.slime_go]).convert_alpha(),
                    (49, 102))
            if self.slime_go == 5:
                self.slime_go = 0
            else:
                self.slime_go += 1



            self.screen.blit(pygame.image.load(self.flower[self.flower_go]).convert_alpha(), (50, 100))
            self.flower_go += 1
            if self.flower_go == 4:
                self.flower_go = 0

            pygame.display.flip()
            self.clock.tick(10)


if __name__ == '__main__':
    main().run()