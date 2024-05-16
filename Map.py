from Brick import Brick

WIDTH = 800
HEIGHT = 800


class Map:
    def __init__(self, numb):
        self.obj_list = []
        if numb == 1:
            self.__level1__()
        else: self.level_test()


    def del_brick(self, brick):
        brick.destroy()
        self.obj_list.remove(brick)

    def level_test(self):
        r = Brick.size
        self.obj_list.append(Brick(r * 7, r * 7))

    def __level1__(self):
        r = Brick.size
        for i in range(16):
            self.obj_list.append(Brick(0, r * i))
            self.obj_list.append(Brick(15 * r, r * i))
        for i in range(1, 15):
            self.obj_list.append(Brick(i * r, 0))
            self.obj_list.append(Brick(i * r, 15 * r))

        # боковые выступы
        for j in range(7, 9):
            self.obj_list.append(Brick(1 * r, r * j))
            self.obj_list.append(Brick(14 * r, r * j))

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

