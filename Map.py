import Player
from Brick import Brick
from Water import Water
from Base import Base
import pygame

from Gift import Gift
from Strong_wall import Strong_wall

WIDTH = 800
HEIGHT = 800

class Map:
    def __init__(self, numb, score):
        self.obj_list = []
        self.players = []
        self.score = score
        self.bullets = []
        self.base = []
        self.baysic()
        if numb == 1:
            self.__level1__()
        elif numb == 2:
            self.__level2__()
        elif numb == 3:
            self.__level3__()
        elif numb == 4:
            self.__level4__()
        else: self.level_test()


    def add_player(self, player):
        self.players.append(player)


    def add_base(self, p_base):
        self.obj_list.append(p_base)
        self.base.append(p_base)
    def add_bullet(self, bullet):
        self.bullets.append(bullet)

#если база противника убита то выиграл
    def win(self, base):
        if base.fencing == (50 * 7, 50 * 1):
            return True
        return False

    def del_fencing(self, fencing):
        if fencing.type != "strong_wall":
            fencing.lifes -= 1
            if fencing.lifes == 0:
                fencing.destroy()
                self.obj_list.remove(fencing)
            elif fencing.type == "brick":
                fencing.image = pygame.image.load(f"assets/brick_wall_{fencing.lifes}.png")
                fencing.image = pygame.transform.scale(fencing.image, (50, 50))

    def take_gift(self, gift):
        gift.destroy()

    def del_player(self, player, bullet):

        if type(player) == Player.Player:
            if not player.is_alive:
                player.life -= 1
                player.destroy()
        else:
            player.life -= 1
            if player.life == 0:
                if type(bullet.player) == Player.Player:
                    Player.KILLS += 1
                    Player.LAST_ENEMY_KILLED_COORDS = (player.pos_x, player.pos_y)
                    self.score.update_score()
                    self.score.score_time = 0
                    self.score.is_enemy_killed = True
                #pos_x = player.pos_x
                #pos_y = player.pos_y
                player.destroy()
                #self.obj_list.append(Gift(pos_x,pos_y))



    def level_test(self):
        r = Brick.size
        self.obj_list.append(Brick(r * 7, r * 7))

    def __level1__(self):
        r = Brick.size
        # боковые выступы
        for j in range(7, 9):
            self.obj_list.append(Strong_wall(1 * r, r * j))
            self.obj_list.append(Strong_wall(14 * r, r * j))

        for j in {2, 4, 6}:
            # самый левый/правый столбик
            for i in range(2, 5):
                self.obj_list.append(Brick(j * r, i * r))
                self.obj_list.append(Brick((15 - j) * r, i * r))
                self.obj_list.append(Brick(j * r, (15 - i) * r))
                self.obj_list.append(Brick((15 - j) * r, (15 - i) * r))

            # середина вертикальная
        for i in {2, 4, 11, 13}:
            self.obj_list.append(Brick(i * r, 5 * r))
            self.obj_list.append(Brick(i * r, 10 * r))

        # середина horizontal
        for i in range(6, 10):
            self.obj_list.append(Brick(i * r, 6 * r))
            self.obj_list.append(Brick(i * r, 9 * r))

        self.obj_list.append(Brick(7 * r, 7 * r))
        self.obj_list.append(Brick(8 * r, 8 * r))
        #
        for i in range(3, 6):
            self.obj_list.append(Brick(i * r, 8 * r))
            self.obj_list.append(Brick((15 - i) * r, 7 * r))
        self.obj_list.append(Brick(3 * r, 7 * r))
        self.obj_list.append(Brick(12 * r, 8 * r))

    def baysic(self):
        r = Brick.size
        for i in range(16):
            self.obj_list.append(Strong_wall(0, r * i))
            self.obj_list.append(Strong_wall(15 * r, r * i))
        for i in range(1, 15):
            self.obj_list.append(Strong_wall(i * r, 0))
            self.obj_list.append(Strong_wall(i * r, 15 * r))

    def __level2__(self):
        r = Brick.size

        # боковые выступы
        self.obj_list.append(Brick(1 * r, r * 7))
        self.obj_list.append(Brick(1 * r, r * 8))
        self.obj_list.append(Brick(14 * r, r * 8))

        self.obj_list.append(Brick(2 * r, r * 14))
        self.obj_list.append(Brick(4 * r, r * 14))
        self.obj_list.append(Brick(6 * r, r * 14))
        self.obj_list.append(Brick(4 * r, r * 13))
        self.obj_list.append(Brick(1 * r, r * 12))
        self.obj_list.append(Brick(6 * r, r * 12))
        self.obj_list.append(Brick(6 * r, r * 13))
        self.obj_list.append(Brick(4 * r, r * 12))

        self.obj_list.append(Brick(9 * r, r * 12))
        self.obj_list.append(Brick(8 * r, r * 12))
        self.obj_list.append(Brick(10 * r, r * 14))
        self.obj_list.append(Brick(11 * r, r * 13))
        #self.obj_list.append(Strong_wall(10 * r, r * 13))
        self.obj_list.append(Brick(11 * r, r * 14))

        self.obj_list.append(Brick(11 * r, r * 12))
        self.obj_list.append(Brick(12 * r, r * 12))
        self.obj_list.append(Brick(13 * r, r * 12))
        self.obj_list.append(Brick(13 * r, r * 13))

        self.obj_list.append(Brick(7 * r, r * 10))
        self.obj_list.append(Brick(6 * r, r * 10))
        self.obj_list.append(Brick(5 * r, r * 10))
        self.obj_list.append(Brick(11 * r, r * 12))
        self.obj_list.append(Brick(2 * r, r * 12))
        self.obj_list.append(Brick(9 * r, r * 11))
        self.obj_list.append(Brick(9 * r, r * 10))
        self.obj_list.append(Brick(10 * r, r * 10))
        self.obj_list.append(Brick(11 * r, r * 10))
        self.obj_list.append(Brick(14 * r, r * 10))
        self.obj_list.append(Brick(13 * r, r * 10))
        self.obj_list.append(Brick(2 * r, r * 11))
        self.obj_list.append(Brick(2 * r, r * 10))
        self.obj_list.append(Brick(3 * r, r * 10))

        self.obj_list.append(Brick(7 * r, r * 9))
        self.obj_list.append(Brick(7 * r, r * 8))
        self.obj_list.append(Brick(6 * r, r * 8))
        self.obj_list.append(Brick(4 * r, r * 8))
        self.obj_list.append(Brick(3 * r, r * 8))

        self.obj_list.append(Brick(8 * r, r * 8))
        self.obj_list.append(Brick(10 * r, r * 9))
        self.obj_list.append(Brick(13 * r, r * 7))
        self.obj_list.append(Brick(12 * r, r * 8))
        self.obj_list.append(Brick(2 * r, r * 7))

        self.obj_list.append(Brick(4 * r, r * 7))
        self.obj_list.append(Brick(7 * r, r * 7))
        self.obj_list.append(Brick(9 * r, r * 7))
        self.obj_list.append(Brick(10 * r, r * 7))

        self.obj_list.append(Brick(5 * r, r * 6))
        self.obj_list.append(Brick(2 * r, r * 6))
        self.obj_list.append(Brick(10 * r, r * 6))
        self.obj_list.append(Brick(11 * r, r * 6))
        self.obj_list.append(Brick(13 * r, r * 6))

        self.obj_list.append(Brick(4 * r, r * 5))
        self.obj_list.append(Brick(4 * r, r * 4))
        self.obj_list.append(Brick(3 * r, r * 4))
        self.obj_list.append(Brick(2 * r, r * 4))

        self.obj_list.append(Brick(7 * r, r * 5))
        self.obj_list.append(Brick(8 * r, r * 5))

        self.obj_list.append(Brick(14 * r, r * 4))
        self.obj_list.append(Brick(13 * r, r * 4))
        self.obj_list.append(Brick(12 * r, r * 4))
        self.obj_list.append(Brick(9 * r, r * 4))

        self.obj_list.append(Brick(11 * r, r * 3))
        self.obj_list.append(Brick(13 * r, r * 3))
        self.obj_list.append(Brick(2 * r, r * 2))
        self.obj_list.append(Brick(1 * r, r * 3))
        self.obj_list.append(Brick(4 * r, r * 2))
        self.obj_list.append(Brick(5 * r, r * 3))

        self.obj_list.append(Brick(6 * r, r * 2))
        self.obj_list.append(Brick(13 * r, r * 1))
        self.obj_list.append(Brick(10 * r, r * 2))
        self.obj_list.append(Brick(11 * r, r * 2))

    def __level3__(self):
        r = Brick.size
        self.obj_list.append(Brick(1 * r, 7 * r))
        self.obj_list.append(Brick(1 * r, 8 * r))
        self.obj_list.append(Brick(1 * r, 12 * r))
        self.obj_list.append(Brick(2 * r, 12 * r))
        self.obj_list.append(Brick(2 * r, 13 * r))
        self.obj_list.append(Brick(3 * r, 6 * r))
        self.obj_list.append(Brick(4 * r, 6 * r))
        self.obj_list.append(Brick(4 * r, 7 * r))
        self.obj_list.append(Brick(4 * r, 11 * r))
        self.obj_list.append(Brick(4 * r, 12 * r))
        self.obj_list.append(Brick(4 * r, 13 * r))
        self.obj_list.append(Brick(5 * r, 2 * r))
        self.obj_list.append(Brick(5 * r, 3 * r))
        self.obj_list.append(Brick(5 * r, 4 * r))
        self.obj_list.append(Brick(5 * r, 7 * r))
        self.obj_list.append(Brick(5 * r, 8 * r))
        self.obj_list.append(Brick(5 * r, 11 * r))
        self.obj_list.append(Brick(6 * r, 2 * r))
        self.obj_list.append(Brick(6 * r, 13 * r))
        self.obj_list.append(Brick(6 * r, 14 * r))
        self.obj_list.append(Brick(9 * r, 2 * r))
        self.obj_list.append(Brick(9 * r, 13 * r))
        self.obj_list.append(Brick(10 * r, 2 * r))
        self.obj_list.append(Brick(10 * r, 3 * r))
        self.obj_list.append(Brick(10 * r, 4 * r))
        self.obj_list.append(Brick(10 * r, 13 * r))
        self.obj_list.append(Brick(11 * r, 6 * r))
        self.obj_list.append(Brick(11 * r, 7 * r))
        self.obj_list.append(Brick(11 * r, 13 * r))
        self.obj_list.append(Brick(12 * r, 6 * r))
        self.obj_list.append(Brick(13 * r, 3 * r))
        self.obj_list.append(Brick(13 * r, 9 * r))
        self.obj_list.append(Brick(13 * r, 10 * r))
        self.obj_list.append(Brick(13 * r, 11 * r))
        self.obj_list.append(Brick(14 * r, 2 * r))
        self.obj_list.append(Brick(14 * r, 4 * r))

        self.obj_list.append(Strong_wall(2 * r, 3 * r))
        self.obj_list.append(Strong_wall(2 * r, 4 * r))
        self.obj_list.append(Strong_wall(3 * r, 3 * r))
        self.obj_list.append(Strong_wall(3 * r, 4 * r))
        self.obj_list.append(Strong_wall(3 * r, 10 * r))
        self.obj_list.append(Strong_wall(7 * r, 6 * r))
        self.obj_list.append(Strong_wall(7 * r, 7 * r))
        self.obj_list.append(Strong_wall(8 * r, 6 * r))
        self.obj_list.append(Strong_wall(8 * r, 7 * r))
        self.obj_list.append(Strong_wall(11 * r, 3 * r))
        self.obj_list.append(Strong_wall(13 * r, 13 * r))

        self.obj_list.append(Water(5 * r, 14 * r))
        self.obj_list.append(Water(8 * r, 10 * r))
        self.obj_list.append(Water(9 * r, 10 * r))
        self.obj_list.append(Water(10 * r, 10 * r))
        self.obj_list.append(Water(14 * r, 3 * r))

    def __level4__(self):
        r = Brick.size
        self.obj_list.append(Strong_wall(2 * r, 6 * r))
        self.obj_list.append(Strong_wall(2 * r, 5 * r))
        self.obj_list.append(Strong_wall(2 * r, 7 * r))
        self.obj_list.append(Strong_wall(2 * r, 8 * r))
        self.obj_list.append(Strong_wall(2 * r, 9 * r))
        self.obj_list.append(Strong_wall(2 * r, 10 * r))
        self.obj_list.append(Strong_wall(3 * r, 7 * r))
        self.obj_list.append(Strong_wall(3 * r, 10 * r))
        self.obj_list.append(Strong_wall(4 * r, 7 * r))
        self.obj_list.append(Strong_wall(4 * r, 8 * r))
        self.obj_list.append(Strong_wall(4 * r, 9 * r))
        self.obj_list.append(Strong_wall(4 * r, 10 * r))
        self.obj_list.append(Strong_wall(6 * r, 7 * r))
        self.obj_list.append(Strong_wall(6 * r, 8 * r))
        self.obj_list.append(Strong_wall(6 * r, 9 * r))
        self.obj_list.append(Strong_wall(6 * r, 10 * r))
        self.obj_list.append(Strong_wall(7 * r, 7 * r))
        self.obj_list.append(Strong_wall(7 * r, 10 * r))
        self.obj_list.append(Strong_wall(8 * r, 6 * r))
        self.obj_list.append(Strong_wall(8 * r, 7 * r))
        self.obj_list.append(Strong_wall(8 * r, 8 * r))
        self.obj_list.append(Strong_wall(8 * r, 9 * r))
        self.obj_list.append(Strong_wall(8 * r, 10 * r))
        self.obj_list.append(Strong_wall(9 * r, 10 * r))
        self.obj_list.append(Strong_wall(11 * r, 7 * r))
        self.obj_list.append(Strong_wall(11 * r, 8 * r))
        self.obj_list.append(Strong_wall(11 * r, 9 * r))
        self.obj_list.append(Strong_wall(11 * r, 10 * r))
        self.obj_list.append(Strong_wall(11 * r, 12 * r))
        self.obj_list.append(Strong_wall(11 * r, 13 * r))
        self.obj_list.append(Strong_wall(12 * r, 10 * r))
        self.obj_list.append(Strong_wall(12 * r, 13 * r))
        self.obj_list.append(Strong_wall(13 * r, 7 * r))
        self.obj_list.append(Strong_wall(13 * r, 8 * r))
        self.obj_list.append(Strong_wall(13 * r, 9 * r))
        self.obj_list.append(Strong_wall(13 * r, 10 * r))
        self.obj_list.append(Strong_wall(13 * r, 11 * r))
        self.obj_list.append(Strong_wall(13 * r, 12 * r))
        self.obj_list.append(Strong_wall(13 * r, 13 * r))
























































