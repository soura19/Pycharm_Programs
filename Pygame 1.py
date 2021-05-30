import pygame

pygame.init()

screen=pygame.display.set_mode([600,600])

RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

pygame.draw.rect(screen,RED,(50,20,120,100))
pygame.draw.rect(screen,BLUE,(100,60,200,250))
pygame.draw.rect(screen,GREEN,(260,200,150,100))

pygame.display.update()
