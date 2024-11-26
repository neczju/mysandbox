import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()
dt = 0

player_surf = pygame.image.load('sprite.png').convert_alpha()
player_rect = player_surf.get_rect(center = (200, 300))
player_speed = 400

ball_surf = pygame.image.load('ball.png').convert_alpha()
ball_rect = ball_surf.get_rect(center = (400, 300))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('black')
    screen.blit(player_surf, player_rect)
    screen.blit(ball_surf, ball_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_rect.y -= round(player_speed * dt)
    if keys[pygame.K_DOWN]:
        player_rect.y += round(player_speed * dt)

    if player_rect.top <= 0:
        player_rect.top = 0
    if player_rect.bottom >= 600:
        player_rect.bottom = 600

    ball_rect.x -= round(player_speed * dt)
    if ball_rect.colliderect(player_rect):
        ball_rect.y -= round(player_speed * dt)
        ball_rect.x += round(player_speed * dt)

    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
