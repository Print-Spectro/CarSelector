import pygame as pg
import header as hd
def test():
    print("test_success")
def next(pos, sequence):
    "if pos"
    

def last(sequence):
    "a"


def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pg.Color(r, g, b, a))

class Button():
    def __init__(self, x, y, width, height, buttonText="Button", onclickFunction=None, onePress=False, buttonImage = None, button_list = True):
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
            self.buttonSurf = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', buttonImage)).convert_alpha(), hd.scale)
        elif buttonText != None:
            self.buttonSurf = hd.Text_Font.render(buttonText, True, (20, 20, 20))  
        if button_list:
            hd.buttons.append(self)

    def process(self, screen, **kwargs):
        """
        Tracks mouse location and if mouse intersects with the button there is a colour change.
        Upon click 
        """
        mousePos = pg.mouse.get_pos()
        self.buttonSurface.fill((self.fillColors['normal']))
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
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
                 owned = False):
       
        self.colour_surface = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', colour_image)).convert_alpha(), hd.scale)
        self.detail_surface = pg.transform.scale_by(pg.image.load(hd.os.path.join('assets', detail_image)).convert_alpha(), hd.scale)
        self.size = self.colour_surface.get_size()
        self.price = price
        self.button = Button(hd.sx/2-hd.button_size[0]*3.5/2, hd.sy/2-hd.button_size[1]/2, hd.button_size[0]*3.5, hd.button_size[1], buttonText = "Buy £" + str(self.price), button_list = False)
        self.name = detail_image[:-4]
        self.health = health
        self.speed = speed
        self.handling = handling
        self.owned = owned
        self.position = position
        self.colour = (200,200,200)
        self.set_colour((200,200,200))
    def set_colour(self, colour):
        """
        Input: colour name string in white black red yellow green blue
        Result: changes colour of all pixels in colour layer
        """
        fill(self.colour_surface, pg.Color(colour))
        self.colour = colour

    def handle_movement(self):
        "up"
        "down"

    def draw(self, screen):

        "a"

    def purchase(self):
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
    money = hd.Title_Font.render("£ " + str(hd.dinero), True, (200, 200, 200))
    screen.blit(nametag, (sx/20, sy-sy/2-nametag.get_size()[1]/2))
    screen.blit(health, (sx-sx/20-health.get_size()[0], sy/8-health.get_size()[1]/2))
    screen.blit(money, (sx/20, sy/8-health.get_size()[1]/2))
    vehicle.button.process(screen)
    for i in hd.buttons:
        i.process(screen)


    
def colour_selector():
    bx, by = hd.button_size
    sx, sy = hd.screen.get_size()
    c = 0
    for i in hd.colours:
        Button_i = Button(c*sx/(len(hd.colours)*2)+sx/4,5*sy/6-by/2, bx, by, buttonText="", onclickFunction = hd.colours[i].colour_set)
        colour = hd.colours[i].colour
        Button_i.fillColors["normal"] = colour
        colour_i = pg.Color(colour)
        h, s, l, a = colour_i.hsla
        colour_i.hsla = h, s/2, l+(100-l)/2, a
        Button_i.fillColors["hover"] = colour_i
        Button_i.fillColors["pressed"] = colour
        c+=1
    
def main():
    run = True
    clock = pg.time.Clock()
    sx, sy = hd.screen.get_size()
    button_size = hd.button_size
    Button(sx-sx/5-button_size[0]/2,3*sy/4-button_size[1]/2, button_size[0], button_size[1], buttonImage = "down.png", onclickFunction = hd.vehicles.forward)
    Button(sx-sx/5-button_size[0]/2 ,sy/4-button_size[1]/2, button_size[0], button_size[1], buttonImage = "up.png", onclickFunction = hd.vehicles.reverse)
    colour_selector()
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

        

        draw_selector(hd.screen, hd.vehicles.item)

        pg.display.update()
        



if __name__ == '__main__':
    main()
    pg.quit()
 

