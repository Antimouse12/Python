from sys import argv

script_name, worked_hours, hour_rate, bonus = argv

print('название скрипта: ', script_name)
print('выработка в часах: ', worked_hours)
print('часовая ставка: ', hour_rate)
print('премия: ', bonus)
print(float(worked_hours) * float(hour_rate) + float(bonus))
