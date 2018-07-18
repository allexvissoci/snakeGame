# Snake Game Pygame

import pygame
import sys
import random
import time

check_errors = pygame.init()[1]

# Check for initializing errors
if check_errors > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors))
    sys.exit(-1)

# Play surface
playSourface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game!")

# Colors
red = pygame.Color(255, 0, 0) #gameover
blue = pygame.Color(0, 0, 255) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

# FPS controller
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodSpawn = True

direction = 'rigth'
changeTo = direction


# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSourface.blit(GOsurf, GOrect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()
