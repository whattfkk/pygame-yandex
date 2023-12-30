import pygame
from Settings import *
from Tile import Tile

class Back_ground:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(world_map):
            for col_index, col in enumerate(row):
                x = col_index * 100
                y = row_index * 100

                if col == "x":
                    Tile((x, y), [self.visible_sprites], "x")
                elif col == "p":
                    Tile((x, y), [self.visible_sprites], "p")

    def run(self):
        self.visible_sprites.draw(self.display_surface)