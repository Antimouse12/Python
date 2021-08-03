list_1 = input('введите элементы списка: ')
list_1 = list(list_1)
list_2 = []

i = int(list_1[0])
j = int(list_1[1])
z = len(list_1) // 2

for element in range(0, z):
    (i, j) = (j, i)
    list_2.append(i)
    list_2.append(j)
    (j, i) = (i, j)
    i += 2
    j += 2
if len(list_1) % 2 != 0:
    list_2.append(list_1[-1])
print(list_2)
