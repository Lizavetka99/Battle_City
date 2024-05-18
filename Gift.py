import pygame

image_row = pygame.image.load("assets/gift.png")
image = pygame.transform.scale(image_row, (40, 40))

class Gift:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.image = image
        self.collider = pygame.rect.Rect(self.x, self.y, 40, 40)

    def destroy(self):
        del self
