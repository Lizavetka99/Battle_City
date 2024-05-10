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

    def update_screen(self, player: Player.Player):
        """
        :type player: Player.Player
        """
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(player.player_texture, (player.pos_x, player.pos_y))
