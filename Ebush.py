import pygame
from Fencing import Fencing
ebush_row = pygame.image.load("assets/bush.jpeg")
ebush = pygame.transform.scale(ebush_row, (50, 50))

class Ebush(Fencing):
    def __init__(self, pos_x, pos_y):
        self.image = ebush
        self.x = pos_x
        self.y = pos_y
        self.type = "ebush"
        self.lifes = 1000000000
        self.collider = pygame.rect.Rect(self.x, self.y, 50, 50)
