import pygame
from sys import exit
from const import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('NeoZa game')
clock = pygame.time.Clock()
game_active = True

sky_surf = pygame.image.load('graphics/sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
score_surf = score_font.render('My Game',False,'Black')
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        screen.blit(score_surf, score_rect)

        snail_rect.x -= 3
        if snail_rect.right <= 0: snail_rect.left = 800

        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collison
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)
