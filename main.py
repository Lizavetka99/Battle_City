import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battle City")
icon = pygame.image.load("assets/game_icon.jpg")
pygame.display.set_icon(icon)

running = True
while running:
    pygame.display.update()

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
            pygame.quit()