import Player
import Base
import Screen
import Bullet
import pygame
import Enemy



pygame.init()

p_image_row = pygame.image.load("assets/base.jpg")
e_image_row = pygame.image.load("assets/evil_base.jpg")

p_image = pygame.transform.scale(p_image_row, (100, 100))
e_image = pygame.transform.scale(e_image_row, (100, 100))

# CLASS OBJECTS
screen = Screen.Screen()
player = Player.Player(50 * 7, 50 * 12, 1, screen.map)
bullet = Bullet.Bullet(player, screen.map)
enemy = Enemy.Enemy(50 * 8, 50 * 3, 1, screen.map, "usual")
bullet_enemy = Bullet.Bullet(enemy, screen.map)
enemy.bullet = bullet_enemy


p_base = Base.Base(50 * 7, 50 * 13, player, p_image)
e_base = Base.Base(50 * 7, 50 * 1, enemy, e_image)

enemy_base_attack = Enemy.Enemy(50 * 10, 50 * 3, 1, screen.map, "attack")
enemy_base_attack_bullet = Bullet.Bullet(enemy_base_attack, screen.map)
enemy_base_attack.bullet = enemy_base_attack_bullet

screen.map.add_base(p_base)
screen.map.add_base(e_base)
screen.map.add_player(player)
screen.map.add_player(enemy)
screen.map.add_bullet(bullet)
screen.map.add_bullet(bullet_enemy)
screen.map.add_player(enemy_base_attack)
screen.map.add_bullet(enemy_base_attack_bullet)

# SETTINGS
pygame.display.set_caption("Battle City")
icon = pygame.image.load("assets/game_icon.jpg")
pygame.display.set_icon(icon)
running = True
enemies = [enemy, enemy_base_attack]

while running:
    pygame.display.update()
    screen.update_screen(screen.map.obj_list, player, enemies)
    player.move()
    screen.screen.blit(p_base.image, (p_base.x, p_base.y))
    screen.screen.blit(e_base.image, (e_base.x, e_base.y))
    for enemy in enemies:
        if screen.map.players.__contains__(enemy):
            enemy.move()
    if bullet.isCollision:
        bullet.Freeze_bullet()
    if pygame.key.get_pressed()[pygame.K_SPACE] and (not bullet.is_shooted):
        bullet.setPosition()
        screen.screen.blit(bullet.texture, (bullet.X, bullet.Y))
    if bullet.is_shooted:
        bullet.Move()
        screen.screen.blit(bullet.texture, (bullet.X, bullet.Y))
    for e in enemies:
        if e.bullet.is_shooted:
            screen.screen.blit(e.bullet.texture, (e.bullet.X, e.bullet.Y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
