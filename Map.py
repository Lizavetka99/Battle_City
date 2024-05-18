import Player
from Brick import Brick
from Base import Base
import pygame

from Gift import Gift
from Strong_wall import Strong_wall

WIDTH = 800
HEIGHT = 800

class Map:
    def __init__(self, numb):
        self.obj_list = []
        self.players = []
        self.bullets = []
        self.base = []
        if numb == 1:
            self.__level1__()
        else: self.level_test()


    def add_player(self, player):
        self.players.append(player)

    def add_base(self, p_base):
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

    def del_player(self, player):
        player.life -= 1
        if type(player) == Player.Player:
            player.destroy()
        else:
            if player.life == 0:
                #pos_x = player.pos_x
                #pos_y = player.pos_y
                player.destroy()
                #self.obj_list.append(Gift(pos_x,pos_y))



    def level_test(self):
        r = Brick.size
        self.obj_list.append(Brick(r * 7, r * 7))

    def __level1__(self):
        r = Brick.size
        for i in range(16):
            self.obj_list.append(Strong_wall(0, r * i))
            self.obj_list.append(Strong_wall(15 * r, r * i))
        for i in range(1, 15):
            self.obj_list.append(Strong_wall(i * r, 0))
            self.obj_list.append(Strong_wall(i * r, 15 * r))

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

