
import pygame

import time as time
from random import randint
import var
import functions


def game_loop():

    #global costo, var.Budget, wellImg, skyImg, seisImg, var.SeisSurf, ObjeSurf,var.x,var.y
    #global subImg, var.CoreSurf, fluiImg, var.FluiSurf, crashed


#CREANDO SUPERFICIES TRASPARENTES
    var.BackSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)  
    var.SeisSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.FluiSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.CoreSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    var.ProdSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
    #ObjeSurf = pygame.Surface([var.display_ancho, var.display_alto], pygame.SRCALPHA, 32)
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


#    var.Budget=370
    costo=0
    rate = 0
    var.gameDisplay.fill(var.black)
    var.x = var.display_ancho*0.4

    var.y = 400 * 0.05
    crashed = False
    LEFT = 1

    startTime = time.time()
    var.x = randint(20, var.display_ancho-100)
    plotseis(var.x,var.y)

    var.x = randint(20, var.display_ancho-100)
    plotcore(var.x,var.y)

    var.x = randint(20, var.display_ancho-10)
    plotcore(var.x,var.y)


#POLIGONOS DE LOS YACIMIENTOS A B C
    rax1=40
    rax2=207
    ray1=235
    ray2=250

    rbx1=182
    rbx2=258
    rby1=288
    rby2=318

    rcx1=670
    rcx2=750
    rcy1=180
    rcy2=210
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                crashed = True
       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    var.x += -5
                elif event.key == pygame.K_RIGHT:
                    var.x += 5
                elif event.key == pygame.K_DOWN:
                    plotcore(var.x,var.y)
                    costo += 50   # Se cobra el nucleo
                elif event.key == pygame.K_s:
                    plotseis(var.x,var.y)
                    costo +=100
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                i,j = event.pos
                if 75 < j < 100:
                    var.x = i
                elif 100 < j < 400:
                    closest=min(dist(i,j,rax1,rax2,ray1,ray2),dist(i,j,rbx1,rbx2,rby1,rby2),dist(i,j,rcx1,rcx2,rcy1,rcy2))

                    if closest < 75:
                        alfa = (255,255,0)
                    else:
                        alfa = (255,0,0)
                    
                    if rax1 < i < rax2 and ray1 < j < ray2:
                        rate += 150
                        alfa=(0,255,0)
                    elif rbx1 < i < rbx2 and rby1 < j < rby2:
                        rate += 300
                        alfa=(0,255,0)
                    elif rcx1 < i < rcx2 and rcy1 < j < rcy2:
                        rate += 200
                        alfa=(0,255,0)
                    else:
                        costo +=20
                    

                    pygame.draw.rect(var.ProdSurf,alfa,(i,100,5,j-100))
                    #pygame.draw.rect(var.gameDisplay,(255,255,255),(i,100,5,j-100))

            #print(event)
            #var.gameDisplay.blit(skyImg,(0,0))
            well(var.x,var.y)


            functions.button("Seismic",10,var.HudiSurf,100,0,100,20,var.greenl,var.green,"Seismic")
            functions.button("Next Oilfield",10,var.HudiSurf,600,0,100,20,var.greenl,var.green,"Nextfield")
          
            elapsedTime = int(time.time() - startTime)
            functions.button("Budget: "+str(Budget-costo+rate)+" MMUSD",12, var.HudiSurf, 0,400,200,20,var.greenl,var.green,"None")
            functions.button(str(rate) +" of 650 MMBls",12,var.HudiSurf, 300,400,200,20,var.greenl,var.green,"None")
            functions.button(str(elapsedTime) +" of 250 weeks",12, var.HudiSurf, 600,400,200,20,var.greenl,var.green,"None")
            
            var.gameDisplay.blit(var.BackSurf,(0,0))
            var.gameDisplay.blit(var.SeisSurf,(0,0))
            var.gameDisplay.blit(var.CoreSurf,(0,0))
            var.gameDisplay.blit(var.FluiSurf,(0,0))
            var.gameDisplay.blit(var.ProdSurf,(0,0))
            var.gameDisplay.blit(ObjeSurf,(0,0))
            var.gameDisplay.blit(var.HudiSurf,(0,0))
            
            
            pygame.display.update()
            clock.tick(60)

############################
