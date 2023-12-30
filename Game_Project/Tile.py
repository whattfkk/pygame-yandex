import pygame
import os

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, text):
        super().__init__(groups)

        if text == "x":
            self.image = pygame.image.load("images/back_ground/Rock.png").convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        elif text == "p":
            for filename in os.scandir("images/ggshka"):
                if filename.is_file():
                    print(filename.path)
                    self.image = pygame.image.load(filename.path).convert_alpha()
                    self.image = pygame.transform.scale(self.image, (100, 110))
                    self.rect = self.image.get_rect(topleft=pos)