import pygame
import random
from pygame.locals import *
import time

def backgroundchanger(img):
    background=pygame.image.load(img)
    bg= pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(bg,(0,0))

pygame.init()
pygame.display.set_caption("Police or theif?")
screen_width=900
screen_height=700
screen=pygame.display.set_mode([screen_width,screen_height])
class Police (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("policeimg.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()

class OtherPolice(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("OtherPolicePic.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(20,20))
        self.rect=self.image.get_rect()

class Theif(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("theif.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(20,50))
        self.rect=self.image.get_rect()

allsprites=pygame.sprite.Group()
otherPolice_list=pygame.sprite.Group()
theif_list=pygame.sprite.Group()
for i in range(20):
    otherPolice=OtherPolice()
    otherPolice.rect.x=random.randrange(screen_width)
    otherPolice.rect.y=random.randrange(screen_height)
    otherPolice_list.add(otherPolice)
    allsprites.add(otherPolice)

for i in range(100):
    theif=Theif()
    theif.rect.x=random.randrange(screen_width)
    theif.rect.y=random.randrange(screen_height)
    theif_list.add(theif)
    allsprites.add(theif)

police=Police()
allsprites.add(police)
RED=(255,0,0)
WHITE=(255,255,255)
playing=True
score=0
clock=pygame.time.Clock()
start_time=time.time()
myFont=pygame.font.SysFont("Times New Roman",53)
timingFont=pygame.font.SysFont("Calibri Body",75)
text=myFont.render("Score =" + str(0),True,WHITE)

while playing:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    timeElapsed=time.time()-start_time
    if timeElapsed>=80:
        if score>=60:
            text=myFont.render("You won!Congrats",True,WHITE)
            changeBackground("Man_arrest.jpg")
        else:
            text=myFont.render("You lost!Better luck next time",True,RED)
            changeBackground("losescreen.jpg")
        screen.blit(text,(250,40))
    else:
        backgroundchanger("background1.jpg")
        countDown=timingFont.render(str(60-int(timeElapsed)),True,RED)
        screen.blit(countDown,(800,10))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if police.rect.y>0:
                police.rect.y-=5
        if keys[pygame.K_DOWN]:
            if police.rect.y<630:
                police.rect.y+=5
        if keys[pygame.K_LEFT]:
            if police.rect.x>0:
                police.rect.x-=5
        if keys[pygame.K_RIGHT]:
            if police.rect.x<850:
                police.rect.x+=5
        theif_hit_list=pygame.sprite.spritecollide(police,theif,True)
        otherPolice_hit_list=pygame.sprite.spritecollide(police,otherPolice,True)
        for theif in theif_hit_list:
            score+=1
            text=myFont.render("Score="+str(score),True,(0,0,0))
        for otherPolice in otherpolice_hit_list:
            score-=5
            text=myFont.render("Score="+str(score),True,(0,0,0))
        screen.blit(text,(700,80))
        allsprites.draw(screen)
    pygame.display.update()
pygame.quit()
        

    

