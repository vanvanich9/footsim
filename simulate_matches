from random import randrange
import pygame
import time as tm
import sys


def simulate(rate1, rate2):
    max_goals1 = 3
    max_goals2 = 3
    if rate1 > rate2:
        max_goals1 += (rate1 - rate2) // 5
        max_goals2 = max(1, max_goals2 - (rate1 - rate2) // 10)
    else:
        max_goals2 += (rate2 - rate1) // 5
        max_goals1 = max(1, max_goals1 - (rate2 - rate1) // 10)
    return randrange(0, max_goals1 + 1, 1), randrange(0, max_goals2 + 1, 1)


def simulate_game_with_monemts(g1, g2):
    timecode = {i: [] for i in range(1, 91)}
    for i in range(g1):
        time = randrange(1, 91, 1)
        timecode[time].append(1)
    for i in range(g2):
        time = randrange(1, 91, 1)
        timecode[time].append(2)
    return timecode

pygame.init()

BLACK = pygame.Color('Black')

f = pygame.font.Font(None, 36)
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('White'))
g1, g2 = simulate(76, 80)
timecodes = simulate_game_with_monemts(g1, g2)
print(timecodes)
goal1, goal2 = 0, 0
start_time = tm.time()
j = 0
h_start = 60
pygame.display.update()
while True:
    goal1, goal2 = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if j < 90:
        while tm.time() - start_time < 0.4:
            pygame.display.update()
        start_time = tm.time()
        j += 1
    h_start = 80
    screen.fill((255, 255, 255))
    f2 = pygame.font.SysFont('arial', 24)
    team1 = f2.render("Луч", 1, BLACK)
    screen.blit(team1, (10, 20))
    team2 = f2.render("Зенит", 1, BLACK)
    screen.blit(team2, (500, 20))
    pygame.draw.line(screen, BLACK, (0, 50), (600, 50), 2)
    pygame.draw.line(screen, BLACK, (0, 0), (600, 0), 2)
    pygame.draw.line(screen, BLACK, (300, 0), (300, 50), 2)
    now_time = f2.render(str(j), 1, BLACK)
    screen.blit(now_time, (285, 60))
    f2 = pygame.font.SysFont('arial', 18)
    for i in range(1, j + 1):
        for u in timecodes[i]:
            text = f2.render(str(i) + str(' ГОЛ'), 1, BLACK)
            if u == 1:
                screen.blit(text, (10, h_start))
                goal1 += 1
            else:
                screen.blit(text, (500, h_start))
                goal2 += 1
            h_start += 25
    f2 = pygame.font.SysFont('arial', 24)
    score1 = f2.render(str(goal1), 1, BLACK)
    score2 = f2.render(str(goal2), 1, BLACK)
    screen.blit(score1, (280, 20))
    screen.blit(score2, (309, 20))
    pygame.display.update()
