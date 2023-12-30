import pygame


class player(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.walk_right = ["images/Texas/Texas_go_right/right_go_0.png", "images/Texas/Texas_go_right/right_go_1.png",
                           "images/Texas/Texas_go_right/right_go_2.png", "images/Texas/Texas_go_right/right_go_3.png",
                           "images/Texas/Texas_go_right/right_go_4.png", "images/Texas/Texas_go_right/right_go_5.png",
                           "images/Texas/Texas_go_right/right_go_6.png", "images/Texas/Texas_go_right/right_go_7.png",
                           "images/Texas/Texas_go_right/right_go_8.png", "images/Texas/Texas_go_right/right_go_9.png",
                           "images/Texas/Texas_go_right/right_go_10.png", "images/Texas/Texas_go_right/right_go_11.png"]
        self.walk_left = ["images/Texas/Texas_go_left/left_go_0.png", "images/Texas/Texas_go_left/left_go_1.png",
                          "images/Texas/Texas_go_left/left_go_2.png", "images/Texas/Texas_go_left/left_go_3.png",
                          "images/Texas/Texas_go_left/left_go_4.png", "images/Texas/Texas_go_left/left_go_5.png",
                          "images/Texas/Texas_go_left/left_go_6.png", "images/Texas/Texas_go_left/left_go_7.png",
                          "images/Texas/Texas_go_left/left_go_8.png", "images/Texas/Texas_go_left/left_go_9.png",
                          "images/Texas/Texas_go_left/left_go_10.png", "images/Texas/Texas_go_left/left_go_11.png"]
        self.atack_right = ["images/Texas/Texas_hit_right/Texas_hit_1.png",
                            "images/Texas/Texas_hit_right/Texas_hit_2.png",
                            "images/Texas/Texas_hit_right/Texas_hit_3.png",
                            "images/Texas/Texas_hit_right/Texas_hit_4.png",
                            "images/Texas/Texas_hit_right/Texas_hit_5.png"]
        self.atack_left = ["images/Texas/Texas_hit_left/Texas_hit_1.png",
                           "images/Texas/Texas_hit_left/Texas_hit_2.png",
                           "images/Texas/Texas_hit_left/Texas_hit_2.png",
                           "images/Texas/Texas_hit_left/Texas_hit_4.png",
                           "images/Texas/Texas_hit_left/Texas_hit_5.png", ]
        self.atack = 0
        self.walk = 0
        self.image = pygame.image.load(self.walk_right[self.walk]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 5
        self.check_x = 1

    def input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.atack = 0
            self.rect.y -= 5
            self.walk += 1
        elif key[pygame.K_DOWN]:
            self.atack = 0
            self.rect.y += 5
            self.walk += 1

        elif key[pygame.K_RIGHT]:
            self.atack = 0
            self.rect.x += 5
            self.check_x = 1
            self.walk += 1
        elif key[pygame.K_LEFT]:
            self.atack = 0
            self.rect.x -= 5
            self.check_x = -1
            self.walk += 1

        elif key[pygame.K_SPACE]:
            if self.check_x == -1:
                self.check_x = -2
            elif self.check_x == 1:
                self.check_x = 2

    def update(self):
        self.input()
        if self.check_x == 1:
            self.image = pygame.image.load(self.walk_right[self.walk]).convert_alpha()
        elif self.check_x == -1:
            self.image = pygame.image.load(self.walk_left[self.walk]).convert_alpha()
        elif self.check_x == 2:
            if self.atack == 1:
                print(self.rect.x)
                self.rect.x -= 16
                print(self.rect.x)
            elif self.atack == 3:
                self.rect.y += 1
            self.image = pygame.image.load(self.atack_right[self.atack]).convert_alpha()
            self.atack += 1
        elif self.check_x == -2:
            if self.atack == 3:
                self.rect.y += 1
            elif self.atack == 4:
                self.rect.x -= 10
            self.image = pygame.image.load(self.atack_left[self.atack]).convert_alpha()
            self.atack += 1



        if self.walk == 11:
            self.walk = 0
        if self.atack == 5:
            self.atack = 0
            self.walk = 0
            if self.check_x < 0:
                self.check_x = -1
                self.rect.x += 10
                self.rect.y -= 1
            else:
                self.rect.x += 16
                print(self.rect.x)
                self.rect.y -= 1
                self.check_x = 1

# import pygame
#
# class Player:
#     def __init__(self, pos):
#         self.image = pygame.image.load("images/Link_down/Link_down_2.png").convert_alpha()
#         self.rect = self.image.get_rect(topleft=pos)
#
#         self.direction = pygame.math.Vector2()
#
#     def input(self):
#         key = pygame.key.get_pressed()
#
#         if key[pygame.K_UP]:
#             self.direction.y -= 1
#         elif key[pygame.K_DOWN]:
#             self.direction.y += 1
#
#         if key[pygame.K_RIGHT]:
#             self.direction.x += 1
#         elif key[pygame.K_LEFT]:
#             self.direction.x -= 1
#
#     def updae(self):
#         self.input()
