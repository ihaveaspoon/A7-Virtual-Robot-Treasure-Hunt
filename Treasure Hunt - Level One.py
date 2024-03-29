#Level One - Treasure Hunt
#A7

#Import Modules/Libraries
import pygame, random, sys
import pygame
import time
from time import sleep
from pygame.transform import rotate
from time import time
from math import floor
from pygame.locals import *

#Initialise Pygame/canvas
pygame.init()
pygame.display.set_caption('Treasure Hunt - Level One')
screen = pygame.display.set_mode([640,580])
white = (255,255,255)
screen.fill(white)    #Set background white

#Creating colours for use
white = (255,255,255)
blue = (176,224,230)
dblue = (0,129,242)
# Set fonts 
font = pygame.font.SysFont("monospace", 40) # Time font
bfont = pygame.font.SysFont("monospace", 20) # Button font

# Buttons
start = 150,480,200,200
stop = 150,550,150,50

#Import background
bg = pygame.image.load("kart.jpg").convert()
background_position = [0,0]

# Start and stop buttons
pygame.draw.rect(screen,blue,start)
screen.blit(bfont.render("Treasure status:", 1, dblue),[160,500])
pygame.draw.rect(screen,blue,stop)

#Create a Start screen
class start_button:

    def __intit__(self,x,y): #Initiliase
        self.button= pg.key.get_pressed()
        self.x=x
        self.y=y
        self.text= text
        self.font=font
        self.surface=surface
        self.quit=pygame.quit()
        self.sys=sys.exit()
        
    def loop(self): #Loops
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit=pygame.quit()
                    self.sys=sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:           # pressing escape quit
                        self.quit=pygame.quit()
                        self.sys=sys.exit()
                    return

    def drawText(self,text, font, surface, x, y,TEXTCOLOR): #Create the starting text
            self.x=x
            self.y=y
            self.color=TEXTCOLOR
            self.textobj = font.render(text, 1, self.color)
            self.textrect = self.textobj.get_rect()
            self.textrect.topleft = (self.x,self.y)
            surface.blit(self.textobj, self.textrect)

#Creating class for Car
class Car:
    global screen
    def __init__(self, x, y): # Initialising Images
        self.car_img = "player_car.png"
        self.car_imgt = "player_cart.png"
        self.car_imgb = "player_carb.png"
        self.car_imgr = "player_carr.png"
        self.x = x
        self.y = y

    def create(self): #Function used to create the robot
        self.car_load = pygame.image.load(self.car_img)
        self.car_loadt = pygame.image.load(self.car_imgt)
        self.car_loadb = pygame.image.load(self.car_imgb)
        self.car_loadr = pygame.image.load(self.car_imgr)
        self.car      = self.car_load.get_rect()
        self.car.x = self.x
        self.car.y = self.y
        #Functions for rotations of the car
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
class Landmark: #Creating class for Landmarks
    global screen
    def __init__(self, x, y): # Initilasing
        self.landmark_img = "traffic_cone.png"
        self.x = x
        self.y = y

    def create(self): #Function used to create landmarks
        self.landmark_load = pygame.image.load(self.landmark_img)
        self.landmark      = self.landmark_load.get_rect()
        self.landmark.x = self.x
        self.landmark.y = self.y

    def landmark_update(self): # Function used to update the landmarks onto the screen
        screen.blit(self.landmark_load, self.landmark)

class Red: # Class for Red Traffic light
    global screen
    def __init__(self, x, y):
        self.red_img = "red.png"
        self.x = x
        self.y = y

    def create(self): # Function used to create red light
        self.red_load=pygame.image.load(self.red_img)
        self.red=self.red_load.get_rect()
        self.red.x=self.x
        self.red.y=self.y

    def red_update(self):# Function used to update red light
        screen.blit(self.red_load,self.red)

class Yellow: #Class for yellow light
    global screen
    def __init__(self, x, y): # Initialise image
        self.yellow_img = "yellow.png"
        self.x = x
        self.y = y

    def create(self): #Function used to create yellow light
        self.yellow_load=pygame.image.load(self.yellow_img)
        self.yellow=self.yellow_load.get_rect()
        self.yellow.x=self.x
        self.yellow.y=self.y
    def yellow_update(self):#Function used to update yellow light
        screen.blit(self.yellow_load,self.yellow)

class Green: # Class for green light
    global screen
    def __init__(self, x, y): # Initialise image
        self.green_img = "green.png"
        self.x = x
        self.y = y

    def create(self): # Function used to create green light
        self.green_load=pygame.image.load(self.green_img)
        self.green=self.green_load.get_rect()
        self.green.x=self.x
        self.green.y=self.y
    def green_update(self):#Function used to update green light
        screen.blit(self.green_load,self.green)
#Functions used for the rotations of the car
def update():
    screen.blit(bg, background_position)
    car.car_update()
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
    
