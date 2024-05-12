from Brick import Brick

WIDTH = 1024
HEIGHT = 720


class Map:
    def __init__(self):
        self.obj_list = []
        self.obj_list.append(Brick(0, 0))

    def del_brick(self):
        self.obj_list = []


