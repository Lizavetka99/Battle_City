import pygame
from Fencing import Fencing

ice_row = pygame.image.load("assets/ice.jpeg")
ice = pygame.transform.scale(ice_row, (50, 50))

class Ice(Fencing):
    def __init__(self, pos_x, pos_y):
        self.type = "ice"
        self.x = pos_x
        self.y = pos_y
        self.image = ice
        self.lifes = 10000000000
        self.collider = pygame.rect.Rect(self.x, self.y, 50, 50)