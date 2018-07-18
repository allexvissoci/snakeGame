# Snake Game Pygame

import pygame
import sys
import random
import time

check_errors = pygame.init()[1]

# check for initializing errors
if check_errors > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors))
    sys.exit(-1)

# Play surface
playSourface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game!")

# Colors
red = pygame.Color(255, 0, 0) # gameover
blue = pygame.Color(0, 0, 255) # snake
black = pygame.Color(0, 0, 0) # score
white = pygame.Color(255, 255, 255) # background
brown = pygame.Color(165, 42, 42) # food
