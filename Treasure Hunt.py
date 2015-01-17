#Level One - Treasure Hunt
#A7

#Import Modules/Libraries
import pygame
from time import sleep
from pygame.transform import rotate

#Initialise Pygame/canvas
pygame.init()
pygame.display.set_caption('Treasure Hunt - Level One')
screen = pygame.display.set_mode([640,580])
white = (255,255,255)
screen.fill(white)                      #Turn the screen white

#Import background
bg = pygame.image.load("kart.jpg").convert()
background_position = [0,0]

#Creating class for Car
class Car:
    global screen
    def __init__(self, x, y):
        self.car_img = "player_car.png"
        self.car_imgt = "player_cart.png"
        self.car_imgb = "player_carb.png"
        self.car_imgr = "player_carr.png"
        self.x = x
        self.y = y

    def create(self):
        self.car_load = pygame.image.load(self.car_img)
        self.car_loadt = pygame.image.load(self.car_imgt)
        self.car_loadb = pygame.image.load(self.car_imgb)
        self.car_loadr = pygame.image.load(self.car_imgr)
        self.car      = self.car_load.get_rect()
        self.car.x = self.x
        self.car.y = self.y
        
    def car_update(self):
        screen.blit(self.car_load, self.car)
    def car_updatet(self):
        screen.blit(self.car_loadt,self.car)
    def car_updater(self):
        screen.blit(self.car_loadr,self.car)
    def car_updateb(self):
        screen.blit(self.car_loadb,self.car)
    def move(self, x, y):
        self.car = self.car.move(x, y)
        sleep(0.05)
    def rotation(self,A):
        self.angle=A
        self.rotate90 = pygame.transform.rotate(self.car_load,self.angle)
        screen.blit(self.rotate90,self.car)
        pygame.display.flip()
       
class Landmark: #Creating class for Landmarks
    global screen
    def __init__(self, x, y):
        self.landmark_img = "traffic_cone.png"
        self.x = x
        self.y = y

    def create(self):
        self.landmark_load = pygame.image.load(self.landmark_img)
        self.landmark      = self.landmark_load.get_rect()
        self.landmark.x = self.x
        self.landmark.y = self.y

    def landmark_update(self):
        screen.blit(self.landmark_load, self.landmark)

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

def update():
    screen.blit(bg, background_position)
    car.car_update()
    red.red_update()
    pygame.display.flip()
def updatet():
    screen.blit(bg, background_position)
    car.car_updatet()
    pygame.display.flip()
def updater():
    screen.blit(bg, background_position)
    car.car_updater()
    pygame.display.flip()
def updateb():
    screen.blit(bg, background_position)
    car.car_updateb()
    pygame.display.flip()

#Screen Update
screen.blit(bg, background_position)

#Creating Instance of Car
car = Car(250,380)
car.create()

#Landmarks
l1 = Landmark(130,120)
l1.create()
l2 = Landmark(310,70)
l2.create()
l3 = Landmark(400,200)
l3.create()
l4 = Landmark(500,400)
l4.create()

#Traffic Lights
yellow=Yellow(45,490)
yellow.create()
green=Green(45,490)
green.create()
red=Red(45,490)
red.create()
update()

#Movement
true=1
while true:
    for i in range(23):
        car.move(-10, 0)
        update()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
    for i in range(37):
        car.move(0, -10)
        updatet()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
    for i in range(19):
        car.move(10,0)
        updater()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
    for i in range(10):
        car.move(0,10)
        updateb()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
    for i in range(10):
        car.move(10,0)
        updater()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()

    for i in range(10):
        car.move(0,-10)
        updatet()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()

    for i in range(24):
        car.move(10,0)
        updater()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()

    for i in range(8):
        car.move(0,10)
        updateb()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()

    for i in range(13):
        car.move(-10,0)
        update()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()

    for i in range(12):
        car.move(0,10)
        updateb()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()

    for i in range(29):
        car.move(-10,0)
        update()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
    for i in range(10):
        car.move(0,10)
        updateb()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
        
    for i in range(42):
        car.move(10,0)
        updater()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
        
    for i in range(10):
        car.move(0,10)
        updateb()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
        
    for i in range(38):
        car.move(-10,0)
        update()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
    true=0
    
pygame.display.flip()
pygame.display.quit()
