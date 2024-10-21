import pygame
import shelve
from pathlib import Path
import sys

pygame.init()

screen_size = pygame.Vector2(640, 480)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('pet bulbasaur!')
clock = pygame.time.Clock()
running = True

game_font = pygame.font.Font(Path('font/Roboto-Regular.ttf'), 30)

bulb_surf = pygame.image.load(Path('assets/bulb.png')).convert_alpha()
bulb_rect = bulb_surf.get_rect(center = (320, 240))

if sys.platform == 'linux':
    if not Path('counter').exists():
        counterFile = shelve.open('counter')
        counterFile['counter'] = 0
    else:
        counterFile = shelve.open('counter')
elif sys.platform == 'win32':
    if not Path('counter.dat').exists():
        counterFile = shelve.open('counter')
        counterFile['counter'] = 0
    else:
        counterFile = shelve.open('counter')

counter_surf = game_font.render(f'pet counter: {counterFile['counter']}', True, 'white')
counter_rect = counter_surf.get_rect(topleft = (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP: 
            mouse_pos = pygame.mouse.get_pos()
            if bulb_rect.collidepoint(mouse_pos) and event.button == 1:
                counterFile['counter'] += 1
                counter_surf = game_font.render(f'pet counter: {counterFile['counter']}', True, 'white')


    screen.fill('black')
    screen.blit(counter_surf, counter_rect)
    screen.blit(bulb_surf, bulb_rect)

    clock.tick(60)
    pygame.display.update()

counterFile.close()
pygame.quit()
