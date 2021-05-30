import pygame
import time
import os

pygame.init()

screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Message from "my boss"')
myFont=pygame.font.SysFont("Times New Roman",20)
label=myFont.render("you are fired you idiot",1,(255,0,0))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            time.sleep(0.10)

            screen=pygame.display.set_mode((1000,1000))
            pygame.display.set_caption('Message from"my boss"')
    screen.fill((255,255,255))
    screen.blit(label,(50,50))

    pygame.display.update()
