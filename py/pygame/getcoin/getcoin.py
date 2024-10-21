import pygame
from pathlib import Path
import random

def score_display(color):
    score_text = score_font.render(f'coins: {player_score}', True, color)
    score_rect = score_text.get_rect(topleft = (0, 0))
    screen.blit(score_text, score_rect)
    
def timer_display():
    timer_text = timer_font.render(f'timer: {counter}', True, 'white')
    timer_rect = timer_text.get_rect(topleft = (0, 40))
    screen.blit(timer_text, timer_rect)

def pickupcoin_sfx():
    pygame.mixer.music.load(Path('audio/pickupcoin.wav'))
    pygame.mixer.music.play()

def gameover_sfx():
    pygame.mixer.music.load(Path('audio/explosion.wav'))
    pygame.mixer.music.play()

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('getcoin!')
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

# Coin
player_score = 0
coin_surf = pygame.image.load(Path('assets/coin_sprite.png')).convert_alpha()
coin_rect = coin_surf.get_rect(topleft = (-100, -100))

# Timer
game_active = True
counter = 5
pygame.time.set_timer(pygame.USEREVENT, 1000)
timer_text = timer_font.render(f'timer: {counter}', True, 'white')

# Game over
gameover_font = pygame.font.Font(Path('fonts/Roboto-Regular.ttf'), 50)
gameover_text = gameover_font.render('GAME OVER!', True, 'black')
gameover_rect = gameover_text.get_rect(center = (400, 300))

while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.USEREVENT:
            counter -= 1
            if counter == 0:
                gameover_sfx()
                game_active = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_active:
            game_active = True
            counter = 5
            player_score = 0
            coin_rect = coin_surf.get_rect(topleft = (-100, -100))
            player_rect = player_surf.get_rect(center = (screen.get_width() / 2, screen.get_height() / 2))

            

    if game_active:
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
            pickupcoin_sfx()
            coin_rect.topleft = (-100, -100)
            player_score += 1

        screen.blit(player_surf, player_rect)

        # Coin logic
        if coin_rect.left <= 0 or coin_rect.right >= 800 or coin_rect.top <= 0 or coin_rect.bottom >= 600:
            coin_rect.x = random.randint(0, screen.get_width())
            coin_rect.y = random.randint(0, screen.get_height())
        else:
            screen.blit(coin_surf, coin_rect)

        # Update timer and core
        score_display('white')
        timer_display()

        # Draw timer and core


    else:
        screen.fill('white')
        score_display('black')
        screen.blit(gameover_text, gameover_rect)


    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
