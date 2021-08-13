f_write = open('text_3.txt', 'w')
str_list = [
    'Ivanov 25000\n',
    'Petrov 26000\n',
    'Henderson 15000\n',
    'Livingston 150000\n',
    'Smith 18500\n',
    'Winston 250000\n'
]
f_write.writelines(str_list)
f_write.close()

with open('text_3.txt', 'r') as f_read:
    employees = {}
    for line in f_read:
        key, value = line.split()
        employees[key] = float(value)
    print(
        f'Average employees salary is {round(sum(employees.values()) / len(employees), 2)}\n'
        f'Employees with salary below 20k are: {[el[0] for el in employees.items() if el[1] < 20000]} '
    )
