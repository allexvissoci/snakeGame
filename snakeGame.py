# Snake Game Pygame

import pygame
import sys
import random
import time
import json
import datetime
import os

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")
    name = input("Say your name: ")


# Colors
red = pygame.Color(255, 0, 0)  # gameover
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

playSurface = pygame.display.set_mode((720, 460))


def indexFunction():
    # Play surface
    score = 0
    fpsSpeed = 10
    pause = False
    pygame.display.set_caption('Snake game!')

    # FPS controller
    fpsController = pygame.time.Clock()

    # Important variables
    snakePos = [100, 50]
    snakeBody = [[100, 50], [90, 50], [80, 50]]

    foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
    foodSpawn = True

    direction = 'RIGHT'
    changeto = direction

    # Main Logic of the gameOver
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    changeto = 'RIGHT'
                    fpsSpeed *= 2
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    changeto = 'LEFT'
                    fpsSpeed *= 2
                if event.key == pygame.K_UP or event.key == ord('w'):
                    changeto = 'UP'
                    fpsSpeed *= 2
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    changeto = 'DOWN'
                    fpsSpeed *= 2
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.key == pygame.K_SPACE:
                    pause = True
                    while pause:
                        time.sleep(0.1)
                        for event1 in pygame.event.get():
                            if event1.key == pygame.K_SPACE:
                                if pause:
                                    pause = False
                                    break
            elif event.type == pygame.KEYUP:
                fpsSpeed /= 2
            fpsController.tick(fpsSpeed)

        # Validation of direction
        if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = changeto
        if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = changeto
        if changeto == 'UP' and not direction == 'DOWN':
            direction = changeto
        if changeto == 'DOWN' and not direction == 'UP':
            direction = changeto

        # Update snake position [x, y]
        if direction == 'RIGHT':
            snakePos[0] += 10
        if direction == 'LEFT':
            snakePos[0] -= 10
        if direction == 'UP':
            snakePos[1] -= 10
        if direction == 'DOWN':
            snakePos[1] += 10

        # Snake Body mechanism
        snakeBody.insert(0, list(snakePos))
        if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
            score += 1
            if score % 5 == 0:
                fpsSpeed += fpsSpeed * 0.1
            foodSpawn = False
        else:
            snakeBody.pop()

        # Food Spawn
        if foodSpawn is False:
            foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
        foodSpawn = True

        # Background
        playSurface.fill(black)

        # Draw Snake
        for pos in snakeBody:
            pygame.draw.rect(playSurface, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(playSurface, red,
                         pygame.Rect(foodPos[0], foodPos[1], 10, 10))

        if snakePos[0] > 710 or snakePos[0] < 0:
            gameOver(score)
        if snakePos[1] > 450 or snakePos[1] < 0:
            gameOver(score)

        # Self hit
        for block in snakeBody[1:]:
            if snakePos[0] == block[0] and snakePos[1] == block[1]:
                gameOver(score)

        showScore(score)
        pygame.display.flip()
        fpsController.tick(fpsSpeed)


# Game over function
def gameOver(score):
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    saveRanking(score)
    showRanking()
    showScore(score, 0)
    pygame.display.flip()
    time.sleep(3)
    indexFunction()


def showScore(score, choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score), True, white)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 70)
    playSurface.blit(Ssurf, Srect)


def saveRanking(score):
    file = open("scoreRanking.txt", "r")
    ranking = []

    if os.stat("scoreRanking.txt").st_size > 0:
        ranking = json.loads(file.read())
        file.close()

    date = datetime.datetime.now().strftime('%Y-%m-%d')
    newScore = {"name": name, "date": date, "score": score}
    ranking.append(newScore)

    file = open("scoreRanking.txt", "w")
    file.write(json.dumps(ranking))
    file.close()


def showRanking():
    file = open("scoreRanking.txt", "r")
    sortedList = sorted(json.loads(file.read()), key=lambda k: k['score'],
                        reverse=True)
    file.close()

    sFont = pygame.font.SysFont('monaco', 21)
    posY = 120
    i = 0
    for v in sortedList:
        if(i < 5):
            ranking = '{0} - {1}  {2}  {3}'.format(i+1, v['score'], v['date'], v['name'])
            Ssurf = sFont.render('{0}'.format(ranking), True, white)
            Srect = Ssurf.get_rect()
            Srect.midtop = (360, posY)
            Srect.midleft = (280, posY)
            posY = posY + (2 * 21)
            i += 1
            playSurface.blit(Ssurf, Srect)


indexFunction()
