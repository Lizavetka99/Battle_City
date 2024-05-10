import Player
import Screen
import pygame


pygame.init()

# CLASS OBJECTS
screen = Screen.Screen()
player = Player.Player(100, 100, 0.1)

# SETTINGS
pygame.display.set_caption("Battle City")
icon = pygame.image.load("assets/game_icon.jpg")
pygame.display.set_icon(icon)
running = True

while running:
    pygame.display.update()
    screen.update_screen(player)
    player.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
