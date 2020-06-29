import pygame
from pygame.locals import *
from pygame import font


pygame.init()
pygame.font.init()
#Constants
menuSize=(1080,564)
gameSize=(500,700)

#colors
rosadito=(240,178,151)
Marine=(15,127,133,52)
Blue=(13,200,209,82)
Black=(20,20,20,0)
Gold=(209,189,79,82)
Purple=(133,8,89,52)
##fuente=pygame.font.Font("Hey Kiddo demo.ttf",15)
Font_title= pygame.font.Font("Fonts/28 Days Later.ttf",80)


def Text_Boxes(text,font,color):# This functions creates text boxes, with diferent colors and fonts
    text_box=font.render(text,True,color)
    return text_box,text_box.get_rect()#return the text and the rectagule



def MainMenu():
    main = pygame.display.set_mode((menuSize))
    pygame.display.set_caption("Proyecto Progra")
    pygame.display.flip()
    
    def Button(text,x,y,w,h,bg,activebg,font,action=None):#This function creates buttons
        mouse= pygame.mouse.get_pos()
        press=pygame.mouse.get_pressed()
        pygame.draw.rect(main,bg,(x,y,w,h))
        
        if x+w>mouse[0]>x and y+h>mouse[1]>y:#Verifies if the mouse is over the button
            pygame.draw.rect(main,activebg,(x,y,w,h))
                    
            if press[0]==1 and action!=None:# this line return the function of the button, when the button is pressed 
                action()
        else:
            pygame.draw.rect(main,bg,(x,y,w,h))
            
        letter,box=Text_Boxes(text,font,Black)
        box.center=((x+(w//2)),(y+(h//2)))
        main.blit(letter,box)

    main.fill(rosadito)
    
    
    def buttons():
        Button("Play",100,30,170,100,Marine,Gold,Font_title,Game)
        
    closeWindow = True
    while closeWindow:
        buttons()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEMOTION:
                pos=pygame.mouse.get_pos()
        pygame.display.update()


        
def Game():
    screen = pygame.display.set_mode((gameSize))
    pygame.display.set_caption("TRPONE")
    pygame.display.flip()
    screen.fill(Purple)
    
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MainMenu()
        pygame.display.update()


        
MainMenu()

#Hola
