import pygame

import time as time
from random import randint
import var
import functions


pygame.init()
#var.black = (0,0,0)
#var.white = (255,255,255)
#var.red = (255,0,0)
#var.redl=(200,0,0)
#var.greenl = (0,200,0)
#var.green=(0,255,0)
#var.display_ancho = 800
#var.display_alto = 420
#var.x=0
#var.y=0
#var.gameDisplay = pygame.display.set_mode((var.display_ancho,var.display_alto))
pygame.display.set_caption('PyTroleo by AJ Ovalles 2016')
#clock = pygame.time.Clock()

var.gameDisplay.fill(var.white)

    


def game_intro():
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        var.gameDisplay.fill(var.white)
        WelcomeImg = pygame.image.load('./003_Welcome/intro3pic.png')
        var.gameDisplay.blit(WelcomeImg,(0,0))
        #largeText = pygame.font.Font('freesansbold.ttf',60)
        #TextSurf, TextRect = functions.text_objects("PyTroleo", largeText)
        #TextRect.center = ((var.display_ancho/2),(var.display_alto/2))
        #var.gameDisplay.blit(TextSurf,TextRect)
        #functions.button("PyPetrol",80, var.gameDisplay,350,150,100,50,var.white,var.white,"None")
        functions.button("Play",20, var.gameDisplay,220,350,100,50,
                         var.greenl,var.green,"Play")

        functions.button("Quit",20,var.gameDisplay,500,350,100,50,
                         var.redl,var.red,"Quit")

        #functions.button("by AJ Ovalles",16, var.gameDisplay,300,50,200,50,var.white,var.white,"None")
        pygame.display.update()
#        clock.tick(20)





            
    


#############################
############################ ESCENARIO 2 DEFORMED  ########################################
#
game_intro()
pygame.quit()
quit()
