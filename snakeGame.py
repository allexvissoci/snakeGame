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
time.sleep(5)
