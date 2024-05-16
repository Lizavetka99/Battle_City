import pygame
import random
import time

MOVEMENT = {
    "Up" : [0, -1],
    "Down" : [0,1],
    "Left" : [-1, 0],
    "Right" : [1, 0]
}
DIRECTION = ["Up", "Down", "Left", "Right"]



enemy_anim = {
    "Up": [pygame.image.load("assets/bot/bot_1_w.png"),
                 pygame.image.load("assets/bot/bot_2_w.png")],
    "Down": [pygame.image.load("assets/bot/bot_1_s.png"),
                 pygame.image.load("assets/bot/bot_2_s.png")],
    "Right": [pygame.image.load("assets/bot/bot_1_d.png"),
                 pygame.image.load("assets/bot/bot_2_d.png")],
    "Left": [pygame.image.load("assets/bot/bot_1_a.png"),
                 pygame.image.load("assets/bot/bot_2_a.png")]
}
for image in enemy_anim.keys():
    for i in range(len(enemy_anim[image])):
        enemy_anim[image][i] = \
            pygame.transform.scale(enemy_anim[image][i], (44, 44))
class Enemy:
    def __init__(self, pos_x, pos_y, speed, map):
        self.pos_x = pos_x
        self.direction = "Down"
        self.pos_y = pos_y
        self.speed = speed
        self.enemy_texture = enemy_anim["Down"][0]
        self.enemy_anim_count = 0
        self.size = 44
        self.map = map
        self.collider = pygame.rect.Rect(self.pos_x, self.pos_y, 40, 40)


    def move(self):

        self.enemy_texture = enemy_anim[self.direction][
            self.enemy_anim_count]
        if self.can_move():
            self.pos_x += MOVEMENT[self.direction][0]
            self.pos_y += MOVEMENT[self.direction][1]
        else:
            self.direction = DIRECTION[random.randint(0, 3)]

        self.enemy_anim_count = (self.enemy_anim_count + 1) % 2

    def can_move(self):
        dx, dy = MOVEMENT[self.direction]
        self.collider = pygame.rect.Rect(self.pos_x + dx, self.pos_y + dy, 40, 40)
        for brick in self.map.obj_list:
            if self.collider.colliderect(brick.collider):
                return False
        for player in self.map.players:
            if player == self: continue
            if self.collider.colliderect(player.collider):
                return False
        return True
    def destroy(self):
        self.__init__(50 * 8, 50 * 2, 1, self.map)