import pygame
import sys

pygame.init()
BLACK = pygame.Color('Black')
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('White'))
teams = [['Зенит', 0], ['Краснодар', 0], ['Ростов', 0], ['ПФК ЦСКА', 0], ['Локомотив', 0], ['Арсенал', 0], ['Уфа', 0],
           ['Динамо', 0], ['Урал', 0], ['Спартак', 0], ['Тамбов', 0], ['Ахмат', 0], ['Рубин', 0], ['Оренбург', 0],
           ['Крылья Советов', 0], ['Луч', 0]]
matches = {'Зенит': [0, 0, 0], 'Краснодар': [0, 0, 0], 'Ростов': [0, 0, 0], 'ПФК ЦСКА': [0, 0, 0], 'Локомотив': [0, 0, 0], 'Арсенал': [0, 0, 0], 'Уфа': [0, 0, 0],
           'Динамо': [0, 0, 0], 'Урал': [0, 0, 0], 'Спартак': [0, 0, 0], 'Тамбов': [0, 0, 0], 'Ахмат': [0, 0, 0], 'Рубин': [0, 0, 0], 'Оренбург': [0, 0, 0],
           'Крылья Советов': [0, 0, 0], 'Луч': [0, 0, 0]}
while True:
    screen.fill(pygame.Color('White'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen, BLACK, (10, 10, 550, 578), 2)
    h = 10
    for i in range(16):
        h += 34
        pygame.draw.line(screen, BLACK, [10, h], [560, h], 2)
    h = 20
    f2 = pygame.font.SysFont('arial', 18)
    for i in range(17):
        if i == 0:
            text = '№'
            team = 'Команды'
            point = 'О'
            win = 'В'
            lose = 'П'
            draw = 'Н'
        else:
            text = str(i)
            team = teams[i - 1][0]
            point = str(teams[i - 1][1])
            win = str(matches[teams[i - 1][0]][0])
            lose = str(matches[teams[i - 1][0]][2])
            draw = str(matches[teams[i - 1][0]][1])
        Text = f2.render(team, 1, BLACK)
        screen.blit(Text, (45, h))
        Text = f2.render(point, 1, BLACK)
        screen.blit(Text, (535, h))
        Text = f2.render(text, 1, BLACK)
        screen.blit(Text, (15, h))
        Text = f2.render(win, 1, BLACK)
        screen.blit(Text, (505, h))
        Text = f2.render(lose, 1, BLACK)
        screen.blit(Text, (445, h))
        Text = f2.render(draw, 1, BLACK)
        screen.blit(Text, (475, h))
        h += 34

    pygame.draw.line(screen, BLACK, [40, 10], [40, 588], 2)
    pygame.draw.line(screen, BLACK, [530, 10], [530, 588], 2)
    pygame.draw.line(screen, BLACK, [500, 10], [500, 588], 2)
    pygame.draw.line(screen, BLACK, [470, 10], [470, 588], 2)
    pygame.draw.line(screen, BLACK, [440, 10], [440, 588], 2)
    pygame.display.flip()
