import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 720))
pygame.display.set_caption("Battle City")
icon = pygame.image.load("assets/game_icon.jpg")
pygame.display.set_icon(icon)

bg = pygame.image.load("assets/background_test.jpg")
bg = pygame.transform.scale(bg, (1024, 720))
# player_anim = [pygame.image.load("assets/Player_tank_1_w.png"),
#                pygame.image.load("assets/tank_s.png"),
#                pygame.image.load("assets/tank_a.png"),
#                pygame.image.load("assets/tank_d.png")]
player_anim = {
    pygame.K_w : [pygame.image.load("assets/player_tank/Player_tank_1_w.png"),
                  pygame.image.load("assets/player_tank/Player_tank_2_w.png")],
    pygame.K_s : [pygame.image.load("assets/player_tank/Player_tank_1_s.png"),
                  pygame.image.load("assets/player_tank/Player_tank_2_s.png")],
    pygame.K_d : [pygame.image.load("assets/player_tank/Player_tank_1_d.png"),
                  pygame.image.load("assets/player_tank/Player_tank_2_d.png")],
    pygame.K_a : [pygame.image.load("assets/player_tank/Player_tank_1_a.png"),
                  pygame.image.load("assets/player_tank/Player_tank_2_a.png")],

}

player_anim_count = 0
for keys in player_anim.keys():
    for i in range(len(player_anim[keys])):
        player_anim[keys][i] = pygame.transform.scale(player_anim[keys][i], (100, 100))
player_pos_x = 100
player_pos_y = 100
speed = 0.1
player = player_anim[pygame.K_w][0]

running = True
while running:
    pygame.display.update()
    screen.blit(bg, (0,0))
    screen.blit(player, (player_pos_x, player_pos_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos_y -= speed
        player = player_anim[pygame.K_w][player_anim_count]
    elif keys[pygame.K_s]:
        player_pos_y += speed
        player = player_anim[pygame.K_s][player_anim_count]
    elif keys[pygame.K_a]:
        player_pos_x -= speed
        player = player_anim[pygame.K_a][player_anim_count]
    elif keys[pygame.K_d]:
        player_pos_x += speed
        player = player_anim[pygame.K_d][player_anim_count]

    player_anim_count = (player_anim_count + 1) % 2

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False
            pygame.quit()