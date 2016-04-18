import pygame
import time as time
from random import randint
import var
import map


def text_objects(text, font):
    textSurface = font.render(text, True, var.black)
    return textSurface, textSurface.get_rect()

def button(msg,font_size,Surface,xpos,ypos,w,h,ic,ac,action=None):
    #global HudiSurf, costo, Budget, crashed
    mouse = pygame.mouse.get_pos()   #meto en una lista la posicion del mouse
    click = pygame.mouse.get_pressed()
    crashed = False
    if xpos+w > mouse[0] > xpos and ypos+h > mouse[1] >ypos:
        pygame.draw.rect(Surface, ac, (xpos,ypos,w,h))
        if click[0] == 1 and action != None:
            if action == "Play":
                map.map()
                
            elif action == "Quit":
                pygame.quit()
                quit()
            elif action =="Seismic":
                plotseis(x,y)
                costo += 100

            elif action == "Nextfield":
                crashed = True

    else:
        pygame.draw.rect(Surface, ic, (xpos,ypos,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",font_size)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((xpos + (w/2)),(ypos + (h/2)))
    Surface.blit(textSurf, textRect)

    return crashed






