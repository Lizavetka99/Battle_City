import pygame

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

for pressed_key in player_anim.keys():
    for i in range(len(player_anim[pressed_key])):
        player_anim[pressed_key][i] = \
            pygame.transform.scale(player_anim[pressed_key][i], (60, 60))


class Player:
    def __init__(self, pos_x, pos_y, speed):
        self.pos_x = pos_x
        self.direction = "Up"
        self.pos_y = pos_y
        self.speed = speed
        self.player_texture = player_anim[pygame.K_w][0]
        self.player_anim_count = 0

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w]:
            self.direction = "Up"
            self.pos_y -= self.speed
            self.player_texture = player_anim[pygame.K_w][
                self.player_anim_count]
        elif pressed_key[pygame.K_s]:
            self.direction = "Down"
            self.pos_y += self.speed
            self.player_texture = player_anim[pygame.K_s][
                self.player_anim_count]
        elif pressed_key[pygame.K_a]:
            self.direction = "Left"
            self.pos_x -= self.speed
            self.player_texture = player_anim[pygame.K_a][
                self.player_anim_count]
        elif pressed_key[pygame.K_d]:
            self.direction = "Right"
            self.pos_x += self.speed
            self.player_texture = player_anim[pygame.K_d][
                self.player_anim_count]

        self.player_anim_count = (self.player_anim_count + 1) % 2
