import pygame,sys
import time
import random
from pygame.locals import *

SCREEN_WIDTH=700
SCREEN_HEIGHT=700
pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def changeBackground(img):
    background=pygame.image.load(img)
    bg= pygame.transform.scale(background,(screen_width,screen_height)) 
    screen.blit(bg,(0,0))
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Player test.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(100,90))
        self.rect=self.image.get_rect()
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("realtarget.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(100,70))
        self.rect=self.image.get_rect()
        self.rect.x=1
        self.rect.y=500
        self.moveLeft=False
class Enemy(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(60,60))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(SCREEN_WIDTH)
        self.rect.y=random.randrange(SCREEN_HEIGHT)

enemies=["Obstacle1.png","obstacle2.png","final obstacle 3.png"]

enemy_group=pygame.sprite.Group()
allsprites=pygame.sprite.Group()

def createEnemy():
    newenemy=Enemy(random.choice(enemies))
    enemy_group.add(newenemy)
    allsprites.add(newenemy)
    return newenemy

def createPlayerTarget():
    player=Player()
    allsprites.add(player)
    target=Target()
    allsprites.add(target)
    return player,target

def startgame():
    player,target=createPlayerTarget()
    createEnemy()
    allsprites.draw(screen)
    pygame.display.update()
startgame()
changebackground("BgImage.jpg")
