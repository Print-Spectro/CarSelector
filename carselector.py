import pygame as pg
import header as hd



def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pg.Color(r, g, b, a))

class vehicle:
    def __init__(self, colour_image, detail_image, health = 10, speed = 10, handling = 10, price = 100, owned = True):
        self.colour_surface = pg.transform.scale_by(pg.image.load(colour_image).convert_alpha(), 10)
        self.detail_surface = pg.transform.scale_by(pg.image.load(detail_image).convert_alpha(), 10)
        self.name = detail
        self.health = health
        self.speed = speed
        self.handling = handling
        self.price = price
        self.owned = owned
    
    def colour(self, colour):
        """
        Input: colour name string in white black red yellow green blue
        Result: changes colour of all pixels in colour layer
        """
        fill(self.colour_surface, pg.Color(colour))


def draw(vehicle, mode):
    "a"

    




 



def main():
    run = True
    clock = pg.time.Clock()
    screen = DISPLAYSURF = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()
    bean = vehicle("assets/panthercolour.png", "assets/panther.png")
    # Uncomment this for a non-translucent surface.
    # surface = pg.Surface((100, 150), pg.SRCALPHA)
    # pg.draw.circle(surface, pg.Color(40, 240, 120), (50, 50), 50)
    surface = pg.image.load('assets/bugatticolour.png').convert_alpha()
    overlay = pg.image.load("assets/bugatti.png").convert_alpha()
    surface = pg.transform.rotozoom(surface, 180, 1)
    surface = pg.transform.scale_by(surface, 10)

    done = False
    counter = 1
    while run:
        clock.tick(hd.FPS)
        print(counter)
        counter += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    fill(surface, pg.Color(hd.colours["white"]))
                    bean.colour(hd.colours["white"])
                if event.key == pg.K_g:
                    fill(surface, pg.Color(hd.colours["black"]))
                    bean.colour(hd.colours["black"])
                if event.key == pg.K_h:
                    fill(surface, pg.Color(hd.colours["red"]))
                    bean.colour(hd.colours["red"])

        screen.fill(pg.Color('lightskyblue4'))
        pg.draw.rect(screen, (40, 50, 50), (0, 0, 50, 50))
        surface.blit(overlay, (100,100))
        screen.blit(surface, (100, 200))
       
        pg.draw.rect(surface, pg.Color(40, 50, 50), (0, 0, 50, 50))
        #bean.colour_surface.blit(bean.detail_surface, (0,0))
        screen.blit(bean.colour_surface, (0,0))
        screen.blit(bean.detail_surface, (0,0))
        #bean.colour_surface.blit(bean.detail_surface, (0,0))
        pg.display.update()



if __name__ == '__main__':
    

    main()
    pg.quit()
 
pygame.quit()
quit()