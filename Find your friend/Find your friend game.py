import pygame,sys
import time
import random
from pygame.locals import *

SCREEN_WIDTH=700
SCREEN_HEIGHT=700
pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
WHITE=(255,255,255)
RED=(255,0,0)
BLACK=(0,0,0)
pygame.mixer.init()
clock=pygame.time.Clock()
myFont=pygame.font.SysFont("Times New Roman",52)
SmallFont=pygame.font.SysFont("Calibri",46)

def changeBackground(img):
    background=pygame.image.load(img)
    bg=pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(bg,(0,0))
    pygame.display.set_caption("Finding my friend")
    pygame.display.update() 

def welcomeScreen():
    pygame.mixer.music.load("startsound.mp3")
    pygame.mixer.music.play(-1)
    changeBackground("startscreen.jpg")
    text=myFont.render("Finding my friend starfish",True,RED)
    screen.blit(text,(100,100))
    #rules
    text=SmallFont.render('Press "Space bar" to start',True,BLACK)
    screen.blit(text,(20,300))
    text=SmallFont.render('Press the arrow keys to navigate',True,BLACK)
    screen.blit(text,(20,325))
    text=SmallFont.render('If you touch a fish(enemy) you will lose a life',True,BLACK)
    screen.blit(text,(20,350))
    text=SmallFont.render('If you touch a seagrass(obstacle) you will be relocated',True,BLACK)
    screen.blit(text,(20,375))
    text=SmallFont.render('Press (X) to quit the game',True,BLACK)
    screen.blit(text,(20,400))
    text=SmallFont.render("Wish you good luck :D",True,RED)
    
    screen.blit(text,(70,70))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE):
                startgame()
                return
            
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("player.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,70))
        self.rect=self.image.get_rect()
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)
        if self.rect.left<0:
            self.rect.left=0
        elif self.rect.right>SCREEN_WIDTH:
            self.rect.right=SCREEN_WIDTH
        if self.rect.top<=0:
            self.rect.top=0
        elif self.rect.bottom>=SCREEN_HEIGHT:
            self.rect.bottom=SCREEN_HEIGHT
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("target.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(70,70))
        self.rect=self.image.get_rect()
        self.rect.x=1
        self.rect.y=500
        self.moveLeft=False
    def update(self):
        if self.moveLeft:
            self.rect.move_ip(-2,0)
            if self.rect.x<=5:
                self.moveLeft=False
        else:
            self.rect.move_ip(2,0)
            if self.rect.x>=SCREEN_WIDTH - 50:
                self.moveLeft=True
class Enemy(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(60,60))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(SCREEN_WIDTH)
        self.rect.y=random.randrange(SCREEN_HEIGHT)
        self.speed=random.randint(1,7)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img).convert_alpha()
        self.image=pygame.transform.scale(self.image,(60,60))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(SCREEN_WIDTH)
        self.rect.y=random.randrange(SCREEN_HEIGHT)
    def update(self):
        self.rect.move_ip(random.randint(-3,3),random.randint(-1,1))
        if self.rect.right<0:
            self.kill()
                        

enemies=["enemy1.png","enemy2.png","enemy3.png","enemy4.png"]
obstacles=["obstacle1.png","obstacle2.png","obstacle3.png","obstacle4.png"]

enemy_group=pygame.sprite.Group()
obstacle_group=pygame.sprite.Group()

allsprites=pygame.sprite.Group()

def createEnemy():
    newenemy=Enemy(random.choice(enemies))
    enemy_group.add(newenemy)
    allsprites.add(newenemy)
    return newenemy

def createObstacle():
    newobstacle=Obstacle(random.choice(obstacles))
    obstacle_group.add(newobstacle)
    allsprites.add(newobstacle)
    return newobstacle

def createPlayerTarget():
    player=Player()
    allsprites.add(player)
    target=Target()
    allsprites.add(target)
    return player,target

def bounce(obj):
    pygame.mixer.music.load("bounce.mp3")
    pygame.mixer.music.play()
    obj.rect.move_ip(random.randint(-30,30),random.randint(-30,30))
def endScreen(sound,img,text):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    changeBackground(img)
    screen.blit(text,(150,50))
    text=SmallFont.render("Press 'Space Bar' to restart",True,BLACK)
    screen.blit(text,(20,200))
    text=SmallFont.render("Press(X) to quit the game",True,BLACK)
    screen.blit(text,(20,240))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE):
                welcomeScreen()
                return
            
    
    

def startgame():
    enemy_group.empty()
    obstacle_group.empty()
    allsprites.empty()
    ADD_ENEMY=pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENEMY,600)
    ADD_OBSTACLE=pygame.USEREVENT + 2
    pygame.time.set_timer(ADD_OBSTACLE,1000)
    
    player,target=createPlayerTarget()
    
    #createEnemy()
    #createObstacle()
    life=20
    clock.tick(30)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                return
            elif event.type==ADD_ENEMY:
                createEnemy()
            elif event.type==ADD_OBSTACLE:
                createObstacle()
        pressed_keys=pygame.key.get_pressed()

        
        player.update(pressed_keys)
        if pygame.sprite.spritecollideany(player,obstacle_group):
            bounce(player)
        if pygame.sprite.spritecollideany(player,enemy_group):
            bounce(player)
            life-=1
            if life==0:
                sound="losesound.mp3"
                image="endscreen.jpg"
                text=myFont.render("You lost! Better luck next time",True,WHITE)
                endScreen(sound,image,text)
                return
        if pygame.sprite.collide_rect(player,target):
            sound="winsound.mp3"
            image="endscreen.jpg"
            text=myFont.render("Congrats you won! :D",True,WHITE)
            endScreen(sound,image,text)
            return
        

        
        enemy_group.update()
        obstacle_group.update()
        target.update()
        screen.blit(pygame.image.load("background.jpg"),(0,0))
        pygame.draw.rect(screen,BLACK,(500,10,life*10,10))
        
        allsprites.draw(screen)
        clock.tick(30)
        pygame.display.update()

welcomeScreen()
pygame.quit()




    



