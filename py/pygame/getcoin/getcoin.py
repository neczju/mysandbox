import pygame
from pathlib import Path
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()
dt = 0 # deltatime

# Fonts
timer_font = pygame.font.Font(Path('fonts/Roboto-Regular.ttf'), 30)
score_font = pygame.font.Font(Path('fonts/Roboto-Regular.ttf'), 40)

# Player
player_surf = pygame.image.load(Path('assets/player_sprite.png')).convert_alpha()
player_rect = player_surf.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))
player_speed = 300
player_pos = pygame.Vector2(player_rect.x, player_rect.y)

# Score
player_score = 0
score_text = score_font.render(f'score: {player_score}', True, 'white')
score_rect = score_text.get_rect(topleft = (0, 0))

# Coin
coin_surf = pygame.image.load(Path('assets/coin_sprite.png')).convert_alpha()
coin_rect = coin_surf.get_rect(topleft = (-100, -100))

# Timer
game_active = True
counter = 5
pygame.time.set_timer(pygame.USEREVENT, 1000)
timer_text = timer_font.render(f'timer: {counter}', True, 'white')
timer_rect = timer_text.get_rect(topright = (800, 0))

# Game over
gameover_font = pygame.font.Font(Path('fonts/Roboto-Regular.ttf'), 50)
gameover_text = gameover_font.render('GAME OVER!', True, 'black')
gameover_rect = gameover_text.get_rect(center = (400, 300))

while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        if event.type == pygame.USEREVENT:
            counter -= 1
            if counter <= 0:
                game_active = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_active:
            game_active = True
            counter = 5
            player_score = 0
            

    if game_active:
        # Draw
        screen.fill('black')


        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_rect.x -= round(player_speed * dt)
        if keys[pygame.K_d]:
            player_rect.x += round(player_speed * dt)
        if keys[pygame.K_w]:
            player_rect.y -= round(player_speed * dt)
        if keys[pygame.K_s]:
            player_rect.y += round(player_speed * dt)

        if player_rect.left <= 0:
            player_rect.left = 0
        if player_rect.right >= screen.get_width():
            player_rect.right = screen.get_width()
        if player_rect.top <= 0:
            player_rect.top = 0
        if player_rect.bottom >= screen.get_height():
            player_rect.bottom = screen.get_height()

        if player_rect.colliderect(coin_rect):
            counter = 5
            coin_rect.topleft = (-100, -100)
            player_score += 1

        screen.blit(player_surf, player_rect)

        # Coin logic
        #if coin_rect.x <= 0 or coin_rect.y <= 0 or coin_rect.x >= screen.get_width() or coin_rect.y >= screen.get_height():
        if coin_rect.left <= 0 or coin_rect.right >= 800 or coin_rect.top <= 0 or coin_rect.bottom >= 600:
            coin_rect.x = random.randint(0, screen.get_width())
            coin_rect.y = random.randint(0, screen.get_height())
        else:
            screen.blit(coin_surf, coin_rect)

        # Update timer and core
        score_text = score_font.render(f'score: {player_score}', True, 'white')
        timer_text = timer_font.render(f'timer: {counter}', True, 'white')

        # Draw timer and core
        screen.blit(score_text, score_rect)
        screen.blit(timer_text, timer_rect)

    else:
        screen.fill('white')
        score_text = score_font.render(f'score: {player_score}', True, 'black')

        screen.blit(gameover_text, gameover_rect)
        screen.blit(score_text, score_rect)


    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
