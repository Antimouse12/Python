rating = [9, 7, 5, 4, 3, 1]
new = int(input('введите новый элемент рейтинга: '))
rating.append(new)
rating.sort(reverse=True)
print(rating)
