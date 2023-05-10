import pygame as pg
import header as hd

def toggle_fullscreen():
    """Depricated
    Thought it would be fun to make some rudimentary settings but 
    pygamne didn't want to exit meaning updating all the scale values wasn't really worth it
    """
    if hd.fullscreen: 
        hd.screen = pg.display.set_mode((1000, 800)) 
        hd.fullscreen == False
    elif not hd.fullscreen:
        hd.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        hd.fullscreen == True
    hd.buttons = []
    hd.vehicles = hd.create_vehicles()
    colour_selector()
    menu()




def test():
    print("test_success")
class colour_class:
    def __init__(self, colour):
        self.colour = colour
    def colour_set(self):
        vehicles.item.set_colour(self.colour)

colours ={
            "white" : colour_class((206,206,206)),
            "black" : colour_class((30,30,30)),
            "red"   : colour_class((180, 16, 16)),
            "orange": colour_class((255, 128, 31)),
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






def fill(surface, color):
    """Fill all pixels of the surface with color, preserving transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pg.Color(r, g, b, a))

def upgrade_button_dist(upgrades):
    c=0
    sx, sy = hd.screen.get_size()
    bx, by = hd.button_size
    for i in upgrades: #setting the button positions
        i.set_position((c*sx/(len(upgrades)*3)+sx/3+bx/2, sy/6-by/2))
        c+=1

class Button():
    """
    Facilitates the creaton of button objects that execute a function on click.
    """
    def __init__(self, x, y, width, height, buttonText="Button", onclickFunction=None, onePress=False, buttonImage = None, button_list = True, onhoverFunction = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onhoverFunction = onhoverFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.fillColors = {
            'normal': '#dadada',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
        
        


        if buttonImage != None: #conditional statement allows for more flexible button representations
            self.buttonSurf = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', buttonImage)).convert_alpha(), hd.scale)
        elif buttonText != None:
            self.buttonSurf = hd.Text_Font.render(buttonText, True, (20, 20, 20))
        if button_list:
            hd.buttons.append(self)
    def update(self):
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)

    def process(self, screen, **kwargs):
        """
        Tracks mouse location and if mouse intersects with the button there is a colour change.
        Upon click 
        """
        mousePos = pg.mouse.get_pos()
        self.buttonSurface.fill((self.fillColors['normal']))
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if self.onhoverFunction != None:
                self.onhoverFunction()
            if pg.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction(**kwargs)
                elif not self.alreadyPressed:
                    self.onclickFunction(**kwargs)
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
            ])
        screen.blit(self.buttonSurface, self.buttonRect)

class upgrade:
    def __init__(self, image, owned = False, equipped = False, price = 10, scale = hd.scale, button_position = (hd.sx/2, hd.sy/6) ):
        self.surface = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', "magnet.png")).convert_alpha(), scale)
        self.name = image[:-4]
        self.price = price
        self.owned = owned
        self.equipped = equipped
        self.bpos = button_position
        self.image = image
        bx, by = self.bpos
        self.description = self.name
        #initialising buy state button
        self.button_buy = Button(bx, by, hd.button_size[0], hd.button_size[1], 
                                 buttonImage = image,   onhoverFunction = self.describe,
                                 onclickFunction=self.purchase, button_list = False)
        self.button_buy.fillColors["normal"] = (30, 30, 30)
        self.button_equip = Button(bx, by, hd.button_size[0], hd.button_size[1], 
                                   buttonImage = image, onhoverFunction = self.describe,
                                   onclickFunction=self.equip_toggle, button_list = False)

    def draw_button(self, screen, vehicle):
        """
        Draws the buy button which runs the purchase function if not owned.
        once owned the equip toggle button will be displayed
        """
        if vehicle.owned:
            if self.owned:
                self.button_equip.process(screen)

            elif not self.owned:
                self.button_buy.process(screen)
                text = pg.transform.scale_by(hd.Text_Font.render("£ " + str(self.price), True, (200, 200, 200)), 0.6)
                tx, ty = text.get_size()
                bx, by = hd.button_size
                screen.blit(text, (self.bpos[0]+bx/2-tx/2, self.bpos[1]+by/2-ty/2))
            else:
                print("Error self.owned is not bool")
            

    def equip_toggle(self):
        """
        Swapps the equip state for an upgrade instance. This will only become available once owned = True, see self.draw_button.
        """
        if not self.equipped:
            self.equipped = True
            self.button_equip.fillColors["normal"] = (91, 190, 91)
            self.button_equip.fillColors["hover"] = (0, 100, 0)
        elif self.equipped:
            self.equipped = False
            self.button_equip.fillColors["normal"] = "#dadada"
            self.button_equip.fillColors["hover"] = '#666666'

    def purchase(self):
        """Used to purchase this upgrade instance. Will be stored in the instanced vehicle class so each vehicle has its own upgrades
        Subtracts the price of the upgrade from global money "dinero" only if you can afford it and sets owned to True.
        """
        if not self.owned and hd.dinero >= self.price:
            self.owned = True
            hd.dinero -= self.price

    def set_position(self, position):
        """Input: x, y coordinate tuple: button placed at this position
        """
        self.bpos = position
        for i in (self.button_buy, self.button_equip):
            i.x = position[0]
            i.y = position[1]
            i.update()

    def describe(self):
        "Draws an ability description to the screen"
        text = hd.Title_Font.render(self.description, True, (200, 200, 200))
        tx, ty = text.get_size()
        hd.screen.blit(text, (hd.sx/2-tx/2, hd.sy/2-ty/2))

class vehicle():
    def __init__(self, 
                 colour_image, 
                 detail_image, 
                 screen,
                 position = (0,0),
                 health = 10, 
                 speed = 10, 
                 handling = 10, 
                 price = 100, 
                 owned = False,
                 upgrades = [
                     upgrade("magnet.png"),
                     upgrade("ram.png"),
                     upgrade("wheel.png")
                 ]):
       
        self.colour_surface = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', colour_image)).convert_alpha(), hd.scale)
        self.detail_surface = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', detail_image)).convert_alpha(), hd.scale)
        self.size = self.colour_surface.get_size()
        self.price = price
        self.button_buy = Button(hd.sx/2-hd.button_size[0]*3.5/2, 
                             hd.sy/2-hd.button_size[1]/2, 
                             hd.button_size[0]*3.5, 
                             hd.button_size[1], 
                             buttonText = "Buy £" + str(self.price), 
                             button_list = False,
                             onclickFunction = self.purchase)
        self.magnet = upgrade("magnet.png")
        self.upgrades = upgrades
        upgrade_button_dist(upgrades)
        self.name = detail_image[:-4]
        self.health = health
        self.speed = speed
        self.handling = handling
        self.owned = owned
        self.position = position
        self.colour = colours["blue"].colour
        self.set_colour(colours["white"].colour)
    def set_upgrades(self, upgrades = upgrade("magnet.png")):
        self.upgrades = [i for i in upgrades]

    
    def set_colour(self, colour):
        """
        Input: RGB colour tuple
        Result: changes colour of all pixels in colour layer
        Saturation and lightnes are reduced if the vehicles has not been purchased
        """
        
        self.colour = colour
        colour = pg.Color(colour)
        if not self.owned: 
            h, s, l, a = colour.hsla
            colour.hsla = h, s/2, l/2, a
        fill(self.colour_surface, colour)
        

    def handle_movement(self):
        "up"
        "down"

    def draw_buttons(self, screen):
        """
        Method for drawring the purchase button. 
        The button will not be drawn if the vehicle is already owned. 
        """
        if not self.owned:
            self.button_buy.process(screen)
        if self.owned:
            for i in self.upgrades:
                i.draw_button(screen, self)


    def purchase(self):
        if self.owned == False and hd.dinero >= self.price:
            self.owned = True
            hd.dinero -= self.price
            self.set_colour(self.colour)
            


def colour_selector():
    """Creates n buttons from the colours list in the header
    Each colour is is an object with its own method for setting colour"""
    bx, by = hd.button_size #as always, scaling to the screen resolution
    sx, sy = hd.screen.get_size()  
    c = 0 #counter because I decided to use a dictionary for the colours
    #looping through colours
    for i in colours:
        Button_i = Button(c*sx/(len(colours)*2)+sx/4-bx/2,5*sy/6-by/2, bx, by, buttonText="", onclickFunction = colours[i].colour_set)
        colour = colours[i].colour #changing the coloures stored in the button object
        Button_i.fillColors["normal"] = colour
        colour_i = pg.Color(colour)
        h, s, l, a = colour_i.hsla
        colour_i.hsla = h, s/2, l+(100-l)/2, a
        Button_i.fillColors["hover"] = colour_i
        Button_i.fillColors["pressed"] = colour
        c+=1

def draw_selector(screen, vehicle):
    """Grouping of all the methods that draw to the screen
    probably don't need to pass in screen or vehicle since they are global
    """
    sx, sy = screen.get_size()
    bx, by = hd.Background.get_size()
    vx, vy = vehicle.size
    Background = pg.transform.scale(hd.Background, ((sy/by)*bx, sy))
    screen.blit(Background, (0,0))
    vehicle.draw_buttons(screen)
    screen.blit(vehicle.colour_surface, (4*sx/5-vx/2, (sy-vy)/2))
    screen.blit(vehicle.detail_surface, (4*sx/5-vx/2, (sy-vy)/2))
    nametag = hd.Title_Font.render(vehicle.name, True, (200, 200, 200))
    health = hd.Title_Font.render(str(vehicle.health) + " HP", True, (200, 200, 200))
    money = hd.Title_Font.render("£ " + str(hd.dinero), True, (200, 200, 200))
    screen.blit(nametag, (sx/20, sy-sy/2-nametag.get_size()[1]/2))
    screen.blit(health, (sx-sx/20-health.get_size()[0], sy/8-health.get_size()[1]/2))
    screen.blit(money, (sx/20, sy/8-health.get_size()[1]/2))
    for i in hd.buttons:
        i.process(screen)
#I was struggling a bit to create separate instances for all the upgrades bloody python sometimes
def create_vehicles():
    return cycler([vehicle("beancolour.png", "bean.png", hd.screen, health = 5, price = 0, owned = True, upgrades = [upgrade("magnet.png"),upgrade("ram.png"),upgrade("wheel.png")]),
            vehicle("jeepcolour.png", "jeep.png", hd.screen, health = 10, price = 50, upgrades = [upgrade("magnet.png"),upgrade("ram.png"),upgrade("wheel.png")]),
            vehicle("bugatticolour.png", "bugatti.png", hd.screen, health = 10, price = 100, upgrades = [upgrade("magnet.png"),upgrade("ram.png"),upgrade("wheel.png")]),
            vehicle("panthercolour.png", "panther.png", hd.screen, health = 50, price = 500, upgrades = [upgrade("magnet.png"),upgrade("ram.png"),upgrade("wheel.png")])])
    
vehicles = create_vehicles()
    
def menu():
    """Herein lie the few remaining local variables. 
    good place to create buttons that run global functions and such
    While loop to run the game at maximum 60 updates per second. 
    """

    run = True
    clock = pg.time.Clock()
    sx, sy = hd.screen.get_size()
    bx, by = hd.button_size
    Button(sx-sx/5-bx/2,3*sy/4-by/2, bx, by, buttonImage = "down.png", onclickFunction = vehicles.forward)
    Button(sx-sx/5-bx/2 ,sy/4-by/2, bx, by, buttonImage = "up.png", onclickFunction = vehicles.reverse)
    #Button(sx/20, 19*sy/20-by/2, bx*5, by, buttonText = "Fullscreen", onclickFunction = toggle_fullscreen) #fullscreen button
    colour_selector()
    print(len(hd.buttons))
    while run:
        clock.tick(hd.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit() #it's surprisingly hard to quit without this functionality
        draw_selector(hd.screen, vehicles.item)
        pg.display.update() #update the display at the end of each loop
        



if __name__ == '__main__':
    menu()
    pg.quit()
 

