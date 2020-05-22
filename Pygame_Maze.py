# Reference:
# https://github.com/kidscancode/pygame_tutorials/tree/master/tilemap/part%2013

from camera import *
from obj import *
from player import *
from visual import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        self.player_left = pg.image.load(PLAYER_LEFT)
        self.player_right = pg.image.load(PLAYER_RIGHT)
        self.player_up = pg.image.load(PLAYER_UP)
        self.player_down = pg.image.load(PLAYER_DOWN)
        self.pear = pg.image.load(PEAR)
        self.map = TileMap("Maze.tmx")
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        
        self.intro_image = pg.image.load("Maze_Images\intro_image.png")
        self.instruction_image = pg.image.load("Maze_Images\instruction.png")
        self.congrats_image = pg.image.load("Maze_Images\go_image.png")

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.walls = pg.sprite.Group()
        self.pears = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()

        # set up the score counter
        self.score = 0
        
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "player":
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == "wall":
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)

        # set up the pears
        random_list = random.sample(range(0, 15), 5)
        # randomly choose 5 pairs of co-ordinates and put them into a list
        # print(random_list)
        # print the random_list for test
        for i in range(5):
            Pear(self, PEAR_TUPLE[2*random_list[i]], PEAR_TUPLE[1+2*random_list[i]])
        # iterate random_list and render pears in place    
        self.camera = Camera(self.map.width, self.map.height)

        # set up the timer
        self.minutes = GAME_MINUTES
        self.seconds = GAME_SECONDS
        
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            # divide 1000 to convert the time passed from milliseconds to seconds
            if self.seconds < 0:
                self.minutes -= 1
                self.seconds += 60
                # calculate the time left
            self.time_left = (str(self.minutes).rjust(2, "0") + ":" +
                              str(math.floor(self.seconds)).rjust(2, "0"))
            # math. floor function rounds it down and produces nice whole numbers
            # store the value of count down timer in the format "xx:xx"
            self.seconds -= self.dt

            self.events()
            self.update()
            self.draw()
             
    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of game_loop
        self.all_sprites.update()
        self.camera.update(self.player)
        
    def draw(self):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # draw sprites
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # draw score
        Text(self, "Score: "+str(self.score), TILESIZE, SCORE_X, SCORE_Y)
        # draw game over and go back to main menu if time is over
        if self.minutes == 0 and math.floor(self.seconds) == 0:
            Text(self, "GAME OVER", TILESIZE, WIDTH/2, HEIGHT/2)
            Text(self, "0 PEARS", TILESIZE, WIDTH/2, HEIGHT/2 - 64)
            pg.display.flip()
            time.sleep(4)
            self.show_start_screen()
        # draw time
        Text(self, self.time_left, TILESIZE, 128, 64)
        
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
            
    def show_start_screen(self):
        while True:
            self.events()

            self.screen.blit(self.intro_image, (0, 0))
            # blit start menu image
            Button(self, 425, 390, 175, 70, self.show_instruction)
            # play button
            
            pg.display.update()
            self.clock.tick(15)

    def show_instruction(self):
        while True:
            self.events()

            self.screen.blit(self.instruction_image, (0, 0))
            # blit instruction image
            pg.display.update()
            self.clock.tick(15)
            
            keys = pg.key.get_pressed()
            if (keys[pg.K_LEFT] or keys[pg.K_RIGHT]
                or keys[pg.K_UP] or keys[pg.K_DOWN]):
                self.game_loop()
                # press any arrow key to start the game
            
    def show_go_screen(self):
        while True:
            self.events()

            self.screen.blit(self.congrats_image, (0, 0))
            # blit finish menu image
            Text(self, str(self.score), 64, 590, 285)
            # blit text in the gap
            for n in range(self.score):
                self.screen.blit(self.pear,(270+100*n, 128))
                # blit the right number of pears
            Button(self, 375, 490, 275, 50, self.show_start_screen)
            # main menu button
            
            pg.display.update()
            self.clock.tick(15)
            
    def game_loop(self):
        self.new()
        self.run()
        self.show_go_screen()
        
# start the game loop
g = Game()

g.show_start_screen()
