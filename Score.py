import pygame
import Player

class Score:
    def __init__(self):
        self.score_time = 0
        self.score = 0
        self.text = f"Score: {self.score}"
        self.x = 600
        self.is_enemy_killed = False
        self.y = 10
        self.enemy_x = -100
        self.enemy_y = -100
        self.text_surface = pygame.font.SysFont("Ariel", 50).render(self.text,
                                                                    True,
                                                                    (255, 255, 255))
        self.enemy_score = pygame.font.SysFont("Ariel", 30).render("100", True,
                                                                   (0, 128, 0))

    def update_score(self):
        self.score += 100
        self.text = f"Score: {self.score}"
        self.text_surface = pygame.font.SysFont("Ariel", 30).render(self.text, True, (0, 0, 0))
        self.enemy_x, self.enemy_y = Player.LAST_ENEMY_KILLED_COORDS

    def check_time_to_show(self):
        if self.is_enemy_killed:
            self.score_time += 1
        if self.score_time == 100:
            self.is_enemy_killed = False
            return False
        return True

