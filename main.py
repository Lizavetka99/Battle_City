import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Battle City")
icon = pygame.image.load("assets/game_icon.jpg")
pygame.display.set_icon(icon)

bg = pygame.image.load("assets/background_test.jpg")
player_anim = [pygame.image.load("assets/tank_w.png"),
               pygame.image.load("assets/tank_s.png"),
               pygame.image.load("assets/tank_a.png"),
               pygame.image.load("assets/tank_d.png")]
for i in range(len(player_anim)):
    player_anim[i] = pygame.transform.scale(player_anim[i], (50, 50))
player_pos_x = 100
player_pos_y = 100
speed = 0.3
player = player_anim[0]

running = True
while running:
    pygame.display.update()

    screen.blit(bg, (0,0))
    screen.blit(player, (player_pos_x, player_pos_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos_y -= speed
        player = player_anim[0]
    elif keys[pygame.K_s]:
        player_pos_y += speed
        player = player_anim[1]
    elif keys[pygame.K_a]:
        player_pos_x -= speed
        player = player_anim[2]
    elif keys[pygame.K_d]:
        player_pos_x += speed
        player = player_anim[3]

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
            pygame.quit()