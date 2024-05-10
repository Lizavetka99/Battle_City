import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battle City")
icon = pygame.image.load("assets/game_icon.jpg")
pygame.display.set_icon(icon)

bg = pygame.image.load("assets/background_test.jpg")
player = pygame.image.load("assets/tank.png")


running = True
while running:
    pygame.display.update()

    screen.blit(bg, (0,0))
    screen.blit(player, (100, 100))
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
            pygame.quit()