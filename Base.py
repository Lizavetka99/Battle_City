import pygame
from Brick import Brick

class Base(Brick):
    size = 50
    def __init__(self, pos_x, pos_y, player, image):
        self.fencing = (pos_x, pos_y)
        self.collider = pygame.rect.Rect(self.fencing[0], self.fencing[1], 100, 100)
        self.player = player
        self.image = image

    def destroy(self):
        del self