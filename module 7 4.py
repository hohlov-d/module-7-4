team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451


def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return 'Победа команды Волшебники Данных!'
    else:
        return 'Ничья!'


tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total


print('В команде Мастера кода участников:%d!' % team1_num)
print('Итого сегодня в командах участников:%d, %d!' % (team1_num,team2_num))
print('Команда Волшебники данных решила задач:{}!'.format(score_2))
print('Волшебники данных решили задачи за {} c!'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задачи.')
print(f'Результат битвы {challenge_result()}')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!')


