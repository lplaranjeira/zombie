import pygame
import random
from pygame_functions import *

screenSize (800, 600)


Water = makeSprite("Water.png")
Zombie0 = makeSprite("Zombie.png")
Zombie1 = makeSprite("Zombie.png")
Zombie2 = makeSprite("Zombie.png")
Zombie3 = makeSprite("Zombie.png")
Zombie4 = makeSprite("Zombie.png")

PS_L = makeSprite("PS_L.png")
PS_R = makeSprite("PS_R.png")
PS_D = makeSprite("PS_D.png")
PS_UP = makeSprite("PS_UP.png")
Bullet = makeSprite("Bullet.png")
setBackgroundImage("Ground.png")
Over = makeSprite("Gameover.png")
Win = makeSprite ("Vitoria.png")
makeMusic("mp3.mp3")
i = 1
enemys = 0
bullets = 0
px = 400
py = 300
bx = px
by = py
shoot = False
up = False
down = False
left = False
right = False
run = False
death = False
speed = 10

class Zombies():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 1
        self.asset = Zombie0
        self.health = 1
    def Zombie_ia(self):
        if self.health > 0:
            moveSprite(self.asset, self.x, self.y, True)
            showSprite(self.asset)
            if self.x > px:
                self.x -= self.speed
            elif self.x < px:
                self.x += self.speed

            if self.y > py:
                self.y -= self.speed
            elif self.y < py:
                self.y += self.speed
        elif self.health <= 0:
            hideSprite(self.asset)

        

def Player():
    moveSprite(PS_L, px, py, True)
    moveSprite(PS_R, px, py, True)
    moveSprite(PS_D, px, py, True)
    moveSprite(PS_UP, px, py, True)
    
zombie0 = Zombies()
zombie1 = Zombies()
zombie2 = Zombies()
zombie3 = Zombies()
zombie4 = Zombies()
playMusic(loops=100)
while i <= 6:
    zombie0.health = 1
    zombie0.x = random.randint(100, 300)
    zombie0.y = random.randint(100, 200)
    zombie0.speed += 0.5

    zombie1.health = 1
    zombie1.asset = Zombie1
    zombie1.x = random.randint(100, 300)
    zombie1.y = random.randint(300, 500)
    zombie1.speed += 0.5

    zombie2.health = 1
    zombie2.asset = Zombie2
    zombie2.x = random.randint(100, 300)
    zombie2.y = random.randint(100, 200)
    zombie2.speed = 0.5

    zombie3.health = 1
    zombie3.asset = Zombie3
    zombie3.x = random.randint(500, 700)
    zombie3.y = random.randint(100, 200)
    zombie3.speed += 0.5

    zombie4.health = 1
    zombie4.asset = Zombie4
    zombie4.x = random.randint(500, 600)
    zombie4.y = random.randint(300, 500)
    zombie4.speed += 0.5

    enemys = 5
    px = 400
    py = 300
    bullets += 1 
    
    run = True   
    while run == True:
        if enemys == 0:
            run = False
        showSprite(Water)
        Player()

    #Zombies
        zombie0.Zombie_ia()
        zombie1.Zombie_ia()
        zombie2.Zombie_ia()
        zombie3.Zombie_ia()
        zombie4.Zombie_ia()

    #Player
        #death
        if touching(PS_L, zombie0.asset) and zombie0.health > 0:
            showSprite(Over)
            death = True
        elif touching(PS_L, zombie1.asset) and zombie1.health > 0:
            showSprite(Over)
            death = True
        elif touching(PS_L, zombie2.asset) and zombie2.health > 0:
            showSprite(Over)
            death = True
        elif touching(PS_L, zombie3.asset) and zombie3.health > 0:
            showSprite(Over)
            death = True
        elif touching(PS_L, zombie4.asset) and zombie4.health > 0:
            showSprite(Over)
            death = True
        #movement
        if death == False:
            if keyPressed("up"):
                up = True
                down = False
                left = False
                right = False
            elif keyPressed("down"):
                up = False
                down = True
                left = False
                right = False
            elif keyPressed("left"):
                up = False
                down = False
                left = True
                right = False
            elif keyPressed("right"):
                up = False
                down = False
                left = False
                right = True
                
            if keyPressed("w"):
                showSprite(PS_UP)
                hideSprite(PS_D)
                hideSprite(PS_L)
                hideSprite(PS_R)            
                
                py -= speed
            elif keyPressed("s"):
                showSprite(PS_D)
                hideSprite(PS_UP)
                hideSprite(PS_L)
                hideSprite(PS_R)
                
                py += speed
            elif keyPressed("a"):
                showSprite(PS_L)
                hideSprite(PS_D)
                hideSprite(PS_UP)
                hideSprite(PS_R)
                
                px -= speed
            elif keyPressed("d"):
                showSprite(PS_R)
                hideSprite(PS_D)
                hideSprite(PS_L)
                hideSprite(PS_UP)
                
                px += speed

            #shooting
            if keyPressed("space") and bx == px and by == py and bullets > 0:
                shoot = True
                bullets -= 1

            if shoot == True:
                if up == True:
                    moveSprite(Bullet, bx, by, True)
                    showSprite(Bullet)
                    by -= 20
                elif down == True:
                    moveSprite(Bullet, bx, by, True)
                    showSprite(Bullet)
                    by += 20
                elif left == True:
                    moveSprite(Bullet, bx, by, True)
                    showSprite(Bullet)
                    bx -= 20
                elif right == True:
                    moveSprite(Bullet, bx, by, True)
                    showSprite(Bullet)
                    bx += 20

                if touching(Bullet, zombie0.asset) and zombie0.health > 0:
                    zombie0.health -= 1
                    enemys -= 1
                elif touching(Bullet, zombie1.asset) and zombie1.health > 0:
                    zombie1.health -= 1
                    enemys -= 1
                elif touching(Bullet, zombie2.asset) and zombie2.health > 0:
                    zombie2.health -= 1
                    enemys -= 1
                elif touching(Bullet, zombie3.asset) and zombie3.health > 0:
                    zombie3.health -= 1
                    enemys -= 1
                elif touching(Bullet, zombie4.asset) and zombie4.health > 0:
                    zombie4.health -= 1
                    enemys -= 1

                if touching (Bullet, Water):
                    shoot = False
            else:
                moveSprite(Bullet, bx, by, True)
                bx = px
                by = py
                hideSprite(Bullet)
    i += 1
showSprite(Win)
    

