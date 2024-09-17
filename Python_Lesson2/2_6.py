commodities = input('введите товары для анализа через пробел: ')
commodities = commodities.split(' ')
print(commodities)
z = len(commodities)
# print(z)

goods_list = []
goods_dict = []
result_dict = {}
n = 1

while n <= z:
    goods_dict = dict(
        {'название': input('название товара: '),
         'цена': input('введите цену товара: '),
         'количество': input('введите количество товара: '),
         'единица измерения': input('введите единицу измерения для товара: ')})
    goods_list.append((n, goods_dict))
    n += 1

    result_dict = dict(
        {'назв': goods_dict.get('название'),
         'цен': goods_dict.get('цена'),
         'кол-во': goods_dict.get('количество'),
         'ед изм': goods_dict.get('единица измерения')})

print('\n'.join(str(value) for value in goods_list))
print('\n'.join(str(value) for value in result_dict))
# не получается на данном этапе реализовать заполнение словаря, буду ждать разбор на уроке
# print(goods_dict)
# проверила, словарь не формируется, поэтому видимо и словарь не заполняется данными, в рамках цикла только одна итерация создает словарь, остальные товары не добавляются