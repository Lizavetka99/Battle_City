from Brick import Brick

WIDTH = 1024
HEIGHT = 720


class Map:
    def __init__(self):
        self.obj_list = []
        x, y = 0, 0
        for i in range(10):
            x = 100 * i
            self.obj_list.append(Brick(x, y))


    def del_brick(self, brick):
        brick.destroy()
        self.obj_list.remove(brick)


