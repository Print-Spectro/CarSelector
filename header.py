#made this to store global variables so I don't get global conflics
import pygame as pg
import os
pg.font.init()
screen = DISPLAYSURF = pg.display.set_mode((0, 0), pg.FULLSCREEN)
screen = pg.display.set_mode((1000, 800))
resolution = screen.get_size()
Title_Font = pg.font.SysFont('Squarefont', 100)
Text_Font = pg.font.SysFont('Squarefont', 40)
Background = pg.image.load(os.path.join('assets', 'road.png'))
colours = {
    "white" : (206,206,206),
    "black" : (30,30,30),
    "red"   : (180, 16, 16),
    "yellow": (237, 186, 41),
    "green" : (46, 228, 91)
    }

FPS = 60
dinero = 0
buttons = []
vehicles = None
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

colours_cycler = cycler([colours[i] for i in colours])


        
