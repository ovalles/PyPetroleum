import pygame

import time as time
from random import randint



pygame.init()
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
gameDisplay = pygame.display.set_mode((display_ancho,display_alto))
pygame.display.set_caption('PyTroleo by AJ Ovalles 2016')
clock = pygame.time.Clock()

gameDisplay.fill(white)




def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,font_size,Surface,xpos,ypos,w,h,ic,ac,action=None):
    global HudiSurf, costo, Budget, crashed
    mouse = pygame.mouse.get_pos()   #meto en una lista la posicion del mouse
    click = pygame.mouse.get_pressed()

    if xpos+w > mouse[0] > xpos and ypos+h > mouse[1] >ypos:
        pygame.draw.rect(Surface, ac, (xpos,ypos,w,h))
        if click[0] == 1 and action != None:
            if action == "Play":
                map()
                
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
    


def game_intro():
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("PyTroleo", largeText)
        TextRect.center = ((display_ancho/2),(display_alto/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Play",20, gameDisplay,150,300,100,50,greenl,green,"Play")

        button("Quit",20,gameDisplay,450,300,100,50,redl,red,"Quit")

        button("by AJ Ovalles",16, gameDisplay,300,50,200,50,white,white,"None")
        pygame.display.update()
#        clock.tick(20)


def map():
    
    #global crashed
    mapImg = pygame.image.load('./005_world/worldmap_1.png')
    #mapImg = pygame.transform.scale(mapImg, (display_ancho, display_alto))
    gameDisplay.blit(mapImg,(0,0))
    mapImg_ven = pygame.image.load('./005_world/worldmap_ven.png')
    #mapImg_ven = pygame.transform.scale(mapImg_ven, (display_ancho, display_alto))
    
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
                gameDisplay.blit(mapImg_ven,(0,0))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    #game_loop()
                    anticline()
                    game_loop()
                    anticline()
                    
            else:
                gameDisplay.blit(mapImg,(0,0))

        pygame.display.update()
#        clock.tick(40)


def well(x,y):   #Funcion que despliega el pozo en las coordenadas XY
    global ObjeSurf
    y=400 * 0.05
    ObjeSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    ObjeSurf.blit(wellImg,(x,y))

def plotcore(x,y):

    

    cropped = pygame.Surface((20, 280))    #crea una superficie
    cropped.blit(subImg, (0, 0), (x, 0, 20, 280))  #pega una porcion de otra sup en la sup creada
    CoreSurf.blit(cropped,(x,100))   #pega la superficie creada en la pantalla

    cropped = pygame.Surface((5, 280))    #crea una superficie
    cropped.blit(fluiImg, (0, 0), (x, 0, 5, 280))  #pega una porcion de otra sup en la sup creada
    FluiSurf.blit(cropped,(x,100))   #pega la superficie creada en la pantalla
    
def plotseis(x,y):  #Funcion que despliega la sismica adquirida


    global SeisSurf
    cropped = pygame.Surface((150, 280))
    cropped.blit(seisImg, (0, 0), (x-50, 0, 150, 280))
    SeisSurf.blit(cropped,(x-75,100))
    
    
def dist(xp,yp,x1,x2,y1,y2):   #Mide la distancia entre la mecha y el yacimiento

    xm=(x1+x2)/2.0
    ym=(y1+y2)/2.0
    distan=((xp-xm)**2+(yp-ym)**2)**(0.5)
    return distan


############################ ESCENARIO 1 ANTICLINE ########################################
def anticline():

    global costo, Budget, wellImg, skyImg, seisImg, SeisSurf, ObjeSurf,x,y
    global subImg, CoreSurf, fluiImg, FluiSurf, crashed


#CREANDO SUPERFICIES TRASPARENTES
    BackSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)  
    SeisSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    FluiSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    CoreSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    IndeSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    ProdSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    #ObjeSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)
    HudiSurf = pygame.Surface([display_ancho, display_alto], pygame.SRCALPHA, 32)

    wellImg = pygame.image.load('./010_demo/rig.png')
    wellImg = pygame.transform.scale(wellImg, (60, 80))

    skyImg = pygame.image.load('./010_demo/cielo.jpeg')
    skyImg = pygame.transform.scale(skyImg, (display_ancho, 100))
    BackSurf.blit(skyImg,(0,0))


    subImg = pygame.image.load('./015_anticline/anticline.png')
    subImg = pygame.transform.scale(subImg, (display_ancho, 300))


    seisImg = pygame.image.load('./015_anticline/anticlineSeis.png')
    seisImg = pygame.transform.scale(seisImg, (display_ancho, 300))

    fluiImg = pygame.image.load('./015_anticline/anticlineflui.png')
    fluiImg = pygame.transform.scale(fluiImg, (display_ancho, 300))

    IndeImg = pygame.image.load('./015_anticline/anticline_index.png')
    IndeImg = pygame.transform.scale(IndeImg, (display_ancho, 300))
    IndeSurf.blit(IndeImg,(0,100))

    Budget_inic=370
    costo=0
    rate = 0
    gameDisplay.fill(black)
    x = display_ancho*0.4

    y = 400 * 0.05
    crashed = False
    LEFT = 1

    startTime = time.time()

    x = randint(80, display_ancho-100)
    plotseis(x,y)

    x = randint(80, display_ancho-100)
    plotcore(x,y)

    x = randint(80, display_ancho-10)
    plotcore(x,y)


#POLIGONOS DE LOS YACIMIENTOS A B C


    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            #x, y = event.pos
       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x += -5
                elif event.key == pygame.K_RIGHT:
                    x += 5
                elif event.key == pygame.K_DOWN:
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

                    alfa = IndeSurf.get_at((i,j))
                    print(alfa)    

                    pygame.draw.rect(ProdSurf,alfa,(i,100,5,j-100))
                    

            #print(event)
            #gameDisplay.blit(skyImg,(0,0))
            
            well(x,y)
            Budget = Budget_inic - costo + rate
           # button("Seismic",10,HudiSurf,100,0,100,20,greenl,green,"Seismic")
            button("Next Oilfield >>",10,HudiSurf,600,0,100,20,greenl,green,"Nextfield")
            
            elapsedTime = int(time.time() - startTime)
            button("Budget: "+str(Budget)+" MMUSD",12, HudiSurf, 0,400,200,20,greenl,green,"None")
           # button(str(rate) +" of 650 MMBls",12,HudiSurf, 300,400,200,20,greenl,green,"None")
           # button(str(elapsedTime) +" of 250 weeks",12, HudiSurf, 600,400,200,20,greenl,green,"None")
            
            gameDisplay.blit(BackSurf,(0,0))
            gameDisplay.blit(SeisSurf,(0,0))
            
            gameDisplay.blit(CoreSurf,(0,0))
            gameDisplay.blit(FluiSurf,(0,0))
            gameDisplay.blit(ProdSurf,(0,0))
            gameDisplay.blit(ObjeSurf,(0,0))
            gameDisplay.blit(HudiSurf,(0,0))
            
            
            pygame.display.update()
            clock.tick(60)
            
    


#############################
############################ ESCENARIO 2 DEFORMED  ########################################
def game_loop():

    global costo, Budget, wellImg, skyImg, seisImg, SeisSurf, ObjeSurf,x,y
    global subImg, CoreSurf, fluiImg, FluiSurf, crashed


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


#    Budget=370
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
                pygame.quit()
                quit()
                crashed = True
       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x += -5
                elif event.key == pygame.K_RIGHT:
                    x += 5
                elif event.key == pygame.K_DOWN:
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


            button("Seismic",10,HudiSurf,100,0,100,20,greenl,green,"Seismic")
            button("Next Oilfield",10,HudiSurf,600,0,100,20,greenl,green,"Nextfield")
          
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

#############################
game_intro()
pygame.quit()
quit()
