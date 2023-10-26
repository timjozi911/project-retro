import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('NeoZa game')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
    