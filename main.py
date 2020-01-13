from random import randrange
import time as tm


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

name_team = 'Луч'
rate = 54
ratings = {'Зенит': 80, 'Краснодар': 78, 'Ростов': 70, 'ПФК ЦСКА': 76, 'Локомотив': 77, 'Арсенал': 65, 'Уфа': 65,
           'Динамо': 69, 'Урал': 63, 'Спартак': 72,
           'Тамбов': 60, 'Ахмат': 58, 'Рубин': 61, 'Оренбург': 57, 'Крылья Советов': 55, 'Луч': 77}
teams = ['Зенит', 'Краснодар', 'Ростов', 'ПФК ЦСКА', 'Локомотив', 'Арсенал', 'Уфа', 'Динамо', 'Урал', 'Спартак',
         'Тамбов', 'Ахмат', 'Рубин', 'Оренбург', 'Крылья Советов', 'Луч']
divisions = [
    [['Зенит', 0], ['Краснодар', 0], ['Ростов', 0], ['ПФК ЦСКА', 0], ['Локомотив', 0], ['Арсенал', 0], ['Уфа', 0],
     ['Динамо', 0], ['Урал', 0], ['Спартак', 0], ['Тамбов', 0], ['Ахмат', 0], ['Рубин', 0], ['Оренбург', 0],
     ['Крылья Советов', 0], ['Сочи', 0]]
]
cup = []


def set_result(code1, code2, goal1, goal2):
    a1, b1, c1 = code1
    a2, b2, c2 = code2
    if goal1 > goal2:
        divisions[a1][b1][c1] += 3
    if goal1 < goal2:
        divisions[a2][b2][c2] += 3
    if goal1 == goal2:
        divisions[a1][b1][c1] += 1
        divisions[a2][b2][c2] += 1


def generate_pairs(team):
    c = []
    for i in range(len(team) // 2):
        l = len(team)
        index1 = randrange(0, l, 1)
        t1 = team.pop(index1)
        l -= 1
        index2 = randrange(0, l, 1)
        t2 = team.pop(index2)
        c.append([t1, t2])
    return c


def make_new_pairs(team):
    c = []
    for i in range(len(team) // 2):
        team1 = team.pop(0)
        team2 = team.pop(0)
        c.append([team1, team2])
    return c


def play_cup_pairs(pairs):
    next_tour = []
    for team1, team2 in pairs:
        g1, g2 = simulate(ratings[team1], ratings[team2])
        if g1 == g2:
            itog_goal = randrange(0, 2, 1)
            if itog_goal == 0:
                g1 += 1
            else:
                g2 += 1
        print(team1 + ' - ' + team2 + ' ' + str(g1) + ':' + str(g2))
        if g1 > g2:
            next_tour.append(team1)
        else:
            next_tour.append(team2)
    return next_tour

cup_teams = teams
j = 0
while len(cup_teams) > 1:
    word = '1' '/' + str(len(cup_teams) // 2)
    if word == '1/4':
        print("Четвертьфинал")
    elif word == '1/2':
        print('Полуфинал')
    elif word == '1/1':
        print('Финал')
    else:
        print(word)
    print('----------------')
    if j == 0:
        cup = generate_pairs(cup_teams)
    else:
        cup = make_new_pairs(cup_teams)
    j += 1
    cup_teams = play_cup_pairs(cup)
    print('----------------')

print("Winner: " + cup_teams[0])
g1, g2 = simulate(ratings['Луч'], ratings['Ростов'])
g = simulate_game_with_monemts(g1, g2)
print(g)
start_time = tm.time()
g1 = 0
g2 = 0
print('СТАРТ ИГРЫ!\t' + str(g1) + ':' + str(g2))
for time, j in g.items():
    print(time)
    while tm.time() - start_time < 0.4:
        pass
    start_time = tm.time()
    for i in j:
        if i == 1:
            g1 += 1
            print(str(time) + '\tГОЛ!!!\t' + str(g1) + ':' + str(g2))
        else:
            g2 += 1
            print(str(time) + '\tГОЛ!!!\t' + str(g1) + ':' + str(g2))

print('КОНЕЦ ИГРЫ!\t' + str(g1) + ':' + str(g2))
