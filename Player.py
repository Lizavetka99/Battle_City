import pygame

import Gift

MOVEMENT = {
    "Up" : [0, -1],
    "Down" : [0, 1],
    "Left" : [-1, 0],
    "Right" : [1, 0]
}
player_anim = {
    pygame.K_w: [pygame.image.load("assets/player_tank/Player_tank_1_w.png"),
                 pygame.image.load("assets/player_tank/Player_tank_2_w.png")],
    pygame.K_s: [pygame.image.load("assets/player_tank/Player_tank_1_s.png"),
                 pygame.image.load("assets/player_tank/Player_tank_2_s.png")],
    pygame.K_d: [pygame.image.load("assets/player_tank/Player_tank_1_d.png"),
                 pygame.image.load("assets/player_tank/Player_tank_2_d.png")],
    pygame.K_a: [pygame.image.load("assets/player_tank/Player_tank_1_a.png"),
                 pygame.image.load("assets/player_tank/Player_tank_2_a.png")]
}

for image in player_anim.keys():
    for i in range(len(player_anim[image])):
        player_anim[image][i] = \
            pygame.transform.scale(player_anim[image][i], (44, 44))


class Player:
    def __init__(self, pos_x, pos_y, speed, map):
        self.pos_x = pos_x
        self.direction = "Up"
        self.pos_y = pos_y
        self.speed = speed
        self.player_texture = player_anim[pygame.K_w][0]
        self.player_anim_count = 0
        self.size = 44
        self.map = map
        self.collider = pygame.rect.Rect(self.pos_x, self.pos_y, 40, 40)
        self.life = 3
        self.invincibility = False



    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w]:
            self.direction = "Up"
            self.player_texture = player_anim[pygame.K_w][
                self.player_anim_count]
            if self.can_move():self.pos_y -= self.speed
        elif pressed_key[pygame.K_s]:
            self.direction = "Down"
            self.player_texture = player_anim[pygame.K_s][
                self.player_anim_count]
            if self.can_move():self.pos_y += self.speed
        elif pressed_key[pygame.K_a]:
            self.direction = "Left"
            self.player_texture = player_anim[pygame.K_a][
                self.player_anim_count]
            if self.can_move():self.pos_x -= self.speed
        elif pressed_key[pygame.K_d]:
            self.direction = "Right"
            self.player_texture = player_anim[pygame.K_d][
                self.player_anim_count]
            if self.can_move():self.pos_x += self.speed

        self.player_anim_count = (self.player_anim_count + 1) % 2

    def can_move(self):
        dx,dy = MOVEMENT[self.direction]
        self.collider = pygame.rect.Rect(self.pos_x + dx, self.pos_y + dy, 40, 40)
        for fencing in self.map.obj_list:
            #if type(fencing) == Gift.Gift: continue
            if self.collider.colliderect(fencing.collider):
                return False
        for player in self.map.players:
            if player == self: continue
            if self.collider.colliderect(player.collider):
                return False
        return True

    def destroy(self):
        self.__init__(50 * 7, 50 * 12, 1, self.map)