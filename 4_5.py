from functools import reduce

my_list = []

for number in range(100, 1001):
    if number % 2 == 0:
        my_list.append(number)

print(my_list)
print(reduce(lambda x, y: x * y, my_list))
