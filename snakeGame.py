# Snake Game Pygame

import pygame
import sys
import random
import time

check_errors = pygame.init()[1]

if check_errors > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")
