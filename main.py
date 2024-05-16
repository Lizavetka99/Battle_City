import Enemy
import Player
import Screen
import Bullet
import pygame
import Enemy
from Map import Map

pygame.init()

# CLASS OBJECTS
screen = Screen.Screen()
player = Player.Player(50, 50, 1, screen.map)
bullet = Bullet.Bullet(player, screen.map)
enemy = Enemy.Enemy(100, 50, 1, screen.map)

# SETTINGS
pygame.display.set_caption("Battle City")
icon = pygame.image.load("assets/game_icon.jpg")
pygame.display.set_icon(icon)
running = True
count = 0
while running:
    count += 1
    pygame.display.update()
    screen.update_screen(screen.map.obj_list, player, enemy)
    player.move()
    enemy.move()
    if bullet.isCollision:
        bullet.Freeze_bullet()
    if pygame.key.get_pressed()[pygame.K_SPACE] and (not bullet.is_shooted):
        bullet.setPosition()
        screen.screen.blit(bullet.texture, (bullet.X, bullet.Y))
    if bullet.is_shooted:
        bullet.Move()
        screen.screen.blit(bullet.texture, (bullet.X, bullet.Y))

    if pygame.key.get_pressed()[pygame.K_q]:
        screen.map.del_brick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
