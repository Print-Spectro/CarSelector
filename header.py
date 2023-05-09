#made this to store global variables so I don't get global conflics
import pygame as pg
import os
import carselector as cs
pg.font.init()
pg.display.set_caption('RoadRage')
fullscreen = False
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
#screen = pg.display.set_mode((1000, 800))
sx, sy = screen.get_size()
Title_Font = pg.font.SysFont('Squarefont', int(200*sy/1440)) if sx >= sy*1.6 else pg.font.SysFont('Squarefont', int(200*sy/2560))
Text_Font = pg.font.SysFont('Squarefont', int(100*sy/1440)) if sx >= sy*1.6 else pg.font.SysFont('Squarefont', int(100*sy/2560))
Background = pg.image.load(os.path.join('assets', 'road.png'))
FPS = 60
dinero = 50
buttons = []
colour_buttons = []
button_size = (sy/10, sy/10) if sx >= sy*1.6 else (sx/16, sx/16) 
scale = screen.get_size()[1]/96
class colour_class:
    def __init__(self, colour):
        self.colour = colour
    def colour_set(self):
        vehicles.item.set_colour(self.colour)
colours ={
            "white" : colour_class((206,206,206)),
            "black" : colour_class((30,30,30)),
            "red"   : colour_class((180, 16, 16)),
            "yellow": colour_class((237, 186, 41)),
            "green" : colour_class((91, 190, 91)),
            "blue"  : colour_class(((46, 110, 190)))
        }

class cycler:
    def __init__(self, items):
        self.items = items
        self.index = 0
        self.item = self.items[0]

    def forward(self):
        if self.index < (len(self.items)-1):
            self.index += 1
            self.item = self.items[self.index]
        elif self.index >= (len(self.items)-1):
            self.index = 0
            self.item = self.items[self.index]
    def reverse(self):
        if self.index > 0:
            self.index -= 1
            self.item = self.items[self.index]
        elif self.index <= 0:
            self.index = (len(self.items)-1)
            self.item = self.items[self.index]


def create_vehicles():
    return cycler([cs.vehicle("beancolour.png", "bean.png", screen, health = 5, price = 0, owned = True),
            cs.vehicle("jeepcolour.png", "jeep.png", screen, health = 10, price = 50),
            cs.vehicle("bugatticolour.png", "bugatti.png", screen, health = 10, price = 100),
            cs.vehicle("panthercolour.png", "panther.png", screen, health = 50, price = 500)])

vehicles = create_vehicles()

















        
