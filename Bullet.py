import pygame
import Screen


CORRECT_SDVIG = {
    "Up" : [35, -30],
    "Down" : [35, 70],
    "Left" : [-30, 35],
    "Right" : [100, 35],
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
    def __init__(self, player, map):
        self.X, self.Y = 0, 0
        self.map = map
        self.player = player
        self.is_shooted = False

    def setPosition(self):
        self.direction = self.player.direction
        self.X, self.Y = (self.player.pos_x + CORRECT_SDVIG[self.direction][0], self.player.pos_y + CORRECT_SDVIG[self.direction][1])
        self.is_shooted = True
        self.texture = pygame.image.load(textures[self.direction])
        self.texture = pygame.transform.scale(self.texture, (32, 32))
        self.collider = pygame.rect.Rect(self.X, self.Y, 32, 32)

    def Move(self):
        self.collider = pygame.rect.Rect(self.X, self.Y, 32, 32)
        self.X += MOVEMENT[self.direction][0]
        self.Y += MOVEMENT[self.direction][1]

        for brick in self.map.obj_list:
            if self.collider.colliderect(pygame.rect.Rect(brick.fencing[0], brick.fencing[1], 100, 100)):
                self.map.del_brick(brick)

        if self.X > Screen.WIDTH or self.X < -300 or self.Y > Screen.HEIGHT or self.Y < -300:
            self.is_shooted = False

