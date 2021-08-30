from collections import Counter

list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
counts = Counter(list_1)
list_2 = []

for element, count in counts.items():
    if count == 1:
        list_2.append(element)
print(list_2)
