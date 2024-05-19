import Enemy
from Map import Map
import Player
import pygame

# SCREEN SETTINGS
WIDTH = 800
HEIGHT = 800
BACKGROUND = "assets/bg_one_tone.jpg"


class Screen:
    def __init__(self, score):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load(BACKGROUND)
        self.background = pygame.transform.\
            scale(self.background, (WIDTH, HEIGHT))
        self.map = Map(1, score)

    def update_screen(self, obj_list, player: Player.Player, enemies: [Enemy.Enemy], gift):
        """
        :param enemy:
        :param obj_list:
        :type player: Player.Player
        """
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(gift.image, (gift.x, gift.y))
        self.screen.blit(player.player_texture, (player.pos_x, player.pos_y))
        for enemy in enemies:
            self.screen.blit(enemy.enemy_texture, (enemy.pos_x, enemy.pos_y))
        for obj in obj_list:
            self.screen.blit(obj.image, (obj.x, obj.y))


    def update_player_lives(self, lives_count, heart_texture):
        pos_x, pos_y = 30, 30
        for i in range(lives_count):
            self.screen.blit(heart_texture, (pos_x, pos_y))
            pos_x += 30

    def update_bases_lives(self, p_base_lifes, e_base_lifes, p_heart, e_heart):
        e_pos_x, e_pos_y = 340, 15
        p_pos_x, p_pos_y = 340, 755
        for i in range(e_base_lifes):
            self.screen.blit(e_heart, (e_pos_x, e_pos_y))
            e_pos_x += 30
        for i in range(p_base_lifes):
            self.screen.blit(p_heart, (p_pos_x, p_pos_y))
            p_pos_x += 30

    def __get_map__(self):
        return self.map