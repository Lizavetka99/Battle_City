import pygame

ebush_row = pygame.image.load("assets/bush.jpg")
ebush = pygame.transform.scale(ebush_row, (50, 50))

class Ebush:
    def __init__(self, pos_x, pos_y):
        self.image = ebush
        self.x = pos_x
        self.y = pos_y
        self.type = "ebush"