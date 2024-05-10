import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battle City")
icon = pygame.image.load("assets/game_icon.jpg")
pygame.display.set_icon(icon)

bg = pygame.image.load("assets/background_test.jpg")
player = pygame.image.load("assets/tank.png")
player = pygame.transform.scale(player, (50, 50))
player_pos_x = 100
player_pos_y = 100
speed = 10

running = True
while running:
    pygame.display.update()

    screen.blit(bg, (0,0))
    screen.blit(player, (player_pos_x, player_pos_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos_y -= speed
    elif keys[pygame.K_s]:
        player_pos_y += speed
    elif keys[pygame.K_a]:
        player_pos_x -= speed
    elif keys[pygame.K_d]:
        player_pos_y += speed

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
            pygame.quit()