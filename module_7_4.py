team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'
team1 = 'Мастера кода'
team2 = 'Волшебники данных'
# Использование %:
 # team1_num количество участников первой команды
 # team2_num количество участников второй команды
print(f"В команде %s участников: %s ! " % (team1,team1_num))
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

# Использование format():
 # score_2 количество задач решённых командой 2
 # team1_time время за которое команда 2 решила задачи
print('Команда {} решила задач: {} !' .format(team2,score_2))
print(' {} решили задачи за {} !' .format(team2,team2_time))
print('Команда {} решила задач: {} !' .format(team1,score_1))
print(' {} решили задачи за {} !' .format(team1,team1_time))

# Использование f-строк:
 # score_1 количество задач решённых командой 1
 # challenge_result исход соревнования
 # tasks_total количество задач
 # time_avg среднее время решения
print(f"Команды решили {score_1} и {score_2} задач.")


tasks_total = score_1+ score_2
time_avg = round ((team1_time+ team2_time)/ tasks_total), 2

print(f"Сегодня было решено {tasks_total}, в среднем по {time_avg} на задачу!.")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды {team1}!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды {team2}!')


