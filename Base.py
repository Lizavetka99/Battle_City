import pygame
from Brick import Brick

class Base(Brick):
    size = 50
    def __init__(self, pos_x, pos_y, player, image):
        self.x = pos_x
        self.y = pos_y
        self.type = "base"
        self.collider = pygame.rect.Rect(self.x, self.y, 100, 100)
        self.player = player
        self.image = image
