from Brick import Brick

WIDTH = 800
HEIGHT = 800


class Map:
    def __init__(self):
        self.obj_list = []
        x, y = 0, 0
        for i in range(16):
            x = 50 * i
            self.obj_list.append(Brick(x, y))
        for i in range(1, 16):
            y = 50*i
            self.obj_list.append(Brick(x, y))
        for i in range(15, -1, -1):
            x = 50*i
            self.obj_list.append(Brick(x, y))
        for i in range(15, 0, -1):
            y = 50*i
            self.obj_list.append(Brick(x, y))



    def del_brick(self, brick):
        brick.destroy()
        self.obj_list.remove(brick)


