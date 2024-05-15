import pygame
from Fencing import Fencing

brick_wall_row = pygame.image.load("assets/brick_wall.png")
brick_wall = pygame.transform.scale(brick_wall_row, (50, 50))
class Brick(Fencing):
    def __init__(self,  pos_x, pos_y):
        self.fencing = (pos_x, pos_y)
        self.image = brick_wall

    def destroy(self):
        del self

