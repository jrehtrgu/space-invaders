#space invaders
import pygame
import os
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space shooter tutorial")

#Load(descargar) images
FUEGO_AZUL = pygame.image.load(os.path.join("img", "fuego azul.png"))

#Player ship
NAVE = pygame.image.load(os.path.join("img", "nave.png"))

#Laser
FUEGO_ROJO = pygame.image.load(os.path.join("img", "fuego.png"))

#Fundo
BG = pygame.image.load(os.path.join("img", "fondo.jpg"))

class ship:
    def_init_(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.sh


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("timesnweroman", 40)
    
    clock = pygame.time.Clock()
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        #draw tex
        lives_label = main_font.render(f"Level: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"level: {level}", 1, (255,255,255))
        
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        
        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()