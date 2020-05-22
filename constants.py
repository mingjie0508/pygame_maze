# imports and constants
import pygame as pg
import pytmx
import sys
import time
import math
import random

# font: rainy days
RAINY_DAYS = 'STHUPO.ttf'

# some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (20, 20, 20)
LIGHTGREY = (100, 100, 100)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 70
TITLE = "Hidden Pears"

TILESIZE = 64

# player settings
PLAYER_SCALE = 0.9
PLAYER_SPEED = 130
DIAGONAL_SPEED_FACTOR = 0.7071
PLAYER_LEFT = "Maze_Images\player_left.png"
PLAYER_RIGHT = "Maze_Images\player_right.png"
PLAYER_UP = "Maze_Images\player_up.png"
PLAYER_DOWN = "Maze_Images\player_down.png"

# timer settings
GAME_MINUTES = 9
GAME_SECONDS = 1

# end stage
END_LEFT = 13 * TILESIZE
END_RIGHT = 17 * TILESIZE
END_UP = 11 * TILESIZE
END_DOWN = 16 * TILESIZE

# pears
# a tuple that holds all the potential x,y co-ordinates of pears
# [x1, y1, x2, y2, ... x15, y15]
PEAR = "Maze_Images\pear_framed.png"
PEAR_TUPLE = (18, 60, 23, 14, 25, 20, 37, 67, 39, 14, 41, 68, 43, 36, 49, 60,
              49, 22, 49, 48, 51, 45, 63, 42, 65, 30, 69, 8, 71, 62)

# score text
SCORE_X = 2 * TILESIZE
SCORE_Y = int(HEIGHT-TILESIZE/2)
