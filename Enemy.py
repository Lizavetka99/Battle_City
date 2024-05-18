import pygame
import random

MOVEMENT = {
    "Up" : [0, -0.5],
    "Down" : [0,0.5],
    "Left" : [-0.5, 0],
    "Right" : [0.5, 0]
}
DIRECTION = ["Up", "Down", "Left", "Right"]



enemy_anim = {
    "Up": [pygame.image.load("assets/enemy/bot/bot_1_w.png"),
                 pygame.image.load("assets/enemy/bot/bot_2_w.png")],
    "Down": [pygame.image.load("assets/enemy/bot/bot_1_s.png"),
                 pygame.image.load("assets/enemy/bot/bot_2_s.png")],
    "Right": [pygame.image.load("assets/enemy/bot/bot_1_d.png"),
                 pygame.image.load("assets/enemy/bot/bot_2_d.png")],
    "Left": [pygame.image.load("assets/enemy/bot/bot_1_a.png"),
                 pygame.image.load("assets/enemy/bot/bot_2_a.png")]
}

enemy_anim_speed = {
    "Up": [pygame.image.load("assets/enemy/fast/fast_enemy_1_w.png"),
                 pygame.image.load("assets/enemy/fast/fast_enemy_2_w.png")],
    "Down": [pygame.image.load("assets/enemy/fast/fast_enemy_1_s.png"),
                 pygame.image.load("assets/enemy/fast/fast_enemy_2_s.png")],
    "Right": [pygame.image.load("assets/enemy/fast/fast_enemy_1_d.png"),
                 pygame.image.load("assets/enemy/fast/fast_enemy_2_d.png")],
    "Left": [pygame.image.load("assets/enemy/fast/fast_enemy_1_a.png"),
                 pygame.image.load("assets/enemy/fast/fast_enemy_2_a.png")]
}

enemy_anim_armor = {
    "Up": [pygame.image.load("assets/enemy/armor/armored_enemy_1_w.png"),
                 pygame.image.load("assets/enemy/armor/armored_enemy_2_w.png")],
    "Down": [pygame.image.load("assets/enemy/armor/armored_enemy_1_s.png"),
                 pygame.image.load("assets/enemy/armor/armored_enemy_2_s.png")],
    "Right": [pygame.image.load("assets/enemy/armor/armored_enemy_1_d.png"),
                 pygame.image.load("assets/enemy/armor/armored_enemy_2_d.png")],
    "Left": [pygame.image.load("assets/enemy/armor/armored_enemy_1_a.png"),
                 pygame.image.load("assets/enemy/armor/armored_enemy_2_a.png")]
}
enemy_anim_attack = {
    "Up": [pygame.image.load("assets/enemy/bot/bot_1_w.png"),
                 pygame.image.load("assets/enemy/bot/bot_2_w.png")],
    "Down": [pygame.image.load("assets/enemy/bot/bot_1_s.png"),
                 pygame.image.load("assets/enemy/bot/bot_2_s.png")],
    "Right": [pygame.image.load("assets/enemy/bot/bot_1_d.png"),
                 pygame.image.load("assets/enemy/bot/bot_2_d.png")],
    "Left": [pygame.image.load("assets/enemy/bot/bot_1_a.png"),
                 pygame.image.load("assets/enemy/bot/bot_2_a.png")]
}


for image in enemy_anim.keys():
    for i in range(len(enemy_anim[image])):
        enemy_anim[image][i] = \
            pygame.transform.scale(enemy_anim[image][i], (44, 44))
for image in enemy_anim_speed.keys():
    for i in range(len(enemy_anim_speed[image])):
        enemy_anim_speed[image][i] = \
            pygame.transform.scale(enemy_anim_speed[image][i], (44, 44))
for image in enemy_anim_attack.keys():
    for i in range(len(enemy_anim_attack[image])):
        enemy_anim_attack[image][i] = \
            pygame.transform.scale(enemy_anim_attack[image][i], (44, 44))
for image in enemy_anim_armor.keys():
    for i in range(len(enemy_anim_armor[image])):
        enemy_anim_armor[image][i] = \
            pygame.transform.scale(enemy_anim_armor[image][i], (44, 44))
class Enemy:
    def __init__(self, pos_x, pos_y, speed, map, type):
        self.type = type
        self.bullet = None
        self.pos_x = pos_x
        self.direction = "Down"
        self.pos_y = pos_y
        self.speed = speed

        self.enemy_anim_count = 0
        self.size = 44
        self.map = map
        self.attack_delay = 0
        self.collider = pygame.rect.Rect(self.pos_x, self.pos_y, 40, 40)
        if self.type == "armor":
            self.life = 2
            self.enemy_texture = enemy_anim_armor["Down"][0]
        elif self.type == "speed":
            self.life = 1
            self.enemy_texture = enemy_anim_speed["Down"][0]
        elif self.type == "attack":
            self.life = 1
            self.enemy_texture = enemy_anim_attack["Down"][0]
        else:
            self.life = 1
            self.enemy_texture = enemy_anim["Down"][0]

    def move(self):
        speed = 1
        if self.type == "usual":
            start, end = 0, 3
        elif self.type == "attack":
            start, end = 1, 3
        elif self.type == "speed":
            start, end = 0, 3
            speed = 2
        elif self.type == "armor":
            start, end = 1, 3
        if not self.bullet.is_shooted:
            self.attack_delay += 1
            if self.attack_delay == 200:
                self.bullet.setPosition()
                self.bullet.Move()
            self.attack_delay %= 201
        if self.bullet.is_shooted:
            self.bullet.Move()
        if self.bullet.isCollision:
            self.bullet.Freeze_bullet()

        if self.type == "usual":
            self.enemy_texture = enemy_anim[self.direction][self.enemy_anim_count]
        if self.type == "speed":
            self.enemy_texture = enemy_anim_speed[self.direction][self.enemy_anim_count]
        if self.type == "attack":
            self.enemy_texture = enemy_anim_attack[self.direction][self.enemy_anim_count]
        if self.type == "armor":
            self.enemy_texture = enemy_anim_armor[self.direction][self.enemy_anim_count]

        if self.can_move():
            self.pos_x += MOVEMENT[self.direction][0] * speed
            self.pos_y += MOVEMENT[self.direction][1] * speed
        else:
            self.get_random_direction(start, end)

        self.enemy_anim_count = (self.enemy_anim_count + 1) % 2

    def get_random_direction(self, start, end):
        self.direction = DIRECTION[random.randint(start, end)]

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
        bullet = self.bullet
        if self.type == "usual":
            self.__init__(50 * 8, 50 * 3, 1, self.map, self.type)
        elif self.type == "attack":
            self.__init__(50 * 9, 50 * 1, 1, self.map, self.type)
        elif self.type == "speed":
            self.__init__(50 * 6, 50 * 1, 1, self.map, self.type)
        else:
            self.__init__(50 * 7, 50 * 3, 1, self.map, self.type)
        self.bullet = bullet