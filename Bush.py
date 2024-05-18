import pygame

bush_row = pygame.image.load("assets/bush.jpg")
bush = pygame.transform.scale(bush_row, (50, 50))

class Bush:
    def __init__(self, pos_x, pos_y):
        self.image = bush
        self.x = pos_x
        self.y = pos_y
        self.type = "bush"