#Level One - Treasure Hunt
#A7
#Import Modules/Libraries
import pygame
from time import sleep
import time
import random

#Initialise Pygame/canvas
pygame.init()
pygame.display.set_caption('Treasure Hunt - Level One')
screen = pygame.display.set_mode([640,600])
white = (255,255,255)

#Import background
bg = pygame.image.load("kart.jpg").convert()
background_position = [0,0]

#Creating class for Car
class Car:
    global screen
    def __init__(self, x, y):
        self.car_img = "player_car.png"
        self.x = x
        self.y = y

    def create(self):
        self.car_load = pygame.image.load(self.car_img)
        self.car      = self.car_load.get_rect()
        self.car.x = self.x
        self.car.y = self.y

    def car_update(self):
        screen.blit(self.car_load, self.car)
        
    def move(self, x, y):
        self.car = self.car.move(x, y)
        sleep(0.05)
        
#Traffic Light classes
class Red:
    global screen
    def __init__(self, x, y):
        self.red_img = "red.png"
        self.x = x
        self.y = y

    def create(self):
        self.red_load=pygame.image.load(self.red_img)
        self.red=self.red_load.get_rect()
        self.red.x=self.x
        self.red.y=self.y

    def red_update(self):
        screen.blit(self.red_load,self.red)

class Yellow:
    global screen
    def __init__(self, x, y):
        self.yellow_img = "yellow.png"
        self.x = x
        self.y = y

    def create(self):
        self.yellow_load=pygame.image.load(self.yellow_img)
        self.yellow=self.yellow_load.get_rect()
        self.yellow.x=self.x
        self.yellow.y=self.y

"""    def yellow_update(self):
        screen.blit(self.yellow_load,self.yellow)
        yellow.create()
        time.sleep(3)"""

class Green:
    global screen
    def __init__(self, x, y):
        self.green_img = "green.png"
        self.x = x
        self.y = y

    def create(self):
        self.green_load=pygame.image.load(self.green_img)
        self.green=self.green_load.get_rect()
        self.green.x=self.x
        self.green.y=self.y

"""    def green_update(self):
        screen.blit(self.green_load,self.green)
        green.create()"""

#Screen Update
screen.blit(bg, background_position)

#Update function
def update():
    #screen.blit(pygame.image.load(self.car_img), car.cL)
    screen.blit(bg, background_position)
    car.car_update()
    red.red_update()
    pygame.display.flip()

def lights():
    b=random.randint(20,30)
    timer=0
    timer=timer+0.25
    if timer >= 4:
        red_update(b)
        yellow_update(b)
        green_update(b)
        timer = 0
        
#Create Lights
yellow=Yellow(50,500)
yellow.create()
green=Green(50,500)
green.create()
red=Red(50,500)
red.create()
#Creating Instance of Car
car = Car(250,380)
car.create()
update()
    
#Movement

for i in range(23):
    car.move(-10, 0)
    update()
for i in range(37):
    car.move(0, -10)
    update()
for i in range(19):
    car.move(10,0)
    update()
for i in range(12):
    car.move(0,10)
    update()
for i in range(10):
    car.move(10,0)
    update()
for i in range(12):
    car.move(0,-10)
    update()
for i in range(24):
    car.move(10,0)
    update()
for i in range(8):
    car.move(0,10)
    update()
for i in range(13):
    car.move(-10,0)
    update()
for i in range(12):
    car.move(0,10)
    update()
for i in range(29):
    car.move(-10,0)
    update()
for i in range(10):
    car.move(0,10)
    update()
for i in range(42):
    car.move(10,0)
    update()
for i in range(10):
    car.move(0,10)
    update()
for i in range(43):
    car.move(-10,0)
    update()
    
pygame.display.flip()
