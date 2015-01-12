#Traffic Light Class
from Tkinter import *
import random
import time

window = Tk()
window.title("Traffic Lights")
canvas = Canvas(window, width=600, height=400, bg='white')
canvas.pack(padx=10,pady=10)

#TrafficLights
class TrafficLights:
    def __init__(self):
        red = canvas.create_oval(35, 35, 50, 50, fill = "white",width=2)
        green = canvas.create_oval(35,60,50,75, fill = "white",width=2)
    def redoff (self):
        for i in range (50):
            red = canvas.create_oval(35,35,50,50,fill="red",outline="black",width=2)
            canvas.update()
            time.sleep(0.05)

    def redon (self):
        for i in range (50):
            red = canvas.create_oval(35,35,50,50,fill="white",outline="black",width=2)
            canvas.update()
            time.sleep(0.05)

    def greenoff (self):
        for i in range (50):
            green = canvas.create_oval(35,60,50,75, fill = "green",outline="black",width=2)
            canvas.update()
            time.sleep(0.01)

    def greenon (self):
        for i in range (50):
            green = canvas.create_oval(35,60,50,75, fill = "white",outline="black",width=2)
            canvas.update()
            time.sleep(0.05)

            
test=TrafficLights()
b = random.randint(20,30)
test.redoff()
test.redon()
test.greenoff()
window.mainloop()
