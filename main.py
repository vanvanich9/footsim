from random import randrange


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


name_team = 'a'
rate = 0
ratings = {name_team: rate, 'Valencia': 81, 'Man City': 86, 'Bayern': 84
    , 'Mechelen': 69, 'Salzburg': 74, 'Shakhtar': 74, 'Midtjylland': 69
    , 'Shamrock Rovers': 62, 'Lazio': 80, 'Lechia Gdansk': 68, 'Sporting CP': 77
    , 'Ajax': 79, 'Lokomotiv': 76, 'Viking': 65, 'Stade Rennais': 75}
teams = [name_team, 'Valencia', 'Man City', 'Bayern',
         'Mechelen', 'Salzvurg', 'Shakhtar', 'Midtjylland',
         'Shamrock Rovers', 'Lazio', 'Lechia Gdansk', 'Sporting CP',
         'Ajax', 'Lokomotiv', 'Viking', 'Stade Rennais']
divisions = [[['', 0], ['', 0], ['', 0], ['', 0]],
             [['', 0], ['', 0], ['', 0], ['', 0]],
             [['', 0], ['', 0], ['', 0], ['', 0]],
             [['', 0], ['', 0], ['', 0], ['', 0]]]


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


def generate_group():
    for i in range(16):
        l = len(teams)
        index = randrange(0, l, 1)
        divisions[i // 4][i % 4][0] = teams.pop(index)
