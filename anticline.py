
import pygame

import time as time
from random import randint
import var
import functions
import numpy as np
import classifier as clasi

def well(x,y):   #Funcion que despliega el pozo en las coordenadas XY
    y= 10
    var.ObjeSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.ObjeSurf.blit(wellImg,(x-30,y))


def plotcore(x,y):

    if user_action == 1:
        pygame.mixer.music.load('./70_SOUNDS/Core.mp3')
        pygame.mixer.music.play(0)
        pygame.time.wait(2000)

    cropped = pygame.Surface((20, 280))    #crea una superficie
    cropped.blit(subImg, (0, 0), (x, 0, 20, 280))  #pega una porcion de otra sup en la sup creada
    var.CoreSurf.blit(cropped,(x,100))   #pega la superficie creada en la pantalla

    cropped = pygame.Surface((5, 280))    #crea una superficie
    cropped.blit(fluiImg, (0, 0), (x, 0, 5, 280))  #pega una porcion de otra sup en la sup creada
    var.FluiSurf.blit(cropped,(x,100))   #pega la superficie creada en la pantalla



    
def plotseis(x,y):  #Funcion que despliega la sismica adquirida
    global seisImg

    if user_action == 1:
        pygame.mixer.music.load('./70_SOUNDS/Seismic.mp3')
        pygame.mixer.music.play(0)
        pygame.time.wait(500)

    cropped = pygame.Surface((150, 280))
    cropped.blit(seisImg, (0, 0), (x-50, 0, 150, 280))
    var.SeisSurf.blit(cropped,(x-75,100))
    
    
def dist(xp,yp,x1,x2,y1,y2):   #Mide la distancia entre la mecha y el yacimiento

    xm=(x1+x2)/2.0
    ym=(y1+y2)/2.0
    distan=((xp-xm)**2+(yp-ym)**2)**(0.5)
    return distan



def anticline():

    global wellImg, skyImg, seisImg, subImg, fluiImg, user_action 
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
    wellImg = pygame.transform.scale(wellImg, (80, 100))

    skyImg = pygame.image.load('./010_demo/cielo.jpeg')
    skyImg = pygame.transform.scale(skyImg, (var.display_ancho, 100))
    var.BackSurf.blit(skyImg,(0,0))


    subImg = pygame.image.load('./015_anticline/anticline.png')
    subImg = pygame.transform.scale(subImg, (var.display_ancho, 300))


    seisImg = pygame.image.load('./015_anticline/anticlineSeis.png')
    seisImg = pygame.transform.scale(seisImg, (var.display_ancho, 300))

    fluiImg = pygame.image.load('./015_anticline/anticlineflui.png')
    fluiImg = pygame.transform.scale(fluiImg, (var.display_ancho, 300))

    IndeImg = pygame.image.load('./015_anticline/anticline_index.png')
    IndeImg = pygame.transform.scale(IndeImg, (var.display_ancho, 300))
    var.IndeSurf.blit(IndeImg,(0,100))

    var.Budget_inic=370
    var.gameDisplay.fill(var.black)
    var.x = var.display_ancho*0.4

    var.y = 400 * 0.05
    crashed = False
    LEFT = 1
    user_action = 0
    ifconter = 0
    pick =np.array([[0,0]])
    startTime = time.time()

    var.x = randint(80, var.display_ancho-100)
    plotseis(var.x,var.y)

    var.x = randint(80, var.display_ancho-100)
    plotcore(var.x,var.y)

    pygame.time.wait(27)

    var.x = randint(80, var.display_ancho-10)
    plotcore(var.x,var.y)


#POLIGONOS DE LOS YACIMIENTOS A B C


    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
		quit()
       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    var.x += -5
                elif event.key == pygame.K_RIGHT:
                    var.x += 5
                elif event.key == pygame.K_DOWN:
                    user_action = 1
                    plotcore(var.x,var.y)
                    var.costo += 50   # Se cobra el nucleo
                elif event.key == pygame.K_s:
                    user_action = 1
                    plotseis(var.x,var.y)
                    var.costo +=100
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                i,j = event.pos
                if 75 < j < 100:
                    var.x = i
                elif 100 < j < 400:

                    alfa = var.IndeSurf.get_at((i,j))
                    #print(alfa)    
                    var.costo += 15
                    pygame.draw.rect(var.ProdSurf,alfa,(i,100,5,j-100))
                    
                    if alfa == (0, 255, 0, 255):
                        ifconter = ifconter+1
                        picknew = [i,j]
                        pick = np.vstack([pick, picknew])
                        #print 'Pick location',pick, ifconter
                        densWell = clasi.hiercluscounter(pick[1:,:],4)
                        print 'Weel Density :',densWell
                        
                        #sound = pygame.mixer.Sound("./70_SOUNDS/Cash.mp3")
                        #sound.play(maxtime = 1000000)
                        pygame.mixer.music.load('./70_SOUNDS/Cash.mp3')
                        pygame.mixer.music.play(0)
                        var.rate += 100*(1.0/densWell)
                        print var.rate

                    else:
                        pygame.mixer.music.load('./70_SOUNDS/Error.mp3')
                        pygame.mixer.music.play(0)

            #print(event)
            #var.gameDisplay.blit(skyImg,(0,0))
            
            well(var.x,var.y)
            var.Budget = int(var.Budget_inic - var.costo + var.rate)
           # functions.button("Seismic",10,var.HudiSurf,
                             #100,0,100,20,var.greenl,var.green,"Seismic")
            crashed = functions.button("Next Oilfield >>",10,var.HudiSurf,
                                       600,0,100,20,var.greenl,var.green,"Nextfield")
            
            elapsedTime = int(time.time() - startTime)
            functions.button("Budget: "+str(var.Budget)+" MMUSD",
                             12, var.HudiSurf, 0,400,200,20,var.greenl,var.green,"None")
           # functions.button(str(var.rate) +" of 650 MMBls",
                            # 12,var.HudiSurf, 300,400,200,20,var.greenl,var.green,"None")
           # functions.button(str(elapsedTime) +" of 250 weeks",
                             #12, var.HudiSurf, 600,400,200,20,var.greenl,var.green,"None")
            
            var.gameDisplay.blit(var.BackSurf,(0,0))
            var.gameDisplay.blit(var.SeisSurf,(0,0))
            
            var.gameDisplay.blit(var.CoreSurf,(0,0))
            var.gameDisplay.blit(var.FluiSurf,(0,0))
            var.gameDisplay.blit(var.ProdSurf,(0,0))
            var.gameDisplay.blit(var.ObjeSurf,(0,0))
            var.gameDisplay.blit(var.HudiSurf,(0,0))
            
            
            pygame.display.update()
            var.clock.tick(60)
