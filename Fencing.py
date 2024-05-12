class Fencing:
    def __init__(self, pos_x, pos_y):
        self.life = True
        self.x = pos_x
        self.y = pos_y

    def hit(self):
        self.life = False
        del self