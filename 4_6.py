from itertools import count
from itertools import cycle

start = int(input('введите первое число последовательности: '))
for el in count(start):
    if el == start + 10:
        break
    else:
        print(el)


my_list = ['Mr', '&', 'Ms', '4ever', 'Love']
c = 0
for el in cycle(my_list):
    if c > 15:
        break
    else:
        print(el)
        c += 1
