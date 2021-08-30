list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(list_1)

new_list = []

for i in range(0, len(list_1) - 1):
    if list_1[i + 1] > list_1[i]:
        new_list.append(list_1[i + 1])
print(new_list)
