from Map import Map
import Player
import pygame

# SCREEN SETTINGS
WIDTH = 1024
HEIGHT = 720
BACKGROUND = "assets/background_test.jpg"


class Screen:
    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load("assets/background_test.jpg")
        self.background = pygame.transform.\
            scale(self.background, (WIDTH, HEIGHT))
        self.map = Map()

    def update_screen(self, obj_list, player: Player.Player):
        """
        :param obj_list:
        :type player: Player.Player
        """
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(player.player_texture, (player.pos_x, player.pos_y))
        for obj in obj_list:
            self.screen.blit(obj.image, (obj.fencing))

    def __get_map__(self):
        return self.map