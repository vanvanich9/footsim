import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)

pygame.init()

k = 1

f = pygame.font.Font(None, 36 * k)
size = width, height = 1024 * k, 600 * k
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

names = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
goals = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

while pygame.event.wait().type != pygame.QUIT:
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, BLACK, (10 * k, 20 * k, 250 * k, 200 * k), 2)
    pygame.draw.line(screen, BLACK, [10 * k, 70 * k], [260 * k, 70 * k], 2)
    pygame.draw.line(screen, BLACK, [10 * k, 120 * k], [260 * k, 120 * k], 2)
    pygame.draw.line(screen, BLACK, [10 * k, 170 * k], [260 * k, 170 * k], 2)
    pygame.draw.line(screen, BLACK, [210 * k, 20 * k], [210 * k, 220 * k], 2)
    group_a = f.render('Группа A', 1, BLACK)
    screen.blit(group_a, (20, 240))

    pygame.draw.rect(screen, BLACK, (10 * k, 300 * k, 250 * k, 200 * k), 2)
    pygame.draw.line(screen, BLACK, [10 * k, 350 * k], [260 * k, 350 * k], 2)
    pygame.draw.line(screen, BLACK, [10 * k, 400 * k], [260 * k, 400 * k], 2)
    pygame.draw.line(screen, BLACK, [10 * k, 450 * k], [260 * k, 450 * k], 2)
    pygame.draw.line(screen, BLACK, [210 * k, 300 * k], [210 * k, 500 * k], 2)
    group_b = f.render('Группа B', 1, BLACK)
    screen.blit(group_b, (20, 520))

    pygame.draw.rect(screen, BLACK, (300 * k, 20 * k, 250 * k, 200 * k), 2)
    pygame.draw.line(screen, BLACK, [300 * k, 70 * k], [550 * k, 70 * k], 2)
    pygame.draw.line(screen, BLACK, [300 * k, 120 * k], [550 * k, 120 * k], 2)
    pygame.draw.line(screen, BLACK, [300 * k, 170 * k], [550 * k, 170 * k], 2)
    pygame.draw.line(screen, BLACK, [500 * k, 20 * k], [500 * k, 220 * k], 2)
    group_с = f.render('Группа С', 1, BLACK)
    screen.blit(group_с, (310, 240))

    pygame.draw.rect(screen, BLACK, (300 * k, 300 * k, 250 * k, 150 * k), 2)
    pygame.draw.line(screen, BLACK, [300 * k, 350 * k], [550 * k, 350 * k], 2)
    pygame.draw.line(screen, BLACK, [300 * k, 400 * k], [550 * k, 400 * k], 2)
    pygame.draw.line(screen, BLACK, [500 * k, 300 * k], [500 * k, 450 * k], 2)
    group_d = f.render('Группа третьих мест', 1, BLACK)
    screen.blit(group_d, (310, 470))

    team1 = f.render(names[0], 1, BLACK)
    team2 = f.render(names[1], 1, BLACK)
    team3 = f.render(names[2], 1, BLACK)
    team4 = f.render(names[3], 1, BLACK)
    team5 = f.render(names[4], 1, BLACK)
    team6 = f.render(names[5], 1, BLACK)
    team7 = f.render(names[6], 1, BLACK)
    team8 = f.render(names[7], 1, BLACK)
    team9 = f.render(names[8], 1, BLACK)
    team10 = f.render(names[9], 1, BLACK)
    team11 = f.render(names[10], 1, BLACK)
    team12 = f.render(names[11], 1, BLACK)
    team13 = f.render(names[12], 1, BLACK)
    team14 = f.render(names[13], 1, BLACK)
    team15 = f.render(names[14], 1, BLACK)

    goal1 = f.render(goals[0], 1, BLACK)
    goal2 = f.render(goals[1], 1, BLACK)
    goal3 = f.render(goals[2], 1, BLACK)
    goal4 = f.render(goals[3], 1, BLACK)
    goal5 = f.render(goals[4], 1, BLACK)
    goal6 = f.render(goals[5], 1, BLACK)
    goal7 = f.render(goals[6], 1, BLACK)
    goal8 = f.render(goals[7], 1, BLACK)
    goal9 = f.render(goals[8], 1, BLACK)
    goal10 = f.render(goals[9], 1, BLACK)
    goal11 = f.render(goals[10], 1, BLACK)
    goal12 = f.render(goals[11], 1, BLACK)
    goal13 = f.render(goals[12], 1, BLACK)
    goal14 = f.render(goals[13], 1, BLACK)
    goal15 = f.render(goals[14], 1, BLACK)

    screen.blit(team1, (20 * k, 35 * k))
    screen.blit(team2, (20 * k, 85 * k))
    screen.blit(team3, (20 * k, 135 * k))
    screen.blit(team4, (20 * k, 185 * k))

    screen.blit(team5, (20 * k, 315 * k))
    screen.blit(team6, (20 * k, 365 * k))
    screen.blit(team7, (20 * k, 415 * k))
    screen.blit(team8, (20 * k, 465 * k))

    screen.blit(team9, (310 * k, 35 * k))
    screen.blit(team10, (310 * k, 85 * k))
    screen.blit(team11, (310 * k, 135 * k))
    screen.blit(team12, (310 * k, 185 * k))

    screen.blit(team13, (310 * k, 315 * k))
    screen.blit(team14, (310 * k, 365 * k))
    screen.blit(team15, (310 * k, 415 * k))

    screen.blit(goal1, (220 * k, 35 * k))
    screen.blit(goal2, (220 * k, 85 * k))
    screen.blit(goal3, (220 * k, 135 * k))
    screen.blit(goal4, (220 * k, 185 * k))

    screen.blit(goal5, (220 * k, 315 * k))
    screen.blit(goal6, (220 * k, 365 * k))
    screen.blit(goal7, (220 * k, 415 * k))
    screen.blit(goal8, (220 * k, 465 * k))

    screen.blit(goal9, (510 * k, 35 * k))
    screen.blit(goal10, (510 * k, 85 * k))
    screen.blit(goal11, (510 * k, 135 * k))
    screen.blit(goal12, (510 * k, 185 * k))

    screen.blit(goal13, (510 * k, 315 * k))
    screen.blit(goal14, (510 * k, 365 * k))
    screen.blit(goal15, (510 * k, 415 * k))

    update = f.render('Обновить таблицу', 1, WHITE)
    pygame.draw.rect(screen, RED, (600 * k, 20 * k, 250 * k, 100 * k))
    screen.blit(update, (610 * k, 60 * k))
    pressed = bool(pygame.mouse.get_pressed()[0])
    x, y = map(int, pygame.mouse.get_pos())
    if x >= 600 and x <= 850 and y >= 20 and y <= 120 and pressed:
        i = 0
        fin = open("names_group.txt", "r")
        names = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        while True:
            line = fin.readline()
            if not line:
                break
            if '\n' in line:
                line = line[:-1]
            print(line)
            names[i] = line
            i += 1
        fin.close()
        i = 0
        fin = open("names_group.txt", "r")
        names = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        while True:
            line = fin.readline()
            if not line:
                break
            if '\n' in line:
                line = line[:-1]
            print(line)
            names[i] = line
            i += 1
        fin.close()
        i = 0
        fin = open("points_group.txt", "r")
        goals = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        while True:
            line = fin.readline()
            if not line:
                break
            if '\n' in line:
                line = line[:-1]
            print(line)
            goals[i] = line
            i += 1
        fin.close()

    update = f.render('Следующий этап', 1, WHITE)
    pygame.draw.rect(screen, GREEN, (600 * k, 300 * k, 250 * k, 100 * k))
    screen.blit(update, (610 * k, 340 * k))

    if 600 <= x <= 850 and 300 <= y <= 400 and pressed:
        break

    pygame.display.flip()

names = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
goals = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

while pygame.event.wait().type != pygame.QUIT:
    screen.fill((255, 255, 255))
    # Четвертьфинал
    pygame.draw.rect(screen, BLACK, (10 * k, 20 * k, 250 * k, 100 * k), 2)
    pygame.draw.line(screen, BLACK, [10 * k, 70 * k], [260 * k, 70 * k], 2)
    pygame.draw.line(screen, BLACK, [210 * k, 20 * k], [210 * k, 120 * k], 2)

    pygame.draw.rect(screen, BLACK, (10 * k, 150 * k, 250 * k, 100 * k), 2)
    pygame.draw.line(screen, BLACK, [10 * k, 200 * k], [260 * k, 200 * k], 2)
    pygame.draw.line(screen, BLACK, [210 * k, 150 * k], [210 * k, 250 * k], 2)

    pygame.draw.rect(screen, BLACK, (10 * k, 280 * k, 250 * k, 100 * k), 2)
    pygame.draw.line(screen, BLACK, [10 * k, 330 * k], [260 * k, 330 * k], 2)
    pygame.draw.line(screen, BLACK, [210 * k, 280 * k], [210 * k, 380 * k], 2)

    pygame.draw.rect(screen, BLACK, (10 * k, 410 * k, 250 * k, 100 * k), 2)
    pygame.draw.line(screen, BLACK, [10 * k, 460 * k], [260 * k, 460 * k], 2)
    pygame.draw.line(screen, BLACK, [210 * k, 410 * k], [210 * k, 510 * k], 2)

    pygame.draw.line(screen, BLACK, [260 * k, 70 * k], [280 * k, 70 * k], 2)
    pygame.draw.line(screen, BLACK, [260 * k, 200 * k], [280 * k, 200 * k], 2)
    pygame.draw.line(screen, BLACK, [260 * k, 330 * k], [280 * k, 330 * k], 2)
    pygame.draw.line(screen, BLACK, [260 * k, 460 * k], [280 * k, 460 * k], 2)

    pygame.draw.line(screen, BLACK, [280 * k, 70 * k], [280 * k, 200 * k], 2)
    pygame.draw.line(screen, BLACK, [280 * k, 330 * k], [280 * k, 460 * k], 2)

    pygame.draw.line(screen, BLACK, [280 * k, 135 * k], [300 * k, 135 * k], 2)
    pygame.draw.line(screen, BLACK, [280 * k, 395 * k], [300 * k, 395 * k], 2)

    # Полуфинал

    pygame.draw.rect(screen, BLACK, (300 * k, 85 * k, 250 * k, 100 * k), 2)
    pygame.draw.line(screen, BLACK, [300 * k, 135 * k], [550 * k, 135 * k], 2)
    pygame.draw.line(screen, BLACK, [500 * k, 85 * k], [500 * k, 185 * k], 2)

    pygame.draw.rect(screen, BLACK, (300 * k, 345 * k, 250 * k, 100 * k), 2)
    pygame.draw.line(screen, BLACK, [300 * k, 395 * k], [550 * k, 395 * k], 2)
    pygame.draw.line(screen, BLACK, [500 * k, 345 * k], [500 * k, 445 * k], 2)

    pygame.draw.line(screen, BLACK, [550 * k, 135 * k], [570 * k, 135 * k], 2)
    pygame.draw.line(screen, BLACK, [550 * k, 395 * k], [570 * k, 395 * k], 2)

    pygame.draw.line(screen, BLACK, [570 * k, 135 * k], [570 * k, 395 * k], 2)

    pygame.draw.line(screen, BLACK, [570 * k, 265 * k], [590 * k, 265 * k], 2)

    # Финал

    pygame.draw.rect(screen, BLACK, (590 * k, 215 * k, 250 * k, 100 * k), 2)
    pygame.draw.line(screen, BLACK, [590 * k, 265 * k], [840 * k, 265 * k], 2)
    pygame.draw.line(screen, BLACK, [790 * k, 215 * k], [790 * k, 315 * k], 2)

    # Матч за третье место

    pygame.draw.rect(screen, BLACK, (590 * k, 400 * k, 250 * k, 100 * k), 2)
    pygame.draw.line(screen, BLACK, [590 * k, 450 * k], [840 * k, 450 * k], 2)
    pygame.draw.line(screen, BLACK, [790 * k, 400 * k], [790 * k, 500 * k], 2)

    f = pygame.font.Font(None, 36 * k)
    quarterfinal = f.render('Четвертьфинал', 1, (180, 0, 0))
    semifinal = f.render('Полуфинал', 1, (180, 0, 0))
    final = f.render('Финал', 1, (180, 0, 0))
    third = f.render('Матч за третье место', 1, (180, 0, 0))

    screen.blit(quarterfinal, (20 * k, 530 * k))
    screen.blit(semifinal, (310 * k, 465 * k))
    screen.blit(final, (600 * k, 335 * k))
    screen.blit(third, (600 * k, 530 * k))

    team1 = f.render(names[0], 1, BLACK)
    team2 = f.render(names[1], 1, BLACK)
    team3 = f.render(names[2], 1, BLACK)
    team4 = f.render(names[3], 1, BLACK)
    team5 = f.render(names[4], 1, BLACK)
    team6 = f.render(names[5], 1, BLACK)
    team7 = f.render(names[6], 1, BLACK)
    team8 = f.render(names[7], 1, BLACK)
    team9 = f.render(names[8], 1, BLACK)
    team10 = f.render(names[9], 1, BLACK)
    team11 = f.render(names[10], 1, BLACK)
    team12 = f.render(names[11], 1, BLACK)
    team13 = f.render(names[12], 1, BLACK)
    team14 = f.render(names[13], 1, BLACK)
    team15 = f.render(names[14], 1, BLACK)
    team16 = f.render(names[15], 1, BLACK)

    goal1 = f.render(goals[0], 1, BLACK)
    goal2 = f.render(goals[1], 1, BLACK)
    goal3 = f.render(goals[2], 1, BLACK)
    goal4 = f.render(goals[3], 1, BLACK)
    goal5 = f.render(goals[4], 1, BLACK)
    goal6 = f.render(goals[5], 1, BLACK)
    goal7 = f.render(goals[6], 1, BLACK)
    goal8 = f.render(goals[7], 1, BLACK)
    goal9 = f.render(goals[8], 1, BLACK)
    goal10 = f.render(goals[9], 1, BLACK)
    goal11 = f.render(goals[10], 1, BLACK)
    goal12 = f.render(goals[11], 1, BLACK)
    goal13 = f.render(goals[12], 1, BLACK)
    goal14 = f.render(goals[13], 1, BLACK)
    goal15 = f.render(goals[14], 1, BLACK)
    goal16 = f.render(goals[15], 1, BLACK)

    # Вывод команд

    screen.blit(team1, (20 * k, 35 * k))
    screen.blit(team2, (20 * k, 85 * k))
    screen.blit(team3, (20 * k, 165 * k))
    screen.blit(team4, (20 * k, 215 * k))
    screen.blit(team5, (20 * k, 295 * k))
    screen.blit(team6, (20 * k, 345 * k))
    screen.blit(team7, (20 * k, 425 * k))
    screen.blit(team8, (20 * k, 475 * k))

    screen.blit(team9, (310 * k, 100 * k))
    screen.blit(team10, (310 * k, 150 * k))
    screen.blit(team11, (310 * k, 360 * k))
    screen.blit(team12, (310 * k, 410 * k))

    screen.blit(team13, (600 * k, 230 * k))
    screen.blit(team14, (600 * k, 280 * k))

    screen.blit(team15, (600 * k, 415 * k))
    screen.blit(team16, (600 * k, 465 * k))

    # Вывод голов

    screen.blit(goal1, (220 * k, 35 * k))
    screen.blit(goal2, (220 * k, 85 * k))
    screen.blit(goal3, (220 * k, 165 * k))
    screen.blit(goal4, (220 * k, 215 * k))
    screen.blit(goal5, (220 * k, 295 * k))
    screen.blit(goal6, (220 * k, 345 * k))
    screen.blit(goal7, (220 * k, 425 * k))
    screen.blit(goal8, (220 * k, 475 * k))

    screen.blit(goal9, (510 * k, 100 * k))
    screen.blit(goal10, (510 * k, 150 * k))
    screen.blit(goal11, (510 * k, 360 * k))
    screen.blit(goal12, (510 * k, 410 * k))

    screen.blit(goal13, (800 * k, 230 * k))
    screen.blit(goal14, (800 * k, 280 * k))

    screen.blit(goal15, (800 * k, 415 * k))
    screen.blit(goal16, (800 * k, 465 * k))

    update = f.render('Обновить таблицу', 1, WHITE)
    pygame.draw.rect(screen, RED, (600 * k, 20 * k, 250 * k, 100 * k))
    screen.blit(update, (610 * k, 60 * k))
    pressed = bool(pygame.mouse.get_pressed()[0])
    x, y = map(int, pygame.mouse.get_pos())
    if x >= 600 and x <= 850 and y >= 20 and y <= 120 and pressed:
        i = 0
        fin = open("names.txt", "r")
        names = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        while True:
            line = fin.readline()
            if not line:
                break
            if '\n' in line:
                line = line[:-1]
            print(line)
            names[i] = line
            i += 1
        fin.close()
        i = 0
        fin = open("goals.txt", "r")
        goals = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        while True:
            line = fin.readline()
            if not line:
                break
            if '\n' in line:
                line = line[:-1]
            print(line)
            goals[i] = line
            i += 1
        fin.close()
    pygame.display.flip()
pygame.quit()
