# Домашнее задание по теме "Форматирование строк".
team1_num : int = 5
team2_num : int = 6
score_1 : int = 40
score_2 : int = 42
team1_time : float = 1552.512
team2_time : float = 2153.31451
tasks_total : int = 82
time_avg : float = 45.2
challenge_result : str = 'Победа команды Волшебники данных!'
result : str = ""

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"

# Использование %:
print("В команде Мастера кода участников: %s! " % team1_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

# Использование format():
print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Волшебники данных решили задачи за {} с!".format(team2_time))

# Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {result}")
tasks_total = score_1 + score_2
time_avg = float.__round__((team1_time + team2_time) / (score_1 + score_2), 2)
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")