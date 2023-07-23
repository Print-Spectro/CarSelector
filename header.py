#made this to store global variables so I don't get global conflics
import pygame as pg
import os
pg.font.init()
pg.display.set_caption('RoadRage')
fullscreen = False
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
screen = pg.display.set_mode((1000, 800))
sx, sy = screen.get_size()
Title_Font = pg.font.SysFont('Squarefont', int(200*sy/1440)) if sx >= sy*1.6 else pg.font.SysFont('Squarefont', int(200*sy/2560)) #for bigger text
Text_Font = pg.font.SysFont('Squarefont', int(100*sy/1440)) if sx >= sy*1.6 else pg.font.SysFont('Squarefont', int(100*sy/2560)) #for smaller text
Background = pg.image.load(os.path.join('assets', 'road.png')) #background image
FPS = 60 #maximum uptades per second
dinero = 1000 #money the player has collected to spend on upgrades
buttons = [] #stores a list of buttons
button_size = (sy/10, sy/10) if sx >= sy*1.6 else (sx/(160/9), sx/(160/9)) 
scale = sy/96 if sx >= sy*1.6 else (sx/(96*16/9), sx/(96*16/9)) 
obstacle_v = 10 #obstacle velocity, exposing it here allows me to tune it without refactoring
obstacles = [] #used to store obstacle objects drawn to the road
coins = [] #used to store coin objects drawn to the road
menu = True #used to swap between gamemodes
obstacles = [] #stores onscreen obscales
coins = []  #stores onscreen coins


















        
