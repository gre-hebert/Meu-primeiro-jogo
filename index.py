import pygame
import random

pygame.init()
pygame.display.set_caption('Meu jogo')
tela = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                quit()
    pass