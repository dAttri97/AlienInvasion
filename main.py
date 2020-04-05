#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pygame
import random
import math
from pygame import mixer
pygame.init()


# In[8]:


background = pygame.image.load('images/background1.jpg')
def backGround():
    screen.blit(background,(0,0))


# In[9]:



mixer.music.load('sounds/background.wav')
mixer.music.play(-1)
bulletSound = mixer.Sound('sounds/laser.wav')
explodeSound = mixer.Sound('sounds/explosion.wav')


# In[10]:


bulletImg = pygame.image.load('images/missile.png')
bulletX = 0
bulletY = 450
bulletChangeX = 0
bulletChangeY = 3
fire = False
def fire_bullet(x,y):
    global fire
    fire = True
    screen.blit(bulletImg,(x+16,y+10))


# In[11]:


playerImg = pygame.image.load('images/rocket.png')
playerX = 370
playerY = 480
playerChangeX=0
playerChangeY=0
def playerShip(x,y):
    screen.blit(playerImg,(x,y))


# In[12]:


arr = ['enemy','enemy1','enemy2','enemy3','enemy4']
ind = random.randint(0,len(arr)-1)
enemyImg = pygame.image.load('images/'+str(arr[ind])+'.png')
enemyX = random.randint(0,736)
enemyY = random.randint(0,536)
enemyChangeX=2.5
enemyChangeY=20
def enemyShip(x,y):
    screen.blit(enemyImg,(enemyX,enemyY))


# In[13]:


def isCollide(ex,ey,bx,by):
    dist = math.sqrt(math.pow(ex-bx,2)+math.pow(ey-by,2))
    if dist<=25:
        return True
    return False


# In[14]:


score = 0
font = pygame.font.Font('freesansbold.ttf',32)
def show_score():
    score_text = font.render('Score:'+str(score),True,(255,255,255))
    screen.blit(score_text,(10,10))


# In[15]:



# setting the screen size
screen = pygame.display.set_mode((800,600))

#changing title and icon
pygame.display.set_caption('Alien Invasion')
icon = pygame.image.load('images/spaceship.png')
pygame.display.set_icon(icon)

running = True
while running:
    backGround()
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeX=-3
            if event.key == pygame.K_RIGHT:
                playerChangeX=3
            if event.key == pygame.K_SPACE:
                if fire == False:
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            playerChangeX=0                        
            playerChangeY=0
    playerX+=playerChangeX
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    enemyX+=enemyChangeX
    if enemyX<=0:
        enemyChangeX=2.5
        enemyY+=enemyChangeY
    elif enemyX>=736:
        enemyChangeX=-2.5
        enemyY+=enemyChangeY
    if bulletY<=0:
        bulletY = 450
        fire = False
    if fire == True:
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletChangeY
    if isCollide(enemyX,enemyY,bulletX,bulletY):
        explodeSound.play()
        score+=10
        fire = False
        bulletY=450
        ind = random.randint(0,len(arr)-1)
        enemyImg = pygame.image.load('images/'+str(arr[ind])+'.png')
        enemyX = random.randint(0,736)
        enemyY = random.randint(0,536)
    enemyShip(enemyX,enemyY)
    show_score()
    playerShip(playerX,playerY)
    pygame.display.update()

