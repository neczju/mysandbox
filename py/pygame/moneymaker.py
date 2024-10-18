# moneymaker.py -- simple coin getting game
import pygame
import random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))
running = True
playerpos = pygame.Vector2((screen.get_width() / 2, screen.get_height() / 2))
coinpos = pygame.Vector2(random.randint(0, screen.get_width()),
                         random.randint(0, screen.get_height()))
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')

    pygame.draw.circle(screen, 'yellow', coinpos, 10)
    pygame.draw.circle(screen, 'red', playerpos, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerpos.y -= 300 * dt
    if keys[pygame.K_s]:
        playerpos.y += 300 * dt
    if keys[pygame.K_a]:
        playerpos.x -= 300 * dt
    if keys[pygame.K_d]:
        playerpos.x += 300 * dt

    dt = clock.tick(60) / 1000
    pygame.display.flip()

pygame.quit()