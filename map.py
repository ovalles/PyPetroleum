import pygame

import time as time
from random import randint
import var
import functions

import anticline
import game_loop 

def map():
    
    mapImg = pygame.image.load('./005_world/worldmap_1.png')
    #mapImg = pygame.transform.scale(mapImg, (var.display_ancho, var.display_alto))
    var.gameDisplay.blit(mapImg,(0,0))
    mapImg_ven = pygame.image.load('./005_world/worldmap_ven.png')
    #mapImg_ven = pygame.transform.scale(mapImg_ven, (var.display_ancho, var.display_alto))
    
    crashed = False
    LEFT = 1

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            mouse = pygame.mouse.get_pos()   #meto en una lista la posicion del mouse
            click = pygame.mouse.get_pressed()    

#            if event.type == pygame.MOUSEMOTION:
#                i,j = event.pos

            if 206 < mouse[0] < 239 and 232 < mouse[1] <259:

                pygame.mixer.music.load('./70_SOUNDS/Click.mp3')
                pygame.mixer.music.play(0)

                var.gameDisplay.blit(mapImg_ven,(0,0))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    
                    #CARGO EL PRIMER ESCENARIO
                    budget = anticline.anticline(var.Budget_inic)

                    #CARGO EL SEGUNDO ESCENARIO
                    game_loop.game_loop()

                    #CARGO EL TERCER ESCENARIO
                    budget = anticline.anticline(budget)
                    
            else:
                var.gameDisplay.blit(mapImg,(0,0))

        pygame.display.update()
#        clock.tick(40)
