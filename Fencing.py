class Fencing:
    def __init__(self, pos_x, pos_y, type):
        self.life = True
        self.x = pos_x
        self.y = pos_y
        self.type = type


    def destroy(self):
        self.life = False
        del self