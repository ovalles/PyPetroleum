
import pygame

import time as time
from random import randint
import var
import functions


def well(x,y):   #Funcion que despliega el pozo en las coordenadas XY
    var.y=400 * 0.05
    var.ObjeSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.ObjeSurf.blit(wellImg,(x,y))


def plotcore(x,y):

    cropped = pygame.Surface((20, 280))    #crea una superficie
    cropped.blit(subImg, (0, 0), (x, 0, 20, 280))  #pega una porcion de otra sup en la sup creada
    var.CoreSurf.blit(cropped,(x,100))   #pega la superficie creada en la pantalla

    cropped = pygame.Surface((5, 280))    #crea una superficie
    cropped.blit(fluiImg, (0, 0), (x, 0, 5, 280))  #pega una porcion de otra sup en la sup creada
    var.FluiSurf.blit(cropped,(x,100))   #pega la superficie creada en la pantalla

    
def plotseis(x,y):  #Funcion que despliega la sismica adquirida
    global seisImg

    cropped = pygame.Surface((150, 280))
    cropped.blit(seisImg, (0, 0), (x-50, 0, 150, 280))
    var.SeisSurf.blit(cropped,(x-75,100))
    
    
def dist(xp,yp,x1,x2,y1,y2):   #Mide la distancia entre la mecha y el yacimiento

    xm=(x1+x2)/2.0
    ym=(y1+y2)/2.0
    distan=((xp-xm)**2+(yp-ym)**2)**(0.5)
    return distan



def game_loop():

    global wellImg, skyImg, seisImg, subImg, fluiImg 
    #global subImg, var.CoreSurf, fluiImg, var.FluiSurf, crashed
    

#CREANDO SUPERFICIES TRASPARENTES
    var.BackSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)  
    var.SeisSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.FluiSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.CoreSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.IndeSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.ProdSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.ObjeSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.HudiSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)

    wellImg = pygame.image.load('./010_demo/rig.png')
    wellImg = pygame.transform.scale(wellImg, (60, 80))


    skyImg = pygame.image.load('./010_demo/cielo.jpeg')
    skyImg = pygame.transform.scale(skyImg, (var.display_ancho, 100))
    var.BackSurf.blit(skyImg,(0,0))


    subImg = pygame.image.load('./010_demo/subsuelo.jpg')
    subImg = pygame.transform.scale(subImg, (var.display_ancho, 300))


    seisImg = pygame.image.load('./010_demo/subsuelo_seis.jpg')
    seisImg = pygame.transform.scale(seisImg, (var.display_ancho, 300))

    fluiImg = pygame.image.load('./010_demo/subsuelo_flui.png')
    fluiImg = pygame.transform.scale(fluiImg, (var.display_ancho, 300))



    IndeImg = pygame.image.load('./010_demo/subsuelo_index.png')
    IndeImg = pygame.transform.scale(IndeImg, (var.display_ancho, 300))
    var.IndeSurf.blit(IndeImg,(0,100))

    var.Budget_inic=370
    var.gameDisplay.fill(var.black)
    var.x = var.display_ancho*0.4

    var.y = 400 * 0.05
    crashed = False
    LEFT = 1

    startTime = time.time()

    var.x = randint(80, var.display_ancho-100)
    plotseis(var.x,var.y)

    var.x = randint(80, var.display_ancho-100)
    plotcore(var.x,var.y)

    var.x = randint(80, var.display_ancho-10)
    plotcore(var.x,var.y)


#POLIGONOS DE LOS YACIMIENTOS A B C


    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            #var.x, var.y = event.pos
       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    var.x += -5
                elif event.key == pygame.K_RIGHT:
                    var.x += 5
                elif event.key == pygame.K_DOWN:
                    plotcore(var.x,var.y)
                    var.costo += 50   # Se cobra el nucleo
                elif event.key == pygame.K_s:
                    plotseis(var.x,var.y)
                    var.costo +=100
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                i,j = event.pos
                if 75 < j < 100:
                    var.x = i
                elif 100 < j < 400:

                    alfa = var.IndeSurf.get_at((i,j))
                    print(alfa)    
                    var.costo += 20
                    pygame.draw.rect(var.ProdSurf,alfa,(i,100,5,j-100))
                    

            #print(event)
            #var.gameDisplay.blit(skyImg,(0,0))
            
            well(var.x,var.y)
            var.Budget = var.Budget_inic - var.costo + var.rate
           # functions.button("Seismic",10,var.HudiSurf,100,0,100,20,var.greenl,var.green,"Seismic")
            functions.button("Next Oilfield >>",10,var.HudiSurf,600,0,100,20,var.greenl,var.green,"Nextfield")
            
            elapsedTime = int(time.time() - startTime)
            functions.button("Budget: "+str(var.Budget)+" MMUSD",12, var.HudiSurf, 0,400,200,20,var.greenl,var.green,"None")
           # functions.button(str(var.rate) +" of 650 MMBls",12,var.HudiSurf, 300,400,200,20,var.greenl,var.green,"None")
           # functions.button(str(elapsedTime) +" of 250 weeks",12, var.HudiSurf, 600,400,200,20,var.greenl,var.green,"None")
            
            var.gameDisplay.blit(var.BackSurf,(0,0))
            var.gameDisplay.blit(var.SeisSurf,(0,0))
            
            var.gameDisplay.blit(var.CoreSurf,(0,0))
            var.gameDisplay.blit(var.FluiSurf,(0,0))
            var.gameDisplay.blit(var.ProdSurf,(0,0))
            var.gameDisplay.blit(var.ObjeSurf,(0,0))
            var.gameDisplay.blit(var.HudiSurf,(0,0))
            
            
            pygame.display.update()
            var.clock.tick(60)
