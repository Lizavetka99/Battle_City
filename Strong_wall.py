import pygame
from Fencing import Fencing

strong_wall_row = pygame.image.load("assets/Images/MapTiles/K.png")
strong_wall = pygame.transform.scale(strong_wall_row, (50, 50))
class Strong_wall(Fencing):
    size = 50
    def __init__(self,  pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.type = "strong_wall"
        self.image = strong_wall
        self.collider = pygame.rect.Rect(self.x, self.y, 50, 50)

