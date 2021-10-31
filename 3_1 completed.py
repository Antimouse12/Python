number_1 = int(input('введите число (делимое) : '))
number_2 = int(input('введите число (делитель) : '))

def divide(number_1, number_2):
    if number_2 == 0:
        print('ошибка, на 0 делить нельзя')
    else:
        return number_1 / number_2


divide = divide(number_1, number_2)
print(divide)
