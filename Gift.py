import pygame
import Player

image_row = pygame.image.load("assets/gift.png")
image = pygame.transform.scale(image_row, (40, 40))

class Gift:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.image = image
        self.is_available = False

    def destroy(self):
        del self

    def spawn(self):
        self.is_available = True
        self.x, self.y = Player.LAST_ENEMY_KILLED_COORDS
        Player.KILLS = 0

    def check_collision_with_player(self, player):
        self.collider = pygame.rect.Rect(self.x, self.y, 40, 40)
        if self.collider.colliderect(player.collider):
            player.is_alive = True
            self.is_available = False
            self.x = -100
            self.y = -100
        return
