#made this to store global variables so I don't get global conflics
import pygame as pg
import os
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
dinero = 1000
buttons = []
button_size = (sy/10, sy/10) if sx >= sy*1.6 else (sx/(160/9), sx/(160/9)) 
scale = sy/96 if sx >= sy*1.6 else (sx/(96*16/9), sx/(96*16/9)) 
obstacles = []
coins = []
menu = True
driving = False


















        
