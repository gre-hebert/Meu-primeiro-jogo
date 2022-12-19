import pygame
import random

pygame.init()
pygame.display.set_caption('Meu jogo')
tela = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            quit()
    pass