import pygame as pg
import header as hd
def test():
    print("test_success")
def next(pos, sequence):
    "if pos"
    

def last(sequence):
    "a"


class Button():
    def __init__(self, x, y, width, height, buttonText="Button", onclickFunction=None, onePress=False, buttonImage = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
        if buttonImage != None: 
            self.buttonSurf = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', buttonImage)).convert_alpha(), 10)
        elif buttonText != None:
            self.buttonSurf = hd.Text_Font.render(buttonText, True, (20, 20, 20))  
 
        hd.buttons.append(self)

    def process(self, screen):
        """
        Tracks mouse location and if mouse intersects with the button there is a colour change.
        Upon click 
        """
        mousePos = pg.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pg.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
        self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
        self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
            ])
        screen.blit(self.buttonSurface, self.buttonRect)



def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pg.Color(r, g, b, a))

class vehicle:
    def __init__(self, 
                 colour_image, 
                 detail_image, 
                 screen,
                 position = (0,0),
                 health = 10, 
                 speed = 10, 
                 handling = 10, 
                 price = 100, 
                 owned = True):
        self.scale = screen.get_size()[1]/96
        self.colour_surface = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', colour_image)).convert_alpha(), self.scale)
        self.detail_surface = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', detail_image)).convert_alpha(), self.scale)
        self.size = self.colour_surface.get_size()
        self.name = detail_image[:-4]
        self.health = health
        self.speed = speed
        self.handling = handling
        self.price = price
        self.owned = owned
        self.position = position
    def colour(self, colour):
        """
        Input: colour name string in white black red yellow green blue
        Result: changes colour of all pixels in colour layer
        """
        fill(self.colour_surface, pg.Color(colour))

    def handle_movement(self):
        "up"
        "down"

    def draw(self, screen):
        "a"


class upgrade:
    def __init__(self, image, scale, owned = True, equipped = False):
        self.surface = pg.transform.scale_by(pg.image.load(image).convert_alpha(), scale)
        self.name = image[:-4]
        self.owned = owned
        self.equipped = equipped



def draw_selector(screen, vehicle):
    sx, sy = screen.get_size()
    bx, by = hd.Background.get_size()
    vx, vy = vehicle.size
    Background = pg.transform.scale(hd.Background, ((sy/by)*bx, sy))
    screen.blit(Background, (0,0))
    screen.blit(vehicle.colour_surface, (4*sx/5-vx/2, (sy-vy)/2))
    screen.blit(vehicle.detail_surface, (4*sx/5-vx/2, (sy-vy)/2))
    nametag = hd.Title_Font.render(vehicle.name, True, (200, 200, 200))
    health = hd.Title_Font.render(str(vehicle.health) + " HP", True, (200, 200, 200))
    screen.blit(nametag, (sx/20, sy-sy/2-nametag.get_size()[1]/2))
    screen.blit(health, (sx-sx/20-health.get_size()[0], sy/8-health.get_size()[1]/2))
    for i in hd.buttons:
        i.process(screen)

def colour_test(event, bean):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_f:
            
            bean.colour(hd.colours["white"])
        if event.key == pg.K_g:
            
            bean.colour(hd.colours["black"])
        if event.key == pg.K_h:
            
            bean.colour(hd.colours["red"])
    

    
def main():
    run = True
    clock = pg.time.Clock()

    clock = pg.time.Clock()
    hd.vehicles = hd.cycler([vehicle("beancolour.png", "bean.png", hd.screen, health = 5),
    vehicle("jeepcolour.png", "jeep.png", hd.screen, health = 10),
    vehicle("bugatticolour.png", "bugatti.png", hd.screen, health = 10),
    vehicle("panthercolour.png", "panther.png", hd.screen, health = 50)])
    sx, sy = hd.screen.get_size()
    button_size = (100, 100)
    button = Button(sx-sx/5-button_size[0]/2,3*sy/4-button_size[1]/2, 100, 100, buttonImage = "down.png", onclickFunction = hd.vehicles.forward)
    button = Button(sx-sx/5-button_size[0]/2 ,sy/4-button_size[1]/2, 100, 100, buttonImage = "up.png", onclickFunction = hd.vehicles.reverse)
    button = Button(sx/2-3*button_size[0]/2,sy/4-button_size[1]/2, 100, 100, buttonImage = "left.png", onclickFunction = hd.colours_cycler.forward)
    button = Button(sx/2+1.5*button_size[0]/2 ,sy/4-button_size[1]/2, 100, 100, buttonImage = "right.png", onclickFunction = hd.colours_cycler.reverse)
    # Uncomment this for a non-translucent surface.
    # Uncomment this for a non-translucent surface.
    # surface = pg.Surface((100, 150), pg.SRCALPHA)
    # pg.draw.circle(surface, pg.Color(40, 240, 120), (50, 50), 50)  
    counter = 1
    while run:
        clock.tick(hd.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
        hd.vehicles.item.colour(hd.colours_cycler.item)
        draw_selector(hd.screen, hd.vehicles.item)

        pg.display.update()
        



if __name__ == '__main__':
    main()
    pg.quit()
 

