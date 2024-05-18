import pygame
import Screen

MOVEMENT = {
    "Up" : [0, -2],
    "Down" : [0, 2],
    "Left" : [-2, 0],
    "Right" : [2, 0]
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
        self.speed = 5
        self.player = player
        self.is_shooted = False
        self.isCollision = False
        self.collider = pygame.rect.Rect(self.X, self.Y, 16, 16)


    def setPosition(self):
        self.CORRECT_SDVIG = {
            "Up": [self.player.pos_x + (self.player.size / 2) - 8, self.player.pos_y + 32],
            "Down": [self.player.pos_x + (self.player.size / 2) - 8, self.player.pos_y + self.player.size-32],
            "Left": [self.player.pos_x + 16, self.player.pos_y + (self.player.size / 2) - 8],
            "Right": [self.player.pos_x + self.player.size - 32, self.player.pos_y + (self.player.size / 2) - 8],
        }
        self.direction = self.player.direction
        self.X, self.Y = (self.CORRECT_SDVIG[self.direction][0], self.CORRECT_SDVIG[self.direction][1])
        self.is_shooted = True
        self.texture = pygame.image.load(textures[self.direction])
        self.texture = pygame.transform.scale(self.texture, (16, 16))
        self.collider = pygame.rect.Rect(self.X, self.Y, 16, 16)

    def Move(self):
        self.collider = pygame.rect.Rect(self.X, self.Y, 16, 16)
        self.X += MOVEMENT[self.direction][0]
        self.Y += MOVEMENT[self.direction][1]

        for fencing in self.map.obj_list:
            if self.collider.colliderect(fencing.collider):
                self.map.del_fencing(fencing)
                self.isCollision = True
                self.Freeze_bullet()
        for player in self.map.players:
            if player == self.player: continue
            if self.collider.colliderect(player.collider):
                self.map.del_player(player, self)
                self.isCollision = True
        for bullet in self.map.bullets:
            if bullet == self: continue
            if self.collider.colliderect(bullet.collider):
                self.isCollision = True
                bullet.isCollision = True


        if self.X > Screen.WIDTH or self.X < -100 or self.Y > Screen.HEIGHT or self.Y < -100:
            self.is_shooted = False

    def Freeze_bullet(self):
        self.X, self.Y = -1000, -1000
        self.isCollision = False