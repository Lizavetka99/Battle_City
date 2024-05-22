import pygame

ice_row = pygame.image.load("assets/ice.jpg")
ice = pygame.transform.scale(ice_row, (50, 50))

class Ice:
    def __init__(self, pos_x, pos_y):
        self.type = "ice"
        self.x = pos_x
        self.y = pos_y
        self.image = ice