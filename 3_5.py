def sum_of_numbers():
    s = 0
    while True:
        numbers_list = input('Введите строку чисел, разделенных пробелом, или х для выхода из программы: ').split()
        for number in numbers_list:
            if number == 'x':
                return s
            else:
                try:
                    s += int(number)
                except ValueError:
                    print('Чтобы выйти из программы, нажмите x - ')
        print(f'сумма чисел = {s}')


print(sum_of_numbers())
