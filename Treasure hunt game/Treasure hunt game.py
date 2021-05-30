import pygame
import random
from pygame.locals import *
import time

def changeBackground(img):
    background=pygame.image.load(img)
    bg= pygame.transform.scale(background,(screen_width,screen_height)) 
    screen.blit(bg,(0,0))

pygame.init()
pygame.display.set_caption("Treasure Hunt")
screen_width=900
screen_height=700
screen=pygame.display.set_mode([screen_width,screen_height])
class Pirate (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("pirate.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()
class Stone(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(20,20))
        self.rect=self.image.get_rect()
 
class Soldier (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("soldier.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(20,50))
        self.rect=self.image.get_rect()


images=["stone1.png","stone2.png","stone3.png"]
stone_list=pygame.sprite.Group()

allsprites=pygame.sprite.Group()
soldier_list=pygame.sprite.Group()
for i in range(100):
    stone=Stone(random.choice(images))
    stone.rect.x=random.randrange(screen_width)
    stone.rect.y=random.randrange(screen_height)
    stone_list.add(stone)
    allsprites.add(stone)
for i in range(20):
    soldier=Soldier()
    soldier.rect.x=random.randrange(screen_width)
    soldier.rect.y=random.randrange(screen_height)
    soldier_list.add(soldier)
    allsprites.add(soldier)
pirate=Pirate()
allsprites.add(pirate)
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
    clock.tick(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    timeElapsed=time.time()-start_time
    if timeElapsed>=60:
        if score>=40:
            text=myFont.render("You won!Congrats",True,RED)
            changeBackground("winscreen.jpg")
        
        else:
            text=myFont.render("You lost!Better luck next time",True,RED)
            changeBackground("losescreen.jpg")
        screen.blit(text,(250,40))
    else:
        
        changeBackground("b1.jpg")
        countDown=timingFont.render(str(60-int(timeElapsed)),True,RED)
        screen.blit(countDown,(800,10))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if pirate.rect.y>0:
                pirate.rect.y-=5
        if keys[pygame.K_DOWN]:
            if pirate.rect.y<630:
                pirate.rect.y+=5
        if keys[pygame.K_LEFT]:
            if pirate.rect.x>0:
                pirate.rect.x-=5
        if keys[pygame.K_RIGHT]:
            if pirate.rect.x<850:
                pirate.rect.x+=5
        stone_hit_list=pygame.sprite.spritecollide(pirate,stone_list,True)
        soldier_hit_list=pygame.sprite.spritecollide(pirate,soldier_list,True)
        for stone in stone_hit_list:
            score+=1
            text=myFont.render("Score="+str(score),True,(0,0,0))
        for soldier in soldier_hit_list:
            score-=5
            text=myFont.render("Score="+str(score),True,(0,0,0))
        screen.blit(text,(700,80))
        allsprites.draw(screen)
    pygame.display.update()
pygame.quit()
    

    
            
            

    
