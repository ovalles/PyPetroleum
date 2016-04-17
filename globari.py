import pygame


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
redl=(200,0,0)
greenl = (0,200,0)
green=(0,255,0)
display_ancho = 800
display_alto = 420
x=0
y=0


BackSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)  
SeisSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
FluiSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
CoreSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
ProdSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
HudiSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)



Budget=370
costo=0
rate = 0
