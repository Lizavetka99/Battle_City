import pygame


CORRECT_SDVIG = {
    "Up" : [-78, -150],
    "Down" : [-78, 0],
    "Left" : [-150, -80],
    "Right" : [0, -80],
}

MOVEMENT = {
    "Up" : [0, -1],
    "Down" : [0, 1],
    "Left" : [-1, 0],
    "Right" : [1, 0]
}

textures = {
    "Up" : "assets/bullets/bullet_up.png",
    "Down" : "assets/bullets/bullet_down.png",
    "Left" : "assets/bullets/bullet_left.png",
    "Right" : "assets/bullets/bullet_right.png",
}

class Bullet:
    def __init__(self, player):
        self.X, self.Y = 0, 0
        self.player = player
        self.is_shooted = False

    def setPosition(self):
        self.direction = self.player.direction
        self.X, self.Y = (self.player.pos_x + CORRECT_SDVIG[self.direction][0], self.player.pos_y + CORRECT_SDVIG[self.direction][1])
        self.is_shooted = True
        self.texture = pygame.image.load(textures[self.direction])
    def Move(self):
        self.X += MOVEMENT[self.direction][0]
        self.Y += MOVEMENT[self.direction][1]

