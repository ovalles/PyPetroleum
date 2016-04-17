import pygame
import time as time
from random import randint

def game_loop(display_ancho):

    global costo, wellImg, skyImg, seisImg, SeisSurf, ObjeSurf,x,y
    global subImg, CoreSurf, fluiImg, FluiSurf
    global display_ancho


#CREANDO SUPERFICIES TRASPARENTES
    BackSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)  
    SeisSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    FluiSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    CoreSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    ProdSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    #ObjeSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    HudiSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)

    wellImg = pygame.image.load('./010_demo/rig.png')
    wellImg = pygame.transform.scale(wellImg, (60, 80))

    skyImg = pygame.image.load('./010_demo/cielo.jpeg')
    skyImg = pygame.transform.scale(skyImg, (display_ancho, 100))
    BackSurf.blit(skyImg,(0,0))


    subImg = pygame.image.load('./010_demo/subsuelo.jpg')
    subImg = pygame.transform.scale(subImg, (display_ancho, 300))


    seisImg = pygame.image.load('./010_demo/subsuelo_seis.jpg')
    seisImg = pygame.transform.scale(seisImg, (display_ancho, 300))

    fluiImg = pygame.image.load('./010_demo/subsuelo_flui.png')
    fluiImg = pygame.transform.scale(fluiImg, (display_ancho, 300))


    Budget=370
    costo=0
    rate = 0
    gameDisplay.fill(black)
    x = display_ancho*0.4

    y = 400 * 0.05
    crashed = False
    LEFT = 1

    startTime = time.time()
    x = randint(20, display_ancho-100)
    plotseis(x,y)

    x = randint(20, display_ancho-100)
    plotcore(x,y)

    x = randint(20, display_ancho-10)
    plotcore(x,y)


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
                crashed = True
       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x += -5
                elif event.key == pygame.K_RIGHT:
                    x += 5
                elif event.key == pygame.K_DOWN:
#                    cropped = pygame.Surface((20, 280))    #crea una superficie
#                    cropped.blit(subImg, (0, 0), (x, 0, 20, 280))  #pega una porcion de otra sup en la sup creada
#                   CoreSurf.blit(cropped,(x,100))   #pega la superficie creada en la pantalla

#                    cropped = pygame.Surface((5, 280))    #crea una superficie
#                    cropped.blit(fluiImg, (0, 0), (x, 0, 5, 280))  #pega una porcion de otra sup en la sup creada
#                    FluiSurf.blit(cropped,(x,100))   #pega la superficie creada en la pantalla
                    plotcore(x,y)
                    costo += 50   # Se cobra el nucleo
                elif event.key == pygame.K_s:
                    plotseis(x,y)
                    costo +=100
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                i,j = event.pos
                if 75 < j < 100:
                    x = i
                elif 100 < j < 400:
                    closest=min(dist(i,j,rax1,rax2,ray1,ray2),dist(i,j,rbx1,rbx2,rby1,rby2),dist(i,j,rcx1,rcx2,rcy1,rcy2))

                    if closest < 75:
                        alfa = (255,255,0)
                    else:
                        alfa = (255,0,0)
                    
                    if rax1 < i < rax2 and ray1 < j < ray2:
                        reser=150
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
                    

                    pygame.draw.rect(ProdSurf,alfa,(i,100,5,j-100))
                    #pygame.draw.rect(gameDisplay,(255,255,255),(i,100,5,j-100))

            #print(event)
            #gameDisplay.blit(skyImg,(0,0))
            well(x,y)

            button("Seismic",10,HudiSurf,600,0,100,20,greenl,green,"Seismic")
            
            elapsedTime = int(time.time() - startTime)
            button("Budget: "+str(Budget-costo+rate)+" MMUSD",12, HudiSurf, 0,400,200,20,greenl,green,"None")
            button(str(rate) +" of 650 MMBls",12,HudiSurf, 300,400,200,20,greenl,green,"None")
            button(str(elapsedTime) +" of 250 weeks",12, HudiSurf, 600,400,200,20,greenl,green,"None")
            
            gameDisplay.blit(BackSurf,(0,0))
            gameDisplay.blit(SeisSurf,(0,0))
            gameDisplay.blit(CoreSurf,(0,0))
            gameDisplay.blit(FluiSurf,(0,0))
            gameDisplay.blit(ProdSurf,(0,0))
            gameDisplay.blit(ObjeSurf,(0,0))
            gameDisplay.blit(HudiSurf,(0,0))
            
            
            pygame.display.update()
            clock.tick(60)
