from constants import *

# player settings
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_down
        self.image = pg.transform.scale(self.image,
                                        (int(PLAYER_SCALE * TILESIZE),
                                         int(PLAYER_SCALE * TILESIZE)))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
            
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.image = self.game.player_left # player facing left
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT]:
            self.image = self.game.player_right # player facing right
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP]:
            self.image = self.game.player_up # player facing up
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN]:
            self.image = self.game.player_down # player facing down
            self.vy = PLAYER_SPEED
        if self.vx < 0 and self.vy != 0:
            self.image = self.game.player_left
            self.vx *= DIAGONAL_SPEED_FACTOR
            self.vy *= DIAGONAL_SPEED_FACTOR
        elif self.vx > 0 and self.vy != 0:
            self.image = self.game.player_right
            self.vx *= DIAGONAL_SPEED_FACTOR
            self.vy *= DIAGONAL_SPEED_FACTOR # 1/sqrt(2)
            # x and y component of diagonal speed

        
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def collide_with_pear(self):
        if pg.sprite.spritecollide(self, self.game.pears, True):
            self.game.score += 1
            # if the player collides with a pear, that pear will disappear,
            #   due to the third argument (True) of the spritecollide function
            # score increases by 1
        
    def update(self):
        self.collide_with_pear()
        self.get_keys()
        self.x += self.vx * self.game.dt # moving left and right
        self.y += self.vy * self.game.dt # moving up and down
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
        
        if END_LEFT < self.x < END_RIGHT and END_UP < self.y < END_DOWN:
            time.sleep(1)
            self.game.show_go_screen()
            # the game ends when the player gets to certain area
