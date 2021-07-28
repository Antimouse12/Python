revenue = int(input('Ваша выручка в тыс.руб.'))
expenses = int(input('Ваши издержки в тыс.руб.'))

fin_result = revenue - expenses

if fin_result > 0:
    print(f'Ваш бизнес прибыльный, прибыль составила {fin_result} тыс.руб.')
    profit_ratio = fin_result / revenue
    print(f'Коэффициент рентабельности = {profit_ratio}')
    number_of_employees = int(input('Численность ваших сотрудников'))
    profit_per_employee = fin_result / number_of_employees
    print(f'Прибыль на одного сотрудника {profit_per_employee} тыс.руб.')
elif fin_result == 0:
    print(f'Ваш бизнес находится в точке безубыточности, прибыли нет, убытков нет')
else:
    print(f'Ваш бизнес убыточный, убыток составил {fin_result} тыс.руб.')

