import pygame
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()
dt = 0

player_surf = pygame.image.load(Path('assets/player_sprite.png')).convert_alpha()
player_rect = player_surf.get_rect(center = (400, 300))
player_speed = 300
player_direction = ''

box_surf = pygame.image.load(Path('assets/box_sprite.png')).convert_alpha()
box_rect = box_surf.get_rect(center = (400, 250))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= round(player_speed * dt)
        player_direction = 'up'
    if keys[pygame.K_s]:
        player_rect.y += round(player_speed * dt)
        player_direction = 'down'
    if keys[pygame.K_a]:
        player_rect.x -= round(player_speed * dt)
        player_direction = 'left'
    if keys[pygame.K_d]:
        player_rect.x += round(player_speed * dt)
        player_direction = 'right'

    if player_rect.colliderect(box_rect):
        if player_direction == 'up':
            player_rect.bottom += round(player_speed * dt)
        elif player_direction == 'down':
            player_rect.top -= round(player_speed * dt)
        elif player_direction == 'left':
            player_rect.right += round(player_speed * dt)
        elif player_direction == 'right':
            player_rect.left -= round(player_speed * dt)

    screen.blit(player_surf, player_rect)
    screen.blit(box_surf, box_rect)

    pygame.display.update() 
    dt = clock.tick(60) / 1000

pygame.quit()
