from constants import *

class TileMap:
    # open a tmx tiled map file and initiate some variables
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    # render tile map
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile,(x * self.tmxdata.tilewidth,
                                     y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
            
class Button:
    def __init__(self, game, x, y, width, height, action = None):
        self.mouse = pg.mouse.get_pos()
        self.click = pg.mouse.get_pressed()
        # print(self.mouse)
        # print the co-ordinates of the mouse when developing the buttons
        if x + width > self.mouse[0] > x and y + height > self.mouse[1] > y:
            self.surface = pg.Surface((width, height))
            self.surface.set_alpha(128) # set transparency
            self.surface.fill(LIGHTGREY)
            game.screen.blit(self.surface, (x, y))
            # the button will be highlighted when the pointer hovers over it
                          
            if self.click[0] == 1:
                action()

class Text:
    def __init__(self, game, text, size, x, y):
        largeText = pg.font.Font(RAINY_DAYS, size)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (x, y) # co-ordinates of the centre
        game.screen.blit(TextSurf, TextRect) # blit text to the screen

    def text_objects(self, text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()
