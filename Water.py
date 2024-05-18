import pygame

water_row = pygame.image.load("assets/water.jpg")
water = pygame.transform.scale(water_row, (50, 50))

class Water:
    def __init__(self, pos_x, pos_y):
        self.type = "water"
        self.x = pos_x
        self.y = pos_y