#Creating timer class  
class Timer(object):
	def __init__(self):
		# Initialize of timer

		self.currentTime = 0
		self.startTime = 0
		self.offset = 0
		self.running = False

	def start(self):
		# Starts the timer

		if not self.running:
			self.startTime = time()
		self.running = True

	def stop(self):
		# Stops the timer

		self.offset = (time() - self.startTime) + self.offset
		self.running = False

	def count(self):
		# Gets the timers current time

		if self.running:
			self.currentTime = (time() - self.startTime) + self.offset

	def update(self, screen, font):
		# Updates timer with current time

		dms = self.currentTime*1000 # Get current time

		# Do all the math
		dmin = floor(((dms%86400000)%3600000)/60000)
		dsec = floor((((dms%86400000)%3600000)%60000)/1000)
		dten = floor(((((dms%86400000)%3600000)%60000)%1000)/10)


		pygame.draw.rect(screen, (0,206,209), (350,480,500,300)) # Color background section

		# Blit onto screen

		screen.blit(font.render(str("%.2f"%(dmin/100)).split(".")[1], 1, white),[350,500])
		screen.blit(font.render(":", 1, blue),[425,500])
		screen.blit(font.render(str("%.2f"%(dsec/100)).split(".")[1], 1, white),[460,500])
		screen.blit(font.render(":", 1, blue),[535,500])
		screen.blit(font.render(str("%.2f"%(dten/100)).split(".")[1], 1, white),[570,500])
		
mainTimer = Timer()# Create new timer object

mainTimer.update(screen, font) # Initially update the screen

#Screen Update
screen.blit(bg, background_position)

#Creating Instance of Car
car = Car(250,380)
car.create()
update()

#Creating instances of Landmarks
l1 = Landmark(230,35)
l1.create()
l2 = Landmark(360,150)
l2.create()
l3 = Landmark(400,200)
l3.create()
l4 = Landmark(530,400)
l4.create()

#Creating instances of traffic lights
yellow=Yellow(45,490)
yellow.create()
green=Green(45,490)
green.create()
red=Red(45,490)
red.create()
update()

#Show the start screen
TW=start_button()
TW.drawText('Treasure Hunt!', font, screen,150,220,(255,0,0))
TW.drawText('Press any key to start.', font, screen, 80, 300,(255,255,255))
pygame.display.update()
TW.loop()
#Timer Run
running = True
timerOn = 0 # Start timer flag
#Movement and timing
true = 1
while true:
    green.green_update()
    for i in range(23):
        car.move(-10, 0)
        update()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
    for i in range(37):
        car.move(0, -10)
        updatet()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        pygame.display.flip()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
    for i in range(19):
        if i==13:
            yellow.yellow_update()
        if i==14:
            pygame.time.delay(3000)
            green.green_update()
        car.move(10,0)
        updater()
        l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
        pygame.display.flip()
    for i in range(10):
        car.move(0,10)
        updateb()
        #l1.landmark_update()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
        pygame.display.flip()
    for i in range(10):
        if i==8:
            yellow.yellow_update()
        if i==9:
            pygame.time.delay(3000)
            green.green_update()
        car.move(10,0)
        updater()
        l2.landmark_update()
        l3.landmark_update()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
        pygame.display.flip()
    for i in range(10):
        car.move(0,-10)
        updatet()
        l3.landmark_update()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
        pygame.display.flip()
    for i in range(24):
        car.move(10,0)
        updater()
        l3.landmark_update()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
        pygame.display.flip()
    for i in range(8):
        car.move(0,10)
        updateb()
        l3.landmark_update()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
        pygame.display.flip()
    for i in range(13):
        car.move(-10,0)
        update()
        l3.landmark_update()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
        pygame.display.flip()
    for i in range(12):
        if i==10:
            red.red_update()
            screen.blit(font.render("FOUND!", 1, white),[190,530])
        if i==11:
            pygame.time.delay(5000)
            green.green_update()
        car.move(0,10)
        updateb()
        l3.landmark_update()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time
        pygame.display.flip()
    for i in range(29):
        car.move(-10,0)
        update()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time        
        pygame.display.flip()
    for i in range(10):
        car.move(0,10)
        updateb()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time        
        pygame.display.flip()
    for i in range(42):
        car.move(10,0)
        updater()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time        
        pygame.display.flip()  
    for i in range(10):
        if i==8:
            yellow.yellow_update()
        if i==9:
            pygame.time.delay(3000)
            green.green_update()
        car.move(0,10)
        updateb()
        l4.landmark_update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time        
        pygame.display.flip()
    update()
    for i in range(38):
        car.move(-10,0)
        update()
        mainTimer.start()
        mainTimer.count() # Get current time
        mainTimer.update(screen, font) # Apply new current time        
        pygame.display.flip()
        true = 0
pygame.display.flip()
pygame.display.quit()
