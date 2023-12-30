import pygame
import sys
from Player import player


class main:
    def __init__(self):
        pygame.init()
        size = 600, 600
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        player(self.all_sprites)

    def run(self):
        while True:
            self.screen.fill((0, 110, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.all_sprites.draw(self.screen)
            self.all_sprites.update()
            pygame.display.flip()
            self.clock.tick(20)


if __name__ == '__main__':
    main().run()
