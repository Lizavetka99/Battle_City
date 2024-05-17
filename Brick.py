import pygame
from Fencing import Fencing

brick_wall_row = pygame.image.load("assets/brick_wall_3.png")
brick_wall = pygame.transform.scale(brick_wall_row, (50, 50))
class Brick(Fencing):
    size = 50
    def __init__(self,  pos_x, pos_y):
        self.x = pos_x
        self.lifes = 3
        self.y = pos_y
        self.type = "brick"
        self.image = brick_wall
        self.collider = pygame.rect.Rect(self.x, self.y, 50, 50)